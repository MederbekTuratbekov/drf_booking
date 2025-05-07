from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('accounts/', include('allauth.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
