from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')

def despedida(request):
    return HttpResponse('Despedida desde Django')

def contacto(request):
    return HttpResponse('''<h1>CONTACTO</h1>
    <br>Name: Julio Pablo Federico
    <br>Surname:Bazan
    <br>Cell:1233123
    <br>contact: cell phone aosojkdaklsjdnalsnjd
    <br>y otras cosas... 
    ''')