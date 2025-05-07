from rest_framework import serializers
from .models import UserProfile, Country, City, ChoiceCity, Hotel, HotelImages, Apartment, ApartmentImages, Reviews, Booking


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ChoiceCitySerializers(serializers.ModelSerializer):
    class Meta:
        model = ChoiceCity
        fields = '__all__'


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class HotelImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelImages
        fields = '__all__'

class ApartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'

class ApartmentImagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImages
        fields = '__all__'

class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
