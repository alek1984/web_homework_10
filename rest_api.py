from rest_framework import serializers
from .models import CustomUser
from mongoengine.django.auth import User
from .mongodb_models import Author, Quote

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email"]

class AuthorSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    birth_date = serializers.CharField()
    birth_place = serializers.CharField()
    description = serializers.CharField()

    def create(self, validated_data):
        return Author(**validated_data).save()

class QuoteSerializer(serializers.Serializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects)
    text = serializers.CharField()
    tags = serializers.ListField(child=serializers.CharField())

    def create(self, validated_data):
        return Quote(**validated_data).save()
