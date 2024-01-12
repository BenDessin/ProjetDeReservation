from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView
from .models import Reservation, Cadre, Cathegorie
from .form import ReserveForm
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from profil.models import ProfilUser



def CreeReservation(request):
    context = {}
    if request.method == "POST":
        form=ReserveForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            reservation = form.save(commit=False)
            id = request.user.pk
            author = ProfilUser.objects.get(pk=id)
            reservation.auth = author
            # A modifier
            message = 'https://wa.me/+22607433029?text={} {} {}'.format(reservation.nom,reservation.format,str(reservation.date_remise))
            reservation.save()
            return HttpResponseRedirect(message)
    else:
        form = ReserveForm
        context ["form"] = form
    #reccuperer la liste des cathegories
    cathegorie = Cathegorie.objects.all()
    context["cathegorie"] = cathegorie
    return render(request, "galerie/galerie.html", context)

#Ajout de fonction
@login_required
def Reservations(request, pk):
    context = {}
    if request.method == "POST":
        form=ReserveForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            reservation = form.save(commit=False)
            id = request.user.pk
            author = ProfilUser.objects.get(pk=id)
            reservation.auth = author
            # A modifier
            message = 'https://wa.me/+22607433029?text={} {} {}'.format(reservation.nom,reservation.format,str(reservation.date_remise))
            reservation.save()
            return HttpResponseRedirect(message)
    else:
        init = {}
        init["nom"] = request.user.nom +" "+ request.user.prenom
        init["numero"] = request.user.telephone
        if pk!=0:
            cadre = Cadre.objects.get(pk=pk)
            init["format"] = cadre.format
            init["cathegorie"] = cadre.cathegorie
        form = ReserveForm(initial=init)
        context ["form"] = form
        form = ReserveForm(initial=init)
        context ["form"] = form
    return render(request, "Reservations/creer.html", context)


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
def Panier(request):
    panier = request.user.reservation_set.all()
    context = {'panier':panier}
    return render(request,'Reservations/panier.html' ,context)
