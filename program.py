import moj_modul # importowanie naszego modulu, szuka modulu w tym samym katalogu

# program.py bedzie sie odwolywal do moj_modul.py
# po uruchomieniu program.py parametr __name__ to moj_modul

print(moj_modul.zmienna)
moj_modul.wypisz() # odwolujemy sie do wypisz zdefinowanego w moj_modul.py
moj_modul.wypisz("Hello world")
