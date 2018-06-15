import random
import locale
import string
import datetime
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError
from airplanes_app.models import Samolot, Pasazer, Zaloga, Lot

class Command(BaseCommand):
    help = 'Reverts the database to the initial state (only with example data)'

    def handle(self, *args, **options):
        Lot.objects.all().delete()
        Zaloga.objects.all().delete()
        Pasazer.objects.all().delete()
        Samolot.objects.all().delete()
        
        miasta = ["Warszawa", "Londyn", "Madryt", "Paryż", "Praga", "Moskwa",
                  "Wiedeń", "Ateny", "Wilno", "Berlin", "Oslo", "Rzym"]
        
        for i in range(50):
            znaki_rejestracyjne = "".join([random.choice(string.ascii_uppercase + string.digits) for i in range(10)])
            liczba_miejsc = random.randint(20, 200)
            samolot = Samolot.objects.create(znaki_rejestracyjne=znaki_rejestracyjne, liczba_miejsc=liczba_miejsc)
            
            lotnisko_docelowe = random.choice(miasta)
            czas_ladowania = timezone.now() + datetime.timedelta(hours=random.randint(0, 23),
                                                                 minutes=random.randint(0, 59))
            for j in range(50):
                lotnisko_startowe = lotnisko_docelowe
                czas_startu = czas_ladowania + datetime.timedelta(hours=random.randint(4, 30),
                                                                  minutes=random.randint(0, 59))
                lotnisko_docelowe = random.choice([miasto for miasto in miasta if miasto not in lotnisko_startowe])
                czas_ladowania = czas_startu + datetime.timedelta(hours=random.randint(2, 5),
                                                                  minutes=random.randint(0, 59))
                Lot.objects.create(lotnisko_startowe=lotnisko_startowe,
                                   czas_startu=czas_startu,
                                   lotnisko_docelowe=lotnisko_docelowe,
                                   czas_ladowania=czas_ladowania,
                                   samolot=samolot,
                                   zaloga=None)
        
        imiona = ["Piotr", "Paweł", "Krzysztof", "Michał", "Jakub", "Adam",
                  "Bartłomiej", "Patryk", "Mariusz", "Kacper", "Jan", "Antoni",
                  "Szymon", "Mateusz", "Tomasz", "Karol", "Marek", "Robert",
                  "Krystian", "Daniel", "Damian", "Łukasz", "Kamil", "Dionizy",
                  "Rafał", "Aleksander", "Maciej", "Wojciech", "Dariusz"]
        nazwiska = ["Nowak", "Kowalski", "Wiśniewski", "Wójcik", "Kowalczyk",
                    "Kamiński", "Lewandowski", "Dąbrowski", "Zieliński",
                    "Szymański", "Woźniak", "Kozłowski", "Jankowski", "Mazur",
                    "Wojciechowski", "Kwiatkowski", "Krawczyk", "Grabowski",
                    "Zając", "Pawłowski", "Król", "Wieczorek", "Jabłoński",
                    "Wróbel", "Nowakowski", "Majewski", "Olszewski", "Stępień",
                    "Malinowski", "Jaworski", "Adamczyk", "Dudek", "Nowicki",
                    "Pawlak", "Górski", "Witkowski", "Walczak", "Sikora",
                    "Baran", "Rutkowski", "Michalak", "Szewczyk", "Ostrowski",
                    "Tomaszewski", "Pietrzak", "Zalewski", "Wróblewski",
                    "Marciniak", "Jasiński", "Zawadzki", "Bąk", "Jakubowski",
                    "Sadowski", "Duda", "Włodarczyk", "Wilk", "Chmielewski",
                    "Borkowski", "Sokołowski", "Szczepañski", "Sawicki",
                    "Kucharski", "Lis", "Maciejewski", "Kubiak", "Kalinowski",
                    "Mazurek", "Wysocki", "Kołodziej", "Kaźmierczak",
                    "Czarnecki", "Sobczak", "Konieczny", "Urbański", "Głowacki",
                    "Wasilewski", "Sikorski"]

        
        while Zaloga.objects.all().count() < 30:
            imie = random.choice(imiona)
            nazwisko = random.choice(nazwiska)
            kapitan = imie + " " + nazwisko
            if not Zaloga.objects.filter(imie_i_nazwisko_kapitana=kapitan).exists():
                Zaloga.objects.create(imie_i_nazwisko_kapitana=kapitan)
        
        print("Finished!")
