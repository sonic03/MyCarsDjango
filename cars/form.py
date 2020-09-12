from django import forms

from .models import GetMyCars,Marka,Model,Gear


marks=Marka.objects.all().values_list("markaName","markaName")
mark_list=[]
for mark in marks:
    mark_list.append(mark)

gear=Gear.objects.all().values_list("gearName","gearName")
gear_list=[]
for g in gear:
    gear_list.append(g)

mods=Model.objects.all().values_list("modelName","modelName")
model_list=[]
for mod in mods:
    model_list.append(mod)


class GetMyCarsForm(forms.ModelForm):

    class Meta:
        model=GetMyCars
        fields = ["title", "content", "marka","model","carYear","gear","km","price", "car_img1","car_img2","car_img3","car_img4"]

        widgets = {
            'marka':forms.Select(choices=mark_list),
            'model': forms.Select(choices=model_list),
            'gear': forms.Select(choices=gear_list),

        }