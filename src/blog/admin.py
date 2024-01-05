from django.contrib import admin
from blog.models import Reservation, Cadre

# Register your models here.
# admin.site.register(Reservation)
admin.site.register(Cadre)

@admin.register(Reservation)
class Reservation(admin.ModelAdmin):
    list_display = (
        "nom","date","date_remise","format",
    )