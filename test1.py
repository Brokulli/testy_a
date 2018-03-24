# -*- coding: utf-8 -*
# !/usr/bin/python

# importowanie niezbednych bibliotek

from selenium import webdriver
import unittest # unittest zawiera klase TestCase wbudowana w pythona

# tworzymy nowa klase WsbPlCheck
# dziedziczaca po klasie TestCase z modulu unittest

class WsbPlCheck(unittest.TestCase): # wykorzystywanie modulu TestCase z Unittest
    # instrukcje ktore zostana wykonane przed kazdym testem
    def setUp(self):
        self.driver = webdriver.Chrome() # otwieranie przegladarki

    # testy
    # tutaj: testy strony wsb
    def test_wsb_pl_1(self):
        driver = self.driver
        driver.get("http://www.wsb.pl") # wchodzimy na strone wsb
        self.assertIn(u"Wyższe Szkoły Bankowe", driver.title) # sprawdza czy cos jest w czyms
        # tutaj czy "Wyższe Szkoły Bankowe" jest w tytule strony

    def test_wsb_pl_2(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        self.assertIn(u"Uczelnie Wyższe", driver.title)

    def test_wsb_pl_3(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        self.assertIn("Panda", driver.title)

    def test_wsb_pl_4(self):
        driver = self.driver
        driver.get("http://www.wsb.pl")
        self.assertIn("Studia", driver.title)

    # bedzie wykonane po kazdym tescie
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__": #sprawdza czy pierwszy plik to plik main
    unittest.main(verbosity = 2) # nie trzeba pisac "pyhton -m unittest NazwaPliku"
    # wystarczy "python NazwaPliku.py"
    # verbosity = gadatliwosc (im wyzsza cyfra tym unittest wiecej mowi,
    # 0 to najnizsza, a 2 to najwyszsza wartosc)
