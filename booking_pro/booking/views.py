from .models import UserProfile, ChoiceCity, Hotel, Apartment, Reviews, Booking, FavoriteItem
from .serializers import (UserProfileSerializer, ChoiceCitySerializers, HotelSerializers, ApartmentSerializers, ReviewsSerializers, BookingSerializers,
                          UserSerializer, LoginSerializer, ManageHotelSerializers, ManageApartmentSerializers, ReviewsReadSerializers, FavoriteItemSerializers)
from  rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, generics, permissions, viewsets, permissions
from .filters import ApartmentFilter, ChoiceCityFilter, HotelFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import serializers
from .permissions import CheckRole, CheckUserRoleReviews


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)

class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# ——————————————————————————
class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permissions = [permissions.IsAdminUser]

class ChoiceCityListAPIView(generics.ListAPIView):
    queryset = ChoiceCity.objects.all()
    serializer_class = ChoiceCitySerializers
    permissions = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ChoiceCityFilter
    search_fields = ['country', 'city']

class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = HotelFilter
    permission_classes = [CheckRole]

class ApartmentListAPIView(generics.RetrieveAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = ApartmentFilter
    ordering_fields = ['apartment_price', 'apartment_number']
    ordering = ['apartment_price']
    search_fields = ['apartment_description', 'apartment_type', 'hotel_name__hotel_name']
    permissions = [permissions.AllowAny]

class ReviewsListAPIView(generics.CreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckUserRoleReviews]

    def perform_create(self, serializer):
        hotel = serializer.validated_data.get('hotel')
        user = self.request.user

        # Проверка, является ли пользователь владельцем отеля
        if hotel and hotel.hotel_owner == user:
            raise serializers.ValidationError("Владельцы отелей не могут оставлять отзывы на свои отели.")

        # Проверка, оставлял ли пользователь уже отзыв на этот отель
        if hotel and Reviews.objects.filter(review_author=user, hotel=hotel).exists():
            raise serializers.ValidationError("Вы уже оставили отзыв на этот отель.")

        serializer.save(review_author=user)

class ReviewsReadAPIView(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsReadSerializers
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        hotel_id = self.kwargs.get('pk')  # Получаем ID отеля из URL
        return Reviews.objects.filter(hotel_id=hotel_id)  # Фильтруем отзывы по отелю

class BookingListAPIView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [CheckUserRoleReviews]

    def perform_create(self, serializer):
        serializer.save(user_reservation=self.request.user)

class BookingCancelAPIView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Только пользователь, создавший бронирование, может его отменить
        return Booking.objects.filter(user_reservation=self.request.user)

    def perform_destroy(self, instance):
        # Удаляем бронирование, что вызовет метод delete в модели Booking
        instance.delete()

class ManageHotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = ManageHotelSerializers
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Hotel.objects.filter(hotel_owner=self.request.user)

class ManageApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ManageApartmentSerializers
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Apartment.objects.filter(hotel_name__hotel_owner=self.request.user)

class FavoriteItemAPIView(generics.ListAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemSerializers
