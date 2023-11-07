from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from .models import Vehicle
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.searchApp, name="searches"),
    path('infocar/<int:vehicle_id>', views.infocar, name='infocar'),
    path('infocarTime/<int:vehicle_id>/<str:array1>/<str:array2>/', views.infocarTimes, name='infocarTime'),
    path('rentCar/<int:vehicle_id>', views.rentCar, name='rentCar'),
    path('rentCarTime/<int:vehicle_id>/<str:array1>/<str:array2>/', views.rentCarTime, name='rentCarTime'),
    path("singin/", views.signin, name="singin"),
    path("singup/", views.signup, name="singup"),
    path("singout/", views.singout, name="singout"),
    path("rentNow/", views.rentNow, name="rentNow"),
    path("thanks/<int:vehicle_id>/<str:array1>/<str:array2>/>", views.rentFinal, name="thanksForRent"),
    path("contacto/", views.contacto, name= "contacto"),
    path("reservar/", views.reservar, name = "reservar")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
