import os ,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
from book.models import Book,Author,Category, Review  
import random
from django.utils.text import slugify
from django.contrib.auth.models import User



fake=Faker()

def seed_category(num_categorys):
    imgs =['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg', ]
    for _ in range(num_categorys):
        category = Category.objects.create(
            name=fake.company(),
            image=f'category/{imgs[random.randint(0,5)]}',
        )
    
    print('Category addec successfully')

def seec_author(n):
    for _ in range(n):
        Author.objects.create(
            name = fake.name(),
            age = random.randint(30, 80) ,
            biography =fake.paragraph(nb_sentences = 20),
        )

def seed_book(n):
    imgs =['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg',
           '07.jpg','08.jpg','09.jpg','10.jpg','11.jpg','12.jpg',
           '13.jpg','14.jpg','15.jpg','16.jpg','17.jpg','18.jpg',
           '19.jpg','20.jpg',
        ]

    category =Category.objects.all()
    author= Author.objects.all()
    for _ in range(n):
        name = fake.company()  # Generate a fake company name
        
        Book.objects.create(
            category =category[random.randint(0,len(category)-1)] ,
            title = name,
            author =author[random.randint(0,len(author)-1)] ,

            image = f'book/{imgs[random.randint(0,19)]}',
            price = fake.random_number(digits=2),
            description=fake.paragraph(nb_sentences = 80),
            quantity = random.randint(1, 100)
        )
    print('Books added successfully')

def seed_review(n):
    user = User.objects.all()
    book = Book.objects.all()
    for i in range(n) :
        for j in range(0,2):
            Review.objects.create(
                reviewer_name = user[random.randint(0 ,len(user)-1)],
                book =book[i],
                content = fake.sentence(nb_words =45),
                rating = fake.random_element(elements = (i for i in range(1,6))),
            )
    print('added review successfully ')


seed_category(20)
seec_author(70)
seed_book(300)
seed_review(300)