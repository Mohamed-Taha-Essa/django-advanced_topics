import graphene
from graphene_django import DjangoObjectType

from .models import Category, Book ,Author ,Review

class CategoryType(DjangoObjectType):
    book_count = graphene.Int() 

    class Meta:
        model = Category
        fields = ('name' ,'image' ,'book_count')
        
    def resolve_book_count(self, info):
        return self.book_category.count() 
    
    
class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title","image", "author", "category" ,'publication_date' ,"price" ,"description")
        # fields = "__all__"

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('name' ,'age' ,'biography')
        # fields = "__all__"

class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        fields = ("book", "reviewer_name", "content", "created_at" ,'rating' )
        # fields = "__all__"



class Query(graphene.ObjectType):
    books = graphene.List(BookType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    authors = graphene.List(AuthorType)

    def resolve_books(root, info):
        return Book.objects.select_related("category" ,'author').all()

    def resolve_authors(root, info):
        return Author.objects.all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)