from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_city_input, name='get_city_input'),
    path('weather/<str:city_name>/', views.get_weather_by_city, name='get_weather_by_city'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
