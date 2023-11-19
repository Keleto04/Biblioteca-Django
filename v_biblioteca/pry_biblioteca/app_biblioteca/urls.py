from django.urls import path, include
from app_biblioteca import views

urlpatterns = [
    path('', views.home, name="home"),
    path('authors/', views.list_authors, name="list_authors"),
    path('authors/insert', views.insert_author, name="insert_author"),
    path('authors/update/<int:id>', views.update_author, name="update_author"),
    path('authors/delete/<int:id>', views.delete_author, name="delete_author"),
    path('books/', views.list_books, name="list_books"),
    path('books/insert', views.insert_book, name="insert_book"),
    path('books/update/<int:id>', views.update_book, name="update_book"),
    path('books/delete/<int:id>', views.delete_book, name="delete_book"),
]
