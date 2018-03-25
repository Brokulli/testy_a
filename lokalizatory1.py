# -*- coding: utf-8 -*
# !/usr/bin/python

# importowanie niezbednych bibliotek

from selenium import webdriver
from time import sleep
import unittest # unittest zawiera klase TestCase wbudowana w pythona

# tworzymy nowa klase WsbPlCheck
# dziedziczaca po klasie TestCase z modulu unittest

class WsbPlCheck(unittest.TestCase): # wykorzystywanie modulu TestCase z Unittest
    # instrukcje ktore zostana wykonane przed kazdym testem
    def setUp(self):
        self.driver = webdriver.Chrome() # otwieranie przegladarki
        driver = self.driver
        driver.maximize_window() # maksymalizuj okno
        driver.get("http://www.wsb.pl/chorzow") # wchodzimy na strone wsb

    # testy
    def test_find_element_by_tag_name(self): #nazwa testu musi zaczynac sie od "test"
        driver = self.driver # musimy znow zdefiniowac
        driver.find_element_by_tag_name("body") # wyszukujemy element

    def test_link(self):
        driver = self.driver # musimy znow zdefiniowac
        link = self.driver.find_element_by_link_text("AKCEPTUJĘ")
        # wyszukujemy element po tekscie linku
        link.click()
        sleep(3) # usypia na chwile, czeka nim przejdzie dalej
        # jak zaimportowano sleep z modulu time (from time import sleep)
        # jesli zaimportowano modul time jako calosc (import time)
        # aby uzyc sleep nalezy napisac time.sleep()
        self.driver.find_element_by_link_text("Studia podyplomowe").click()
        # wyszukuje element po tekscie i klika w link
        sleep(3)

    # instrukcje, ktore beda wykonane po kazdym tescie
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__": #sprawdza czy pierwszy plik to plik main
    unittest.main(verbosity = 2) # gadatliwosc = 2
