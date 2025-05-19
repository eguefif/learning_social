import graphene
from graphene_django import DjangoObjectType

from user.models import User
from learning_space.models import LearningSpace


class LearningSpaceType(DjangoObjectType):
    class Meta:
        model = LearningSpace
        fields = ("id", "name", "description", "user")


class CreateLearningSpaceMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    learning_space = graphene.Field(LearningSpaceType)

    @classmethod
    def mutate(cls, root, info, name, description):
        user = User.objects.get(id=1)
        learning_space = LearningSpace(name=name, description=description, user=user)
        learning_space.save()
        return CreateLearningSpaceMutation(learning_space=learning_space)


class DeleteLearningSpaceMutationById(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    learning_space = graphene.Field(LearningSpaceType)

    @classmethod
    def mutate(cls, root, info, id):
        learning_space = LearningSpace.objects.get(id=id)
        learning_space.delete()
        return DeleteLearningSpaceMutationById(learning_space=learning_space)


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username")


class Mutation(graphene.ObjectType):
    create_learning_space = CreateLearningSpaceMutation.Field()
    delete_learning_space_by_id = DeleteLearningSpaceMutationById.Field()


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
