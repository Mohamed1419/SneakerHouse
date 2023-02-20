from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Listing


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username',)

class ListingSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Listing
        fields = ('id', 'shoe', 'price', 'author', 'shoe_size')

        def create(self, validated_data):
            author_data = validated_data.pop('author')
            (author, _) = get_user_model().objects.get_or_create(**author_data)
            listing = Listing.objects.create(**validated_data, author=author)
            return listing