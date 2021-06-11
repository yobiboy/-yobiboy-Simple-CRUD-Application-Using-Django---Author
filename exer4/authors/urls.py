from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), 
    path('createAuthor/', views.createAuthor, name="create author"), 
    path('updateAuthor/<str:pk>', views.updateAuthor, name="update author"), 
    path('deleteAuthor/<str:pk>', views.deleteAuthor, name="delete author"), 
    path('createBook/', views.createBook, name="create book"), 
    path('updateBook/<str:pk>', views.updateBook, name="update book"), 
    path('deleteBook/<str:pk>', views.deleteBook, name="delete book"), 
]
