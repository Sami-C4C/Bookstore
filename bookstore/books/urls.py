from django.urls import path
from . import views

urlpatterns = [
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('edit/<int:book_id>/', views.book_edit, name='book_edit'),
    path('delete/<int:book_id>/', views.book_delete, name='book_delete'),
    path('', views.books_collection, name='books_collection'),
    path('add/', views.add_book, name='add_book'),  

]
