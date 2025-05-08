from .models import UserProfile, ChoiceCity, Hotel, Apartment, Reviews, Booking
from .serializers import (UserProfileSerializer, ChoiceCitySerializers, HotelSerializers, ApartmentSerializers, ReviewsSerializers, BookingSerializers,
                          UserSerializer, LoginSerializer, ManageHotelSerializers, ManageApartmentSerializers)
#Country, City, HotelImages, ApartmentImages, CountrySerializers, CitySerializers, HotelImagesSerializers, ApartmentImagesSerializers
from  rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, generics, permissions, viewsets
from .filters import ApartmentFilter, ChoiceCityFilter, HotelFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


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
    permissions = [permissions.AllowAny]

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
    permissions = [permissions.IsAuthenticated]

class BookingListAPIView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializers
    permissions = [permissions.IsAuthenticated]

class ManageHotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = ManageHotelSerializers
    permissions = [permissions.IsAdminUser]

class ManageApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ManageApartmentSerializers
    permissions = [permissions.IsAdminUser]

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
