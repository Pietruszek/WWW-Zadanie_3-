from django.contrib.auth import authenticate, login as login_auth, logout as logout_auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Pasazer, Lot

@login_required
def strona_glowna(request):
    lista_lotow = Lot.objects.order_by('czas_startu')
    context = {}
    if 'lotnisko_startowe' in request.POST and request.POST['lotnisko_startowe']:
        context.update({'lotnisko_startowe': request.POST['lotnisko_startowe']})
        lista_lotow = lista_lotow.filter(lotnisko_startowe=request.POST['lotnisko_startowe'])
    if 'lotnisko_docelowe' in request.POST and request.POST['lotnisko_docelowe']:
        context.update({'lotnisko_docelowe': request.POST['lotnisko_docelowe']})
        lista_lotow = lista_lotow.filter(lotnisko_docelowe=request.POST['lotnisko_docelowe'])
    if 'data_lotu' in request.POST and request.POST['data_lotu']:
        try:
            context.update({'data_lotu': request.POST['data_lotu']})
            lista_lotow = lista_lotow.filter(czas_startu__date=request.POST['data_lotu'])
        except ValidationError:
            context.update({'bledna_data': 1})
    context.update({'lista_lotow': lista_lotow[:100]})
    return render(request, 'airplanes_app/strona_glowna.html', context)

@login_required
def lot(request, lot_id):
    lot = Lot.objects.get(id=lot_id)
    context = {'lot_id': lot_id, 'lot': lot}
    liczba_wolnych_miejsc = lot.samolot.liczba_miejsc - lot.liczba_zajetych_miejsc
    wymagane_pola = 0
    if 'imie' in request.POST and request.POST['imie']:
        context.update({'imie': request.POST['imie']})
        wymagane_pola += 1
    if 'nazwisko' in request.POST and request.POST['nazwisko']:
        context.update({'nazwisko': request.POST['nazwisko']})
        wymagane_pola += 1
    if 'liczba_biletow' in request.POST and request.POST['liczba_biletow']:
        context.update({'liczba_biletow': request.POST['liczba_biletow']})
        wymagane_pola += 1
    if 0 < wymagane_pola and wymagane_pola < 3:
        context.update({'rejestracja': "niepowodzenie"})
    if wymagane_pola == 3:
        try:
            pasazer = Pasazer.objects.get(imie=request.POST['imie'], nazwisko=request.POST['nazwisko'])
        except ObjectDoesNotExist:
            pasazer = Pasazer.objects.create(imie=request.POST['imie'], nazwisko=request.POST['nazwisko'])
        if int(request.POST['liczba_biletow']) <= liczba_wolnych_miejsc:
            lot.liczba_zajetych_miejsc += int(request.POST['liczba_biletow'])
            lot.save()
            liczba_wolnych_miejsc = lot.samolot.liczba_miejsc - lot.liczba_zajetych_miejsc
            lot.pasazerowie.add(pasazer)
            context.update({'rejestracja': "powodzenie"})
        else:
            context.update({'rejestracja': "brak_biletow"})
    context.update({'liczba_wolnych_miejsc': liczba_wolnych_miejsc})
    return render(request, 'airplanes_app/lot.html', context)

def login(request):
    uzytkownik = None
    context = {}
    if ('login' in request.POST and request.POST['login']) or ('haslo' in request.POST and request.POST['haslo']):
        context = {'nieudane_logowanie': 1}
    if 'login' in request.POST and request.POST['login'] and 'haslo' in request.POST and request.POST['haslo']:
        uzytkownik = authenticate(request, username=request.POST['login'], password=request.POST['haslo'])
    if uzytkownik is not None:
        login_auth(request, uzytkownik)
        return redirect('strona_glowna')
    else:
        return render(request, 'airplanes_app/login.html', context)

def logout(request):
    logout_auth(request)
    return redirect('strona_glowna')
