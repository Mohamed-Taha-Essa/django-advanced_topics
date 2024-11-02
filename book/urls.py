from django.urls import path
from .views import router
from ninja import NinjaAPI

api =NinjaAPI()

api.add_router('/books' ,router)
urlpatterns = [
    path('api/', api.urls),
]