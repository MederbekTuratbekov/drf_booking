from rest_framework import viewsets
from rest_framework import generics
from .models import UserProfile, ChoiceCity, Hotel, Apartment, Reviews, Booking
from .serializers import UserProfileSerializer, ChoiceCitySerializers, HotelSerializers, ApartmentSerializers, ReviewsSerializers, BookingSerializers
                          #Country, City, HotelImages, ApartmentImages, CountrySerializers, CitySerializers, HotelImagesSerializers, ApartmentImagesSerializers


class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ChoiceCityListAPIView(generics.ListAPIView):
    queryset = ChoiceCity.objects.all()
    serializer_class = ChoiceCitySerializers

class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers

class ApartmentListAPIView(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializers

class ReviewsListAPIView(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers

class BookingListAPIView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers

# class CountryListAPIView(generics.ListAPIView):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializers

# class CityListAPIView(generics.ListAPIView):
#     queryset = City.objects.all()
#     serializer_class = CitySerializers

# class HotelImagesListAPIView(generics.ListAPIView):
#     queryset = HotelImages.objects.all()
#     serializer_class = HotelImagesSerializers

# class ApartmentImagesListAPIView(generics.ListAPIView):
#     queryset = ApartmentImages.objects.all()
#     serializer_class = ApartmentImagesSerializers
