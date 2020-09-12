from django.contrib import admin
from .models import GetMyCars,Marka,Model,Gear


admin.site.register(Marka)
admin.site.register(Model)
admin.site.register(Gear)
@admin.register(GetMyCars)
class GetMyCarsAdmin(admin.ModelAdmin):
    list_display = ["owner", "title", "add_date","model", "marka","km","gear","carYear"]

    class Meta:
        model = GetMyCars

