from graphene_django import DjangoObjectType
from learning_space.models import LearningSpace


class LearningSpaceType(DjangoObjectType):
    class Meta:
        model = LearningSpace
        fields = ("id", "name", "description", "user")
