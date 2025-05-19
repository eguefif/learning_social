import graphene

from my_graphql.types.learning_space import LearningSpaceType

from learning_space.models import LearningSpace


class LearningSpaceQuery(graphene.ObjectType):
    learning_spaces_by_user_id = graphene.List(
        LearningSpaceType, user_id=graphene.String(required=True)
    )

    def resolve_learning_spaces_by_user_id(root, info, user_id):
        return LearningSpace.objects.filter(user=user_id)
