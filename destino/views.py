from django.shortcuts import render

def atracoes(request):
    return render(request, 'destino/atracoes.html')

def historia_cultura(request):
    return render(request, 'destino/historia_cultura.html')

def galeria(request):
    return render(request, 'destino/galeria.html')