from .models import Hotel, Apartment, Reviews # UserProfile, Country, City, ChoiceCity, HotelImages, ApartmentImages, Booking
from modeltranslation.translator import TranslationOptions, register


@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_description',)

@register(Apartment)
class ApartmentTranslationOptions(TranslationOptions):
    fields = ('apartment_description',)

@register(Reviews)
class ReviewsTranslationOptions(TranslationOptions):
    fields = ('review_text',)
