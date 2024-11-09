import graphene
from graphene import relay

from book.filters import BookFilter
from graphene_django.filter import DjangoFilterConnectionField

from .types import BookType , AuthorType ,ReviewType ,CategoryType ,BookConnection
from ..models import Category, Book ,Author ,Review

class Query(graphene.ObjectType):
    books = graphene.List(BookType)
    all_books = DjangoFilterConnectionField(BookType ,filterset_class =BookFilter )

    book = graphene.Field(BookType ,id = graphene.Int(required = True))
    
    authors = graphene.List(AuthorType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    

    def resolve_books(root, info):
        return Book.objects.select_related("category" ,'author').all()
    
    def resolve_book(root, info ,id):
        return Book.objects.select_related("category" ,'author').get(id=id)


    def resolve_authors(root, info):
        return Author.objects.all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
