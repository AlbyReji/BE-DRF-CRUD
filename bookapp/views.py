from .models import Books
from .serializers import BookSerializer
from rest_framework import generics

class BookCreateList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer



class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

