import graphene

from user.models import User
from learning_space.models import LearningSpace


from my_graphql.types.user import UserType
from my_graphql.types.learning_space import LearningSpaceType

from .mutations.create_user import CreateUserMutation
from .mutations.learning_space import (
    CreateLearningSpaceMutation,
    DeleteLearningSpaceMutationById,
)


class Mutation(graphene.ObjectType):
    create_learning_space = CreateLearningSpaceMutation.Field()
    delete_learning_space_by_id = DeleteLearningSpaceMutationById.Field()
    create_user = CreateUserMutation.Field()


class Query(graphene.ObjectType):
    learning_spaces_by_user_id = graphene.List(
        LearningSpaceType, user_id=graphene.String(required=True)
    )
    user_by_id = graphene.Field(UserType, id=graphene.String(required=True))

    def resolve_learning_spaces_by_user_id(root, info, user_id):
        return LearningSpace.objects.filter(user=user_id)

    def resolve_user_by_id(root, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExists:
            return None


schema = graphene.Schema(query=Query, mutation=Mutation)
