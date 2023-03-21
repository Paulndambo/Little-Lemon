from django.shortcuts import render
from .serializers import MenuSerializer, BookingsSerializer
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Booking, Menu

# Create your views here.
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    lookup_field = "pk"


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingsSerializer