from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .form import GetMyCarsForm
from .models import GetMyCars,Marka,Model,Gear
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.

def markAdd(request):
    marks=Marka.objects.all()
    if request.method == "POST":
        marka=request.POST.get("marka")
        newMarka=Marka(markaName=marka)
        newMarka.save()
        messages.success(request,"Marka Eklendi")
        return render(request,"dashboard.html")
    return render(request, "addMarka.html",{"marks":marks})

def modAdd(request):
    mods=Model.objects.all()
    if request.method == "POST":
        mod=request.POST.get("mod")
        newModel=Model(modelName=mod)
        newModel.save()
        messages.success(request,"Model Eklendi")
        return render(request,"dashboard.html")
    return render(request, "addModel.html",{"mods":mods})




def index(request):

    gears=Gear.objects.all()
    marks=Marka.objects.all()
    mods = Model.objects.all()
    keyword=request.GET.get("keyword")
    lowprc = request.GET.get("lowprc")
    hprc = request.GET.get("hprc")
    gear=request.GET.get("gear")
    mark = request.GET.get("mark")
    mdl = request.GET.get("mdl")

    if keyword and lowprc and hprc and gear and mark:
        cars=GetMyCars.objects.filter(title__contains=keyword,price__range=(lowprc,hprc),gear__gearName=gear,marka__markaName=mark,model__modelName=mdl)
        return render(request, "index.html", {"cars": cars})


    cars=GetMyCars.objects.all()




    return render(request,"index.html",{"cars":cars,"gears":gears,"marks":marks,"mods":mods})

def addcar(request):
    form=GetMyCarsForm(request.POST or None ,request.FILES or None)
    if form.is_valid():
        car=form.save(commit=False)
        car.owner=request.user
        car.save()
        messages.success(request,"Araç Eklendi..")
        return redirect("index")
    else:
        messages.error(request, "Araç Eklenemeddi..")
    return render(request,"addcar.html",{"form":form})

def dashboard(request):
    cars=GetMyCars.objects.filter(owner=request.user).order_by("-add_date")

    return render(request,"dashboard.html",{"cars":cars})

def updatecar(request,id):
    car=get_object_or_404(GetMyCars,id=id)
    form = GetMyCarsForm(request.POST or None, request.FILES or None,instance=car)
    if form.is_valid():
        car = form.save(commit=False)
        car.owner = request.user
        car.save()
        messages.success(request, "Araç Eklendi..")
        return redirect("getmycar:dashboard")
    messages.error(request, "Araç güncellendi..")
    return render(request, "updatecar.html", {"form": form})

def deletecar(request,id):
    car=get_object_or_404(GetMyCars,id=id)
    car.delete()
    messages.success(request, "Araç Eklendi..")
    return redirect("getmycar:dashboard")


def detail(request,id):
    car = get_object_or_404(GetMyCars,id=id)
    return render(request,"detail.html",{"car":car})



def deneme(request):
    return render(request,"deneme.html")

