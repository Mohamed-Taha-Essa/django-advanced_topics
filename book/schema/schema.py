import graphene
from .queries import Query as BooksQuery
from .mutations import Mutation as BooksMutation

#apply all query 
class Query(BooksQuery, graphene.ObjectType):
    pass

#apply all mutations
class Mutation(BooksMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)