from django.contrib import admin
from django.urls import path, include

from hotel.api import api

from hotel.routers import router

urlpatterns = [
    path('', include('hotel.urls')),
    path('admin/', admin.site.urls),
    path('django-api-routers/', include(router.urls)),
    path('django-api/', include('hotel.routers')),
    path('ninja-api/', api.urls),
    # path('api-auth/', include('rest_framework.urls')),
]
