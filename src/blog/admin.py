from django.contrib import admin
from blog.models import Reservation, Cadre, Price,Cathegorie,Dimension

# Register your models here.
# admin.site.register(Reservation)
admin.site.register(Cadre)
admin.site.register(Price)
admin.site.register(Cathegorie)
admin.site.register(Dimension)

@admin.register(Reservation)
class Reservation(admin.ModelAdmin):
    list_display = (
        "nom","date","date_remise","format",
    )