from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import Listing


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', )



class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ('id', 'shoe_id', 'price', 'author', 'shoe_size')

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['author'] = AuthorSerializer(instance.author).data
        return response


