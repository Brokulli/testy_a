# -*- coding: utf-8 -*

# importowanie niezbednych bibliotek

from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.common.keys import Keys

valid_name = "Name"
valid_second_name = "Second-name"
valid_tel = "000111000"
invalid_email = "email"
valid_password = "asnhj125"
valid_country = "Poland"

# tworzymy nowa klase WsbPlCheck
# dziedziczaca po klasie TestCase z modulu unittest

class WizzairRegistration(unittest.TestCase):
    # instrukcje ktore zostana wykonane przed kazdym testem
    def setUp(self):
        self.driver = webdriver.Chrome() # otwieranie przegladarki
        driver = self.driver
        driver.maximize_window() # maksymalizuj okno
        driver.get('https://wizzair.com/pl-pl#/') # wchodzimy na strone wizzair

    # testy
    def test_registration_invalid_email(self):
        driver = self.driver
        sign_in = driver.find_element_by_xpath('//*[@id="app"]/header/div[1]/div/nav/ul/li[7]/button')
        # znajdujemy przycisk 'zaloguj sie' za pomoca xpath
        sign_in.click() # klikamy w przycisk 'zaloguj sie'
        #driver.implicitly_wait(10)

        register = driver.find_element_by_css_selector('#login-modal > form > div > p > button')
        register.click()

        name = driver.find_element_by_xpath("//input[@placeholder='Imię']")
        name.send_keys(valid_name) # symuluje wpisywanie tekstu

        second_name= driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
        second_name.send_keys(valid_second_name) # symuluje wpisywanie tekstu

        gender = driver.find_element_by_xpath("//label[@for='register-gender-female']")
        # wyszukujemy element po tekscie linku
        gender.click()

        #   wersja w java script

        #   gender_switch = driver.find_element_by_xpath("//label[@for='register-gender-female']")
        #   driver.execute_script("arguments[0].click()", gender_switch)
        #   gender_switch.click()

        telefon = driver.find_element_by_xpath("//input[@type='tel']")
        telefon.send_keys(valid_tel)

        email = driver.find_element_by_xpath("//input[@data-test='booking-register-email']")
        email.send_keys(invalid_email)

        password = driver.find_element_by_xpath("//input[@data-test='booking-register-password']")
        password.send_keys(valid_password)

        country = driver.find_element_by_xpath("//input[@data-test='booking-register-country']")
        country.send_keys(valid_country)

        offers = driver.find_element_by_xpath("//label[@for='registration-special-offers-checkbox']")
        offers.click()

        policy = driver.find_element_by_xpath("//label[@for='registration-privacy-policy-checkbox']")
        policy.click()

        sleep(5)

    # instrukcje, ktore beda wykonane po kazdym tescie
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
