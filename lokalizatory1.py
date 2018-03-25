# -*- coding: utf-8 -*
# !/usr/bin/python

# importowanie niezbednych bibliotek

from selenium import webdriver
from time import sleep # import usypiania
import unittest # unittest zawiera klase TestCase wbudowana w pythona
from selenium.webdriver.common.keys import Keys # obsluga klawiszy specjalnych

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
        # piszemy sleep() jesli zaimportowano sleep z modulu time (from time import sleep)
        # jesli zaimportowano modul time jako calosc (import time)
        # aby uzyc sleep nalezy napisac time.sleep()
        self.driver.find_element_by_link_text("Studia podyplomowe").click()
        # wyszukuje element po tekscie i klika w link
        sleep(3)
        self.driver.find_element_by_partial_link_text("podyplom")
        # wyszukuje element po fragmencie tekstu

    def test_search_box(self): # testy pola do wyszukiwania
        driver = self.driver
        szukajka = driver.find_element_by_id("edit-search-block-form--2") # szukanie po id
        # tutaj szukanie pola do wyszukiwania
        szukajka.send_keys("testowanie") # symuluje wpisywanie tekstu
        sleep(3)

        wyszukiwanie = driver.find_element_by_id("edit-submit")
        # szukanie przycisku do wyszukiwania po id
        wyszukiwanie.click() # klikanie w wyszukany przycisk
        sleep(5)

        szukacz = driver.find_element_by_id("edit-search-block-form--2") # szukanie po id
        szukacz.send_keys("programista") # symuluje wpisywanie tekstu
        szukacz.send_keys(Keys.RETURN) # symuluje wcisniecie enter
        driver.implicitly_wait(10) # inny sposob czekania aktywnego
        # w trakcie wyszukiwania sprawdza czy moze isc dalej

        results = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/ol/li[4]/div/p')
        # wyszukiwanie za pomoca xpath
        print("znaleziono "+str(len(results)) + " wynikow:\n")
        for result in results:
            print (result.text + "\n")
        sleep(5)

        self.assertEqual(3, len(results))
        # assert 3 == len(results)

    # instrukcje, ktore beda wykonane po kazdym tescie
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__": #sprawdza czy pierwszy plik to plik main
    unittest.main(verbosity = 2) # gadatliwosc = 2
