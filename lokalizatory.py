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
    def test_wsb_search_box_1(self):
        driver = self.driver
        driver.get("http://www.wsb.pl") # wchodzimy na strone wsb
        driver.find_element_by_id("edit-search-block-form--2")

    # bedzie wykonane po kazdym tescie
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__": #sprawdza czy pierwszy plik to plik main
    unittest.main(verbosity = 2)
