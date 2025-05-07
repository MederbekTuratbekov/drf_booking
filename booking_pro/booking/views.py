from rest_framework import viewsets
from rest_framework import generics
from .models import UserProfile, Country, City, ChoiceCity, Hotel, HotelImages, Apartment, ApartmentImages, Reviews, Booking
from .serializers import (UserProfileSerializer, CountrySerializers, CitySerializers, ChoiceCitySerializers, HotelSerializers, HotelImagesSerializers,
                          ApartmentSerializers, ApartmentImagesSerializers, ReviewsSerializers, BookingSerializers)


class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers

class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializers

class ChoiceCityListAPIView(generics.ListAPIView):
    queryset = ChoiceCity.objects.all()
    serializer_class = ChoiceCitySerializers

class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers

class HotelImagesListAPIView(generics.ListAPIView):
    queryset = HotelImages.objects.all()
    serializer_class = HotelImagesSerializers

class ApartmentListAPIView(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializers

class ApartmentImagesListAPIView(generics.ListAPIView):
    queryset = ApartmentImages.objects.all()
    serializer_class = ApartmentImagesSerializers

class ReviewsListAPIView(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers

class BookingListAPIView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
