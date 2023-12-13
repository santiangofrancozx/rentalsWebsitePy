from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from .models import Vehicle
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.searchApp, name="searches"),
    #path('infocar/<int:vehicle_id>', views.infocar, name='infocar'),
    path('infocarTime/<int:vehicle_id>/<str:array1>/<str:array2>/', views.infocarTimes, name='infocarTime'),
    #path('rentCar/<int:vehicle_id>', views.rentCar, name='rentCar'),
    path('rentCarTime/<int:vehicle_id>/<str:array1>/<str:array2>/', views.rentCarTime, name='rentCarTime'),
    path("singin/", views.signin, name="singin"),
    path("singup/", views.signup, name="singup"),
    path("singout/", views.singout, name="singout"),
    path("rentNow/", views.rentNow, name="rentNow"),
    path("thanks/<int:vehicle_id>/<str:array1>/<str:array2>/>", views.rentFinal, name="thanksForRent"),
    path("contacto/", views.contacto, name= "contacto"),
    path("editUserInfo/", views.editUserInfo, name= "editUserInfo"),
    path("reservas/", views.reservas, name = "reservas"),
    path("showUsers/",views.showUsers, name ="showUsers"),
    path("showComments/",views.showComments, name ="showComments"),
    path("showReservation/",views.showReservation, name ="showReservation"),
     path('eliminar_reserva/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
