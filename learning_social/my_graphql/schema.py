import graphene

from my_graphql.queries.learning_space_query import LearningSpaceQuery
from my_graphql.queries.user_query import UserQuery

from my_graphql.mutations.learning_space import LearningSpaceMutation
from my_graphql.mutations.user import UserMutation


class Mutation(UserMutation, LearningSpaceMutation, graphene.ObjectType):
    pass


class Query(LearningSpaceQuery, UserQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
