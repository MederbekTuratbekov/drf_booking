from django.urls import path
from .views import UserProfileListAPIView, ChoiceCityListAPIView, HotelListAPIView, ApartmentListAPIView, ReviewsListAPIView, BookingListAPIView
                    # CountryListAPIView, CityListAPIView, HotelImagesListAPIView, ApartmentImagesListAPIView
from .views import RegisterView, CustomLoginView, LogoutView


urlpatterns = [
    path('user/', UserProfileListAPIView.as_view(), name = 'users'),
    path('', ChoiceCityListAPIView.as_view(), name = 'cities'),
    path('hotels/', HotelListAPIView.as_view(), name = 'hotels'),
    path('hotels/<int:pk>/', ApartmentListAPIView.as_view(), name = 'apartments'),
    path('review/', ReviewsListAPIView.as_view(), name = 'reviews'),
    path('booking/', BookingListAPIView.as_view(), name = 'booking'),

    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]
