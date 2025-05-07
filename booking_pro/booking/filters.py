import django_filters
from .models import Country, City, ChoiceCity, Hotel, HotelImages, Apartment, ApartmentImages, Reviews, Booking


class ApartmentFilter(django_filters.FilterSet):
    apartment_price = django_filters.RangeFilter()
    class Meta:
        model = Apartment
        fields = {
            'apartment_type':['exact'],
            'all_service':['exact'],
            'apartment_price':['gt', 'lt']
        }
