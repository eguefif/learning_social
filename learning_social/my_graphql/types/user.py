from graphene_django import DjangoObjectType
from user.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")
