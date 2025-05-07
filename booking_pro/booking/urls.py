from django.urls import path
from .views import UserProfileListAPIView, ChoiceCityListAPIView, HotelListAPIView, ApartmentListAPIView, ReviewsListAPIView, BookingListAPIView
                    # CountryListAPIView, CityListAPIView, HotelImagesListAPIView, ApartmentImagesListAPIView


urlpatterns = [
    path('user/', UserProfileListAPIView.as_view(), name = 'users'),
    path('', ChoiceCityListAPIView.as_view(), name = 'cities'),
    path('hotels/', HotelListAPIView.as_view(), name = 'hotels'),
    path('hotels/<int:pk>/', ApartmentListAPIView.as_view(), name = 'apartments'),
    path('review/', ReviewsListAPIView.as_view(), name = 'reviews'),
    path('booking/', BookingListAPIView.as_view(), name = 'booking'),
]
