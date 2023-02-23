from django.shortcuts import render
from rest_framework import generics, permissions


from .models import Listing
from .serializers import ListingSerializer


# Create your views here.

from .permissions import IsAuthor

class ListingList(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = ((IsAuthor | permissions.IsAdminUser, ))









