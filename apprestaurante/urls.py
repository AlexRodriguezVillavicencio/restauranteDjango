from django.urls import path
from . import views

app_name= 'apprestaurante'

urlpatterns = [
    path('',views.inicio, name="inicio"),
    path('<slug>/',views.categoria, name="categoria"),
    path('/<slug>/',views.producto, name="producto"),

]

