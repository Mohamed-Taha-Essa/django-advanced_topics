# like serialzers.py 
#build on pydantic  


from ninja import Schema 
from datetime import date
from typing import Optional


#djanog ninga - fast api
#in to db (add ,edit ) ,out from db(list ,detail) 

class AuthorOut(Schema):
    id : int
    name : str 
    age :int
    biography :str

class CategoryOut(Schema):
    id:int 
    name:str

class BookIn(Schema): #add ,edit 
    title:str
    category : int
    author :int
    publication_date: date
    price: float
    description: str
    quantity: int

class BookOut(Schema):#show :Get
    id :int
    title:str
    category : CategoryOut
    author : AuthorOut
    publication_date: date
    price: float
    description: str
    quantity: int

    