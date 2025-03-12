from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import AuthorSerializer, QuoteSerializer
from .mongodb_models import Author, Quote

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects
    serializer_class = QuoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
