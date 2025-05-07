from rest_framework import serializers
from .models import UserProfile, Country, City, ChoiceCity, Hotel, HotelImages, Apartment, ApartmentImages, Reviews, Booking
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number', 'status', 'date_registered')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
# -----------------------------------------------------------------

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ChoiceCitySerializers(serializers.ModelSerializer):
    class Meta:
        model = ChoiceCity
        fields = ['id', 'image_country', 'country', 'city']

class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'hotel_address', 'hotel_description'] # 'hotel_stars'

class ApartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'

class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'review_author', 'hotel', 'review_text', 'rating_stars', 'created_date']

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user_reservation', 'hotel_reservation', 'apartment_reservation', 'check_in_date', 'check_out_date']

# class CountrySerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Country
#         fields = '__all__'

# class CitySerializers(serializers.ModelSerializer):
#     class Meta:
#         model = City
#         fields = '__all__'

# class HotelImagesSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = HotelImages
#         fields = '__all__'

# class ApartmentImagesSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = ApartmentImages
#         fields = '__all__'