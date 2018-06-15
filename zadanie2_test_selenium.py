from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import TestCase, LiveServerTestCase
from airplanes_app.models import Lot, Pasazer
import time

str_imie = "Piotr"
str_nazwisko = "Olczak"
str_liczba_biletow = "5"

selenium = webdriver.Chrome()
selenium.get("http://127.0.0.1:8000")
time.sleep(1)
login = selenium.find_element_by_name("login")
login.send_keys("fajny_login")
haslo = selenium.find_element_by_name("haslo")
haslo.send_keys("fajne_haslo")
haslo.submit()
time.sleep(1)
data_lotu = selenium.find_element_by_xpath("//input[@name='data_lotu']")
data_lotu.send_keys("01.07.2018")
szukaj = selenium.find_element_by_xpath("//input[@value='Szukaj']")
szukaj.click()
time.sleep(1)
szczegoly_lotu = selenium.find_element_by_link_text("Zobacz szczegóły")
url = szczegoly_lotu.get_attribute("href")
lot_id = url.split('/')[4]
lot = Lot.objects.get(pk=lot_id)
liczba_zajetych_miejsc = lot.liczba_zajetych_miejsc
szczegoly_lotu.click()
time.sleep(1)
imie = selenium.find_element_by_xpath("//input[@name='imie']")
imie.send_keys(str_imie)
nazwisko = selenium.find_element_by_xpath("//input[@name='nazwisko']")
nazwisko.send_keys(str_nazwisko)
int_liczba_biletow = selenium.find_element_by_xpath("//input[@name='liczba_biletow']")
int_liczba_biletow.send_keys(str_liczba_biletow)
zarezerwuj = selenium.find_element_by_xpath("//input[@value='Zarezerwuj bilety']")
zarezerwuj.click()
selenium.close()
time.sleep(1)
lot = Lot.objects.get(pk=lot_id)
nowa_liczba_zajetych_miejsc = lot.liczba_zajetych_miejsc
if Pasazer.objects.all().filter(imie=str_imie, nazwisko=str_nazwisko).exists() and nowa_liczba_zajetych_miejsc - liczba_zajetych_miejsc == int(str_liczba_biletow):
    print("Test zaliczony")
else:
    print("Błąd: dane nie zostały poprawnie dodane do bazy danych")

