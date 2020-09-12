from django.contrib import admin
from django.urls import path
from . import views

app_name="getmycar"

urlpatterns = [
    path('',views.index,name="index"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addcar/',views.addcar,name="addcar"),
    path('addMarka/',views.markAdd,name="addMarka"),
    path('addModel/',views.modAdd,name="addModel"),
    path('car/<int:id>' ,views.detail,name="detail"),
    path('car/update/<int:id>',views.updatecar,name="updatecar"),
    path('car/delete/<int:id>',views.deletecar,name="deletecar"),
    path('deneme/',views.deneme,name="deneme"),
]