from django import forms
from .models import Reservation, Cadre

class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ("nom", "numero", "residence", "image", "format", "cathegorie", "event","date_remise")
        labels = {"nom":"Nom&Prenom", "numero":"Whatsapp", "residence":"Résidence", "cathegorie":"Type", "image":"Image", "format":"Format", "event":"Evènement","date_remise":"Date de remise"}
        widgets = {"date_remise":forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
                   "nom":forms.TextInput(attrs={'class':'form-control'}),
                   "numero":forms.TextInput(attrs={'class':'form-control'}),
                   "residence":forms.TextInput(attrs={'class':'form-control'}),
                   "cathegorie":forms.Select(attrs={'class':'form-select'}),
                   "format":forms.Select(attrs={'class':'form-select'}),
                   "event":forms.TextInput(attrs={'class':'form-control'}),
                   'image':forms.FileInput(attrs={'class':'form-control'}),
                   }
        
# years=range(2000,2080), 