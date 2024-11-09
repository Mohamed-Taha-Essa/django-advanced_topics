import graphene
from .queries import Query as BooksQuery
from .mutations import Mutation as BooksMutation

class Query(BooksQuery, graphene.ObjectType):
    pass

class Mutation(BooksMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)