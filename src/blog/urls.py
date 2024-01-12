from django.urls import path
from .views import CreeReservation, ReservationsListes, Panier, Reservations

app_name = 'blog'

urlpatterns = [
    path("reservation/liste", ReservationsListes.as_view(), name='liste'),
    path("", CreeReservation, name='reserve'),
    path("/cadeaux/<int:pk>/Reservation/portrait/", Reservations, name='reserver'),
    path("monpanier/", Panier, name='panier'),
]