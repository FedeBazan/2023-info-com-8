from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('''<h1>Hola mundo desde Django</h1>
    <a link"">''')

def despedida(request):
    return HttpResponse('<h1>Despedida desde Django</h1>')

def contacto(request):
    return HttpResponse('''<h1>CONTACTO</h1>
    <ul>
        <li>Name: Julio Pablo Federico</li>
        <li>Surname:Bazan</li>
        <li>Cell:1233123</li>
        <li>contact: cell phone aosojkdaklsjdnalsnjd</li>
        <li>y otras cosas...</li>
    </ul>
    
    ''')