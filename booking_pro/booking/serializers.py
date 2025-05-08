from rest_framework import serializers
from .models import UserProfile, Country, City, ChoiceCity, Hotel, HotelImages, Apartment, ApartmentImages, Reviews, Booking
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'user_age', 'user_phone_number', 'guest_status', 'account_created_date')
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
        fields = ('id', 'image_country', 'country', 'city')

# class ReviewsSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Reviews
#         fields = ('id', 'review_author', 'hotel', 'review_text', 'rating_stars', 'created_date')

class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('id', 'review_author', 'hotel', 'review_text', 'rating_stars', 'created_date')

    def validate(self, data):
        request = self.context.get('request')
        user = request.user
        hotel = data.get('hotel')

        if hotel and hotel.hotel_owner == user:
            raise serializers.ValidationError("Владельцы отелей не могут оставлять отзывы на свои отели.")
        if hotel and Reviews.objects.filter(review_author=user, hotel=hotel).exists():
            raise serializers.ValidationError("Вы уже оставили отзыв на этот отель.")
        return data

class ReviewsReadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('id', 'review_author', 'hotel', 'review_text', 'rating_stars', 'created_date')

class HotelImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelImages
        fields = ('hotel_image',)

class HotelSerializers(serializers.ModelSerializer):
    get_avg_rating = serializers.SerializerMethodField()
    get_count_review = serializers.SerializerMethodField()
    hotel_image = HotelImagesSerializers(source='images_connect_hotel', many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = ('id', 'hotel_name', 'hotel_address', 'hotel_description', 'get_avg_rating', 'get_count_review', 'hotel_image')

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_review(self, obj):
        return obj.get_count_review()

class ApartmentImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImages
        fields = ('apartment_image',)

class ApartmentSerializers(serializers.ModelSerializer):
    get_avg_rating = serializers.SerializerMethodField()
    get_count_review = serializers.SerializerMethodField()
    apartment_image = ApartmentImagesSerializers(source='images_connect_apartment', many=True, read_only=True)
    class Meta:
        model = Apartment
        fields = ('id', 'apartment_number', 'apartment_type', 'video_file', 'apartment_description', 'is_free', 'all_service',
                  'apartment_price', 'get_avg_rating', 'get_count_review', 'apartment_image')

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_review(self, obj):
        return obj.get_count_review()

# class BookingSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = ('id', 'user_reservation', 'hotel_reservation', 'apartment_reservation', 'check_in_date', 'check_out_date')

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'user_reservation', 'hotel_reservation', 'apartment_reservation', 'check_in_date', 'check_out_date')

    def validate(self, data):
        check_in_date = data.get('check_in_date')
        check_out_date = data.get('check_out_date')
        apartment = data.get('apartment_reservation')

        # Проверка, что дата заезда раньше даты выезда
        if check_in_date >= check_out_date:
            raise serializers.ValidationError("Дата заезда должна быть раньше даты выезда.")

        # Проверка статуса номера
        if apartment.is_free != 'available':
            raise serializers.ValidationError("Номер не доступен для бронирования.")

        # Проверка пересечения дат
        overlapping_bookings = Booking.objects.filter(
            apartment_reservation=apartment,
            check_in_date__lte=check_out_date,
            check_out_date__gte=check_in_date
        )

        if overlapping_bookings.exists():
            raise serializers.ValidationError("Даты бронирования пересекаются с существующими бронированиями.")

        return data

    def create(self, validated_data):
        # Создание бронирования и установка user_reservation
        booking = Booking.objects.create(
            user_reservation=self.context['request'].user,
            **validated_data
        )
        return booking

class ManageHotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'hotel_name', 'hotel_address', 'hotel_description', 'choice_city', 'hotel_owner')

class ManageApartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ('id', 'hotel_name', 'apartment_number', 'apartment_type', 'video_file', 'apartment_description', 'is_free', 'all_service', 'apartment_price')

# class CountrySerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Country
#         fields = '__all__'

# class CitySerializers(serializers.ModelSerializer):
#     class Meta:
#         model = City
#         fields = '__all__'
