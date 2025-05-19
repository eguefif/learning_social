import graphene

from learning_space.graphql.learning_space_mutations import LearningSpaceMutation
from learning_space.graphql.learning_space_queries import LearningSpaceQueries

from user.graphql.user_queries import UserQuery
from user.graphql.user_mutations import UserMutations


class Mutation(UserMutations, LearningSpaceMutation, graphene.ObjectType):
    pass


class Query(LearningSpaceQueries, UserQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
