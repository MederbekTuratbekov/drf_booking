from rest_framework import serializers
from .models import UserProfile, Country, City, ChoiceCity, Hotel, HotelImages, Apartment, ApartmentImages, Reviews, Booking


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

