import graphene

from my_graphql.types.user import UserType

from user.models import User


class UserQuery(graphene.ObjectType):
    user_by_id = graphene.Field(UserType, id=graphene.String(required=True))

    def resolve_user_by_id(root, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExists:
            return None
