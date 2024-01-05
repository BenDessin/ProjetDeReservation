from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import CreateView, ListView
from .models import Reservation, Cadre
from .form import ReserveForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from profil.models import ProfilUser

    
@login_required
def CreeReservation(request):
    if request.method == "POST":
        form=ReserveForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            reservation = form.save(commit=False)
            id = request.user.pk
            author = ProfilUser.objects.get(pk=id)
            reservation.auth = author
            message = 'https://wa.me/+22607433029?text={} {} {}'.format(reservation.nom,reservation.format,str(reservation.date_remise))
            reservation.save()
            return HttpResponseRedirect(message)
    else:
        form = ReserveForm
    return render(request, "Reservations/creer.html", {"form":form})


class ReservationsListes(ListView):
    model = Reservation
    template_name = "Reservations/liste.html"
    context_object_name = "listes"
    

#créer les vues pour les cardres
class ListeCarde(ListView):
    model = Cadre
    template_name = "galerie/galerie.html"
    context_object_name = "cardre"

@login_required
def Panier(request,pk):
    user = ProfilUser.objects.get(pk=pk)
    panier = user.reservation_set.all()
    context = {'panier':panier}
    return render(request,'Reservations/panier.html' ,context)
