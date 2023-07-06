from django.urls import path
from . import views

urlpatterns = [
    path('<int:booklist_id>/', views.booklist, name='booklist'),
    path('edit/<int:booklist_id>/', views.booklist_edit, name='booklist_edit'),
    path('delete/<int:booklist_id>/', views.booklist_delete, name='booklist_delete'),
    path('', views.booklists_collection, name='booklists_collection'),
    path('new/', views.booklist_new, name='booklist_new'),  


]
