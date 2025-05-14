from django.urls import path, include
from .views import UserProfileListAPIView, ChoiceCityListAPIView, HotelListAPIView, ApartmentListAPIView, ReviewsListAPIView, BookingListAPIView, FavoriteItemAPIView
from .views import RegisterView, CustomLoginView, LogoutView, ManageHotelViewSet, ManageApartmentViewSet, ReviewsReadAPIView
from .views import BookingCancelAPIView


urlpatterns = [
    path('user/', UserProfileListAPIView.as_view(), name = 'users'),
    path('', ChoiceCityListAPIView.as_view(), name = 'cities'),
    path('hotel/', HotelListAPIView.as_view(), name = 'hotels'),
    path('hotel/<int:pk>/', ApartmentListAPIView.as_view(), name = 'apartments'),
    path('review/', ReviewsListAPIView.as_view(), name = 'reviews'),
    path('review/<int:pk>', ReviewsReadAPIView.as_view(), name='read_reviews'),
    path('booking/', BookingListAPIView.as_view(), name = 'bookings'),
    path('manage_hotel/', ManageHotelViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy', 'patch': 'update'}), name = 'manage_hotels'),
    path('manage_apartment/', ManageApartmentViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy', 'patch': 'update'}), name = 'manage_apartments'),
    path('booking/<int:pk>/cancel/', BookingCancelAPIView.as_view(), name='cancel_booking'),
    path('favorite/', FavoriteItemAPIView.as_view(), name='favorite'),

    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]
