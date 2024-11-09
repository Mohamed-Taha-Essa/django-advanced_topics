import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from book.filters import BookFilter
from ..models import Category, Book ,Author ,Review


class CategoryType(DjangoObjectType):
    book_count = graphene.Int() 

    class Meta:
        model = Category
        fields = ('name' ,'image' ,'book_count')
        
    def resolve_book_count(self, info):
        return self.book_category.count() 
    
class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        fields = ("book", "reviewer_name", "content", "created_at" ,'rating' )
        
        # fields = "__all__"    
    
class BookType(DjangoObjectType):
    review = graphene.List(ReviewType)
    class Meta:
        model = Book
        fields = ("id", "title","image","review", "author", "category" ,'publication_date' ,"price" ,"description")
        # filterset_class = BookFilter 
        interfaces = (relay.Node,) 

    def resolve_review(self, info) :
        return self.review_book.all()

class BookConnection(relay.Connection):
    class Meta:
        node = BookType

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('name' ,'age' ,'biography')
        # fields = "__all__"
