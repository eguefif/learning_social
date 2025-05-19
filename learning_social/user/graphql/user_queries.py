import graphene

from user.graphql.user_type import UserType

from ..models import User


class UserQuery(graphene.ObjectType):
    user_by_id = graphene.Field(UserType, id=graphene.String(required=True))

    def resolve_user_by_id(root, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None
