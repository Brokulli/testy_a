# -*- coding: utf-8 -*
# !/usr/bin/python

# importowanie niezbednych bibliotek

from selenium import webdriver
import time

# tworzenie nowego sterownika do Chrome
driver = webdriver.Chrome()

# maksymalizuj okno
driver.maximize_window()
driver.get("http://www.wsb.pl")

# poczekaj 5 sekund
# to podobno ZLA metoda
time.sleep(5)

# zamknij sterownik
driver.quit()
