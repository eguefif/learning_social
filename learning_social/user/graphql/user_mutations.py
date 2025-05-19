import graphene

from user.graphql.user_type import UserType

from user.graphql.user_inputs import CreateUserInput

from user.models import User


class CreateUserMutation(graphene.Mutation):
    class Arguments:
        user_data = CreateUserInput(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, user_data):
        user = User(
            username=user_data.username,
            password="",
            first_name=user_data.first_name,
            last_name=user_data.last_name,
        )
        user.set_password(user_data.password)
        user.save()
        return CreateUserMutation(user=user)


class UserMutations(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
