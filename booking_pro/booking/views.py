from .models import UserProfile, ChoiceCity, Hotel, Apartment, Reviews, Booking
from .serializers import UserProfileSerializer, ChoiceCitySerializers, HotelSerializers, ApartmentSerializers, \
    ReviewsSerializers, BookingSerializers, UserSerializer, LoginSerializer
#Country, City, HotelImages, ApartmentImages, CountrySerializers, CitySerializers, HotelImagesSerializers, ApartmentImagesSerializers
from  rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, generics, permissions
from .filters import ApartmentFilter
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

class ChoiceCityListAPIView(generics.ListAPIView):
    queryset = ChoiceCity.objects.all()
    serializer_class = ChoiceCitySerializers

class HotelListAPIView(generics.ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers

class ApartmentListAPIView(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = ApartmentFilter
    # ordering_fields = ['field_name1', 'field_name2']
    # ordering = ['field_name1']
    # search_fields = ['title', 'description']
    # permissions = [permissions.IsAuthenticated]

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
