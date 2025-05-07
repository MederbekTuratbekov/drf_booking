from .models import Hotel, Apartment, Reviews # UserProfile, Country, City, ChoiceCity, HotelImages, ApartmentImages, Booking
from modeltranslation.translator import TranslationOptions,register


@register(Hotel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('hotel_description',)

@register(Apartment)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('apartment_description',)

@register(Reviews)
class ProductTranslationOptions(TranslationOptions):
    fields = ('review_text',)
