import graphene
from graphene_django import DjangoObjectType

from user.models import User
from learning_space.models import LearningSpace


class LearningSpaceType(DjangoObjectType):
    class Meta:
        model = LearningSpace
        fields = ("id", "name", "description", "author")


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username")


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


schema = graphene.Schema(query=Query)
