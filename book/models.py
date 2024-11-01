from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    biography = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        'Category', related_name='book_category', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(
        Author, related_name='book_author', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book')       #must add media and static setting
    publication_date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=3000)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(
        Book, related_name='review_book', on_delete=models.CASCADE)
    reviewer_name = models.ForeignKey(
        User, related_name='reviw_user', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.book.title}"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category')

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name