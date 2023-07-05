from django.urls import path
from .import views

urlpatterns = [
    path('', views.BookCreateList.as_view(), name='booklist'),
    path('<int:pk>/', views.BookDetail.as_view(), name='bookDetail'),
]