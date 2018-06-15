from django.db import models

class Samolot(models.Model):
    znaki_rejestracyjne = models.CharField(max_length=20)
    liczba_miejsc = models.IntegerField(default=0)

class Pasazer(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)

class Zaloga(models.Model):
    imie_i_nazwisko_kapitana = models.CharField(max_length=200)

class Lot(models.Model):
    lotnisko_startowe = models.CharField(max_length=100)
    czas_startu = models.DateTimeField()
    lotnisko_docelowe = models.CharField(max_length=100)
    czas_ladowania = models.DateTimeField()
    samolot = models.ForeignKey(Samolot, on_delete=models.CASCADE)
    pasazerowie = models.ManyToManyField(Pasazer)
    liczba_zajetych_miejsc = models.IntegerField(default=0)
    zaloga = models.ForeignKey(Zaloga, null=True, on_delete=models.CASCADE)
