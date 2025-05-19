import graphene

from learning_space.graphql.learning_space_type import LearningSpaceType

from learning_space.models import LearningSpace


class LearningSpaceQueries(graphene.ObjectType):
    learning_spaces_by_user_id = graphene.List(
        LearningSpaceType, user_id=graphene.String(required=True)
    )

    def resolve_learning_spaces_by_user_id(root, info, user_id):
        return LearningSpace.objects.filter(user=user_id)
