import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoFormMutation

from django import forms
from .models import Category, Book ,Author ,Review

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
        # fields = "__all__"

    def resolve_review(self, info) :
        return self.review_book.all()

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ('name' ,'age' ,'biography')
        # fields = "__all__"


class FormBook(forms.ModelForm):
    class Meta:
        model = Book
        fields="__all__"

class MutationBook(DjangoFormMutation):
    success = graphene.Boolean()  # Success status field
    book = graphene.Field(BookType)  # The field to return the created book

    class Meta:
        form_class = FormBook

    @classmethod
    def perform_mutate(cls, form, info):
        # Save the form, creating the new book instance
        book = form.save()
        # Return the success status and the book instance
        return cls(success=True, book=book)


class Query(graphene.ObjectType):
    books = graphene.List(BookType)
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

class Mutation(graphene.ObjectType):
    create_book = MutationBook.Field()
schema = graphene.Schema(query=Query ,mutation=Mutation )