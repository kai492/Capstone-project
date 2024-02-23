from django.shortcuts import render
from rest_framework import generics, viewsets
from . models import Menu, Booking
from .serializers import MenuSerializer, Bookingserializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core import serializers
from datetime import datetime
import json
from .forms import BookingForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, 'index.html', {})



class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
     permission_classes = [IsAuthenticated]
     queryset = Booking.objects.all()
     serializer_class = Bookingserializer


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})


def home(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html',)

def about(request):
    return render(request, 'about.html')

def reservations(request):
    date = request.GET.get("date", datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize("json", bookings)
    bookings_data = {"bookings": bookings}
    return render(request, "bookings.html", {"bookings": bookings_data})


def book(request):
     form = BookingForm()
     if request.method == 'POST':
         form = BookingForm(request.POST)
         if form.is_valid():
             form.save()
     context = {'form':form}
     return render(request, 'book.html', context)

# Add code for the bookings() view
@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data=json.load(request)
        exist= (
            Booking.objects.filter(reservation_date=data['reservation_date'])
            .filter(reservation_slot=data['reservation_slot'])
            .exists()
        )
        if exist is False:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json') 
   
    date = request.GET.get('date', datetime.today().date()) 
    
    bookings = Booking.objects.all().filter(reservation_date=date)   
    booking_json = serializers.serialize('json',bookings)
    
    return HttpResponse(booking_json, content_type = 'application/json')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 