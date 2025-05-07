from django.contrib import admin
from .models import UserProfile, Country, City, ChoiceCity, Hotel, HotelImages, Apartment, ApartmentImages, Reviews, Booking
from modeltranslation.admin import TranslationAdmin


class HotelImageInline(admin.TabularInline):
    model = HotelImages
    extra = 1

@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    inlines = [HotelImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImages
    extra = 5

@admin.register(Apartment)
class ApartmentAdmin(TranslationAdmin):
    inlines = [ApartmentImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Reviews)
class OtherAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(ChoiceCity)
admin.site.register(Booking)
