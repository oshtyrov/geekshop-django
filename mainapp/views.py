from django.shortcuts import render

# Create your views here.
# контроллер = функция
# MVC - Model Viev Controller
# Jango - MVT = Model Viev Template
# вьюха = контроллер = функция

def index(request):
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/products.html')