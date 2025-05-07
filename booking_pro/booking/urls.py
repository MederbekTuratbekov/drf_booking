from django.urls import path
from .views import (UserProfileListAPIView, CountryListAPIView, CityListAPIView, ChoiceCityListAPIView, HotelListAPIView, HotelImagesListAPIView,
                    ApartmentListAPIView, ApartmentImagesListAPIView, ReviewsListAPIView, BookingListAPIView)


urlpatterns = [
    path('user/', UserProfileListAPIView.as_views(), name = 'users'),
    path('', ChoiceCityListAPIView.as_views(), name = 'cities'),
    path('hotels/', HotelListAPIView.as_views(), name = 'hotels'),
    path('hotels/<int:pk>/', ApartmentListAPIView.as_views(), name = 'apartments'),
    path('review/', ReviewsListAPIView.as_views(), name = 'reviews'),
    path('booking/', BookingListAPIView.as_views(), name = 'booking'),
]
