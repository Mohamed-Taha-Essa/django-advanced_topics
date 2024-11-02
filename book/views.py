#api 

from .schemas import BookIn ,BookOut ,AuthorOut ,CategoryOut
from ninja import Router #url 
from ninja import Query
from .models import Book ,Author ,Category
from .filters import BookFilterSchema
from typing import List , Optional 



#create router 

router = Router()


#book list api

@router.get('/' , response={200:list[BookOut]})
def books_list(request ,filters: BookFilterSchema = Query(...)):
    books = Book.objects.all()
    books = filters.filter(books)

    return books

@router.get('/{book_id}' , response={200:BookOut})
def book_detail(request , book_id):
    book = Book.objects.get(id = book_id)
    return book

@router.post('/' , response={200:BookOut})
def create_book(request , payload:BookIn):
    data = payload.dict()
    author = Author.objects.get(id = data['author'])
    category = Category.objects.get(id = data['category'])
    book = Book.objects.create(
        title = data['title'],
        author = author ,
        category = category,
        publication_date =data['publication_date'],
        price = data['price'],
        description = data['description'],
        quantity= data['quantity']


    ) 
    return book

@router.put('/{book_id}' , response={200:BookOut})
def update_book(request , book_id ,payload:BookIn):
    book = Book.objects.get(id = book_id)
    data = payload.dict()
    author = Author.objects.get(id = data['author'])
    category = Category.objects.get(id = data['category'])

    book.title = data['title']
    book.author = author 
    book.category = category
    book.publication_date =data['publication_date']
    book.price = data['price']
    book.description = data['description']
    book.quantity= data['quantity']

    book.save()
    return book

@router.delete('/{book_id}' )
def delet_book(request , book_id):
    book = Book.objects.get(id = book_id)
    book.delete()
    return {'message':'successfully deleted'}