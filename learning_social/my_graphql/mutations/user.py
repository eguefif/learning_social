import graphene
from passlib.context import CryptContext

from my_graphql.types.user import UserType

from my_graphql.inputs.create_user import CreateUserInput

from user.models import User


class CreateUserMutation(graphene.Mutation):
    class Arguments:
        user_data = CreateUserInput(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, user_data):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hash_password = pwd_context.hash(user_data["password"])
        user = User(
            username=user_data["username"],
            password=hash_password,
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
        )
        user.save()
        return CreateUserMutation(user=user)


class UserMutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
