import graphene

from my_graphql.mutations.learning_space import LearningSpaceMutation
from my_graphql.queries.learning_space_query import LearningSpaceQuery

from user.graphql.user_queries import UserQuery
from user.graphql.user_mutations import UserMutations


class Mutation(UserMutations, LearningSpaceMutation, graphene.ObjectType):
    pass


class Query(LearningSpaceQuery, UserQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
