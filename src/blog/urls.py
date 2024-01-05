from django.urls import path
from .views import ListeCarde, CreeReservation, ReservationsListes, Panier

app_name = 'blog'

urlpatterns = [
    path("reservation/liste", ReservationsListes.as_view(), name='liste'),
    path("reserver/", CreeReservation, name='reserve'),
    path("", ListeCarde.as_view(), name='home'),
    path("monpanier/<int:pk>/",Panier,name='panier'),
]