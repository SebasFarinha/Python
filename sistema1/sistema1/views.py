from django.http import HttpResponse
from django.shortcuts import *

def saludar(request):
    return HttpResponse("Hola pipol")

def get_google(request):
    url = "https:www.google.com"
    return redirect(url)




def get_fibonacci (request):
    lista_fibo=[1]
    x = 0
    fib =1
    for i in range (98):
        
        aux = fib
        fib = fib + x
        lista_fibo.append(f",{fib}, ")
        x = aux
    return HttpResponse(lista_fibo)

def get_pares(request):
    lista_pares=[]
    x=0
    for i in range(100):
        x+=2
        lista_pares.append(f"{x}, ")
    return HttpResponse(lista_pares)
def insertar_algo(request):
    h1= input("Inserte un texto aqui: ")
    return HttpResponse(h1)
        

