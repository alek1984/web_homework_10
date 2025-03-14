from rest_framework import serializers
from .models import Quote, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class QuoteSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Quote
        fields = '__all__'

