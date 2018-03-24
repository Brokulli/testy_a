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

    # test
    # tutaj: test strony wsb
    def test_wsb_pl(self):
        driver = self.driver
        driver.get("http://www.wsb.pl") # wchodzimy na strone wsb
        self.assertIn(u"Wyższe Szkoły Bankowe", driver.title) # sprawdza czy cos jest w czyms
        # tutaj czy "Wyższe Szkoły Bankowe" jest w tytule strony

    # bedzie wykonane po kazdym tescie
    def tearDown(self):
        self.driver.quit()
