import django_filters
from .models import Country, City, ChoiceCity, Hotel, HotelImages, Apartment, ApartmentImages, Reviews, Booking


class ChoiceCityFilter(django_filters.FilterSet):
    city_name = django_filters.CharFilter(field_name='city__city_name', lookup_expr='exact')
    country = django_filters.ModelChoiceFilter(queryset=Country.objects.all())

    class Meta:
        model = ChoiceCity
        fields = ['country', 'city_name']

class HotelFilter(django_filters.FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'hotel_name': ['exact'],
            'hotel_address': ['exact'],
            'hotel_description': ['exact'],
        }

class ApartmentFilter(django_filters.FilterSet):
    apartment_price = django_filters.RangeFilter()
    class Meta:
        model = Apartment
        fields = {
            'apartment_type': ['exact'],
            'all_service': ['exact'],
            'apartment_price': ['gt', 'lt'],
        }
