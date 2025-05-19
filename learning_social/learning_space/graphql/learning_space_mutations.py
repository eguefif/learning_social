import graphene

from learning_space.models import LearningSpace
from user.models import User


from learning_space.graphql.learning_space_type import LearningSpaceType


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


class LearningSpaceMutation(graphene.ObjectType):
    create_learning_space = CreateLearningSpaceMutation.Field()
    delete_learning_space_by_id = DeleteLearningSpaceMutationById.Field()
