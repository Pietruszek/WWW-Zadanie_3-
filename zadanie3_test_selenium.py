from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
from django.test import TestCase, LiveServerTestCase
from airplanes_app.models import Lot, Pasazer
import time

selenium = webdriver.Chrome()
selenium2 = webdriver.Chrome()
selenium.get("http://127.0.0.1:8000")
selenium2.get("http://127.0.0.1:8000")
time.sleep(1)
login = selenium.find_element_by_name("login")
login2 = selenium2.find_element_by_name("login")
login.send_keys("fajny_login")
login2.send_keys("fajny_login")
haslo = selenium.find_element_by_name("haslo")
haslo2 = selenium2.find_element_by_name("haslo")
haslo.send_keys("fajne_haslo")
haslo2.send_keys("fajne_haslo")
haslo.submit()
haslo2.submit()
time.sleep(1)
przycisk = selenium.find_element_by_xpath("//input[@value='Załogi']")
przycisk2 = selenium2.find_element_by_xpath("//input[@value='Załogi']")
przycisk.click()
przycisk2.click()
time.sleep(1)
data_lotu = selenium.find_element_by_xpath("//input[@name='data_lotu']")
data_lotu2 = selenium2.find_element_by_xpath("//input[@name='data_lotu']")
data_lotu.send_keys("01.07.2018")
data_lotu2.send_keys("01.07.2018")
szukaj = selenium.find_element_by_xpath("//input[@value='Szukaj']")
szukaj2 = selenium2.find_element_by_xpath("//input[@value='Szukaj']")
szukaj.click()
szukaj2.click()
time.sleep(1)
select = Select(selenium.find_element_by_name('select_0'))
select2 = Select(selenium2.find_element_by_name('select_1'))
select.select_by_index(1)
select2.select_by_index(1)
time.sleep(1)
try:
    selenium2.switch_to_alert().accept()
    selenium.close()
    selenium2.close()
    print("Test zaliczony")
except NoAlertPresentException:
    print("Błąd: dane nie zostały poprawnie dodane do bazy danych")

