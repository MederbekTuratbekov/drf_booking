from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    user_image = models.ImageField()
    user_age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)])
    user_phone_number = PhoneNumberField(unique=True)
    account_created_date = models.DateField(auto_now_add=True)
    user_country = models.CharField(max_length=100)
    STATUS_CHOICES = (
        ('owner', 'owner'),
        ('guest', 'guest'),
    )
    guest_status = models.CharField(choices=STATUS_CHOICES, default='guest')

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'

class Country(models.Model):
    country_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.country_name

class City(models.Model):
    city_name = models.CharField(max_length=50, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city_name}, {self.country}'

class ChoiceCity(models.Model):
    image_country = models.FileField(upload_to='country_images/')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.country} - {self.city}'

class Hotel(models.Model):
    choice_city = models.ForeignKey(ChoiceCity, on_delete=models.CASCADE)
    hotel_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=100)
    hotel_address = models.CharField(max_length=100, unique=True)
    hotel_description = models.TextField(max_length=200)
    hotel_price = models.DecimalField(max_digits=7, decimal_places=2)
    hotel_stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return self.hotel_name

class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.hotel_image}'

class Apartment(models.Model):
    APARTMENT_STATUS = (
        ('available', 'available'), # свободный
        ('reserved', 'reserved'), # забронирован
        ('occupied', 'occupied'), # занят
    )
    APARTMENT_TYPE = (
        ('studio', 'studio'),  # Открытое пространство без перегородок
        ('one_bedroom', 'one_bedroom'),  # Отдельная спальня плюс кухня
        ('two_bedroom', 'two_bedroom'),  # Жилье с двумя отдельными комнатами
        ('luxury', 'luxury'),  # Улучшенная планировка и высокий уровень комфорта
        ('penthouse', 'penthouse'),  # На верхнем этаже, часто с террасой
        ('loft', 'loft'),  # Высокие потолки, большие окна, индустриальный стиль
        ('serviced', 'serviced'),  # Полностью оснащенные, с возможностью аренды
        ('duplex', 'duplex'),  # Двухуровневые апартаменты с лестницей внутри
        ('townhouse', 'townhouse'),  # Жилье с отдельным входом, как небольшой дом
        ('residence', 'residence')  # Элитные апартаменты с гостиничным сервисом
    )
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    apartment_owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=100)
    hotel_address = models.CharField(max_length=100, unique=True)
    apartment_number = models.PositiveSmallIntegerField(max_length=3)
    apartment_type = models.CharField(choices=APARTMENT_TYPE)
    video_file = models.FileField(upload_to='apartment_videos/', null=True, blank=True)
    apartment_description = models.TextField(max_length=500)
    is_free = models.CharField(choices=APARTMENT_STATUS, default='available')
    all_service = models.BooleanField(default=True) # привилегии
    apartment_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.hotel_name

class ApartmentImages(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    apartment_image = models.ImageField(upload_to='apartment_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.apartment}'

class Reviews(models.Model):
    review_author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=200)
    rating_stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.hotel} - {self.rating_stars}'

class Booking(models.Model):
    user_reservation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel_reservation = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    apartment_reservation = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
