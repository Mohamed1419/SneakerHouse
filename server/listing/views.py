from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Listing
from .serializers import ListingSerializer


# Create your views here.

from .permissions import IsAuthorOrReadonly

class ListingList(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = ((IsAuthorOrReadonly | permissions.IsAdminUser, ))









