from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users import urls



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('users/', include('users.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
