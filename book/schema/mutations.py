from graphene_django.forms.mutation import DjangoFormMutation
import graphene
from django import forms
from .types import BookType , AuthorType ,ReviewType 
from ..models import Category, Book ,Author ,Review



class FormBook(forms.ModelForm):
    class Meta:
        model = Book
        fields="__all__"

class CreateBookMutation(DjangoFormMutation):
    success = graphene.Boolean()  # Success status field
    book = graphene.Field(BookType)  # The field to return the created book

    class Meta:
        form_class = FormBook

    @classmethod
    def perform_mutate(cls, form, info):
        if form.is_valid():
            book = form.save()
            return cls(success=True, book=book)
        else:
            # If the form is not valid, return success=False
            return cls(success=False, book=None)
    

class UpdateBookMutation(graphene.Mutation):
    success = graphene.Boolean()  # To indicate if the mutation was successful
    book = graphene.Field(BookType)  # To return the updated book data

    class Arguments:
        id = graphene.ID(required=True)  # The ID of the book to update
        title = graphene.String()
        category = graphene.ID()
        author = graphene.ID()
        publication_date = graphene.Date()
        description = graphene.String()
        quantity = graphene.Int()
        price = graphene.Decimal()
        image = graphene.String()

    def mutate(self, info, id, **kwargs):
        try:
            # Attempt to retrieve the book by ID
            book = Book.objects.get(id=id)
            author = Author.objects.get(id = kwargs['author'])
            category = Category.objects.get(id = kwargs['category'])
            book.title = kwargs['title']
            book.author = author 
            book.category = category
            book.publication_date =kwargs['publication_date']
            book.price = kwargs['price']
            book.description = kwargs['description']
            book.quantity= kwargs['quantity']

            book.save()

            return UpdateBookMutation(success=True, book=book)
        except Book.DoesNotExist:
            return UpdateBookMutation(success=False, book=None)
        except Category.DoesNotExist:
            return UpdateBookMutation(success=False, book=None)
        except Author.DoesNotExist:
            return UpdateBookMutation(success=False, book=None)

class DeleteBookMutation(graphene.Mutation):
    success = graphene.Boolean()  
    message = graphene.String()    

    class Arguments:
        id = graphene.ID(required=True)  

    @classmethod
    def mutate(cls, root, info, id):
        try:
            book = Book.objects.get(id=id)
            book.delete()  
            return cls(success=True, message="Book deleted successfully.")
        except Book.DoesNotExist:
            return cls(success=False, message="Book not found.")


class Mutation(graphene.ObjectType):
    create_book = CreateBookMutation.Field()
    update_book = UpdateBookMutation.Field()
    delete_book = DeleteBookMutation.Field()