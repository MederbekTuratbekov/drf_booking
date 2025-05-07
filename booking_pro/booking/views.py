from rest_framework import viewsets
from rest_framework import generics
from .models import UserProfile, Country, City, ChoiceCity, Hotel, HotelImages, Apartment, ApartmentImages, Reviews, Booking
from .serializers import (UserProfileSerializer, CountrySerializers, CitySerializers, ChoiceCitySerializers, HotelSerializers, HotelImagesSerializers,
                          ApartmentSerializers, ApartmentImagesSerializers, ReviewsSerializers, BookingSerializers)


class UserProfileListAPIView(generics.ListAPIVIew):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CountryListAPIView(generics.ListAPIVIew):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers

class CityListAPIView(generics.ListAPIVIew):
    queryset = City.objects.all()
    serializer_class = CitySerializers

class ChoiceCityListAPIView(generics.ListAPIVIew):
    queryset = ChoiceCity.objects.all()
    serializer_class = ChoiceCitySerializers

class HotelListAPIView(generics.ListAPIVIew):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers

class HotelImagesListAPIView(generics.ListAPIVIew):
    queryset = HotelImages.objects.all()
    serializer_class = HotelImagesSerializers

class ApartmentListAPIView(generics.ListAPIVIew):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializers

class ApartmentImagesListAPIView(generics.ListAPIVIew):
    queryset = ApartmentImages.objects.all()
    serializer_class = ApartmentImagesSerializers

class ReviewsListAPIView(generics.ListAPIVIew):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers

class BookingListAPIView(generics.ListAPIVIew):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
