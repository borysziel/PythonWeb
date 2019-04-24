import os
import json
from sqlalchemy_create_engine import Session

carInfo = {}
def load_json():
    with open('offers_data.json','r') as output_files:
        _data = json.load(output_files)

    return _data

if __name__ == '__main__':
    from offer_models import Kampanie, Portale,Oferty

    session = Session()

    allegro = Portale(nazwa_portalu='allegro')
    session.add(allegro)

    # bardzo ważny fragment kodu
    session.commit()

    kompania1 = Kampanie(data='2018.11.31',rodzaj_api='allegro')
    session.add(kompania1)
    # bardzo ważny fragment kodu
    session.commit()
    tab = []
    #for line in open('offer.json','r'):
     #   _data = json.load(str(line))
    with open('offers_data.json','r') as output_files:
        _data = json.load(output_files)

    for element in _data:
        print(element)
        obiekt = Oferty(id_kampanii=1,id_oferty=element['OfferId'],id_sprzedajacego=element['Login'],\
                        lokalizacja=element['Location'],tytul=element['Tytul'],cena = element['Cena'],marka=element['Marka'],\
                        model=element['Model'],rok_produkcji=element['Rok produkcji'],przebieg=element['Przebieg'] ,pojemnosc = element['Pojemność silnika'],\
                        moc=element['Moc'],rodzaj_paliwa=element['Rodzaj paliwa'],kolor=element['Kolor'],uszkodzony=element['Uszkodzony'],kraj=element['Kraj pochodzenia'],\
                        naped=element['Napęd'],liczba_miejsc=element['Liczba miejsc'])
        session.add(obiekt)
    # bardzo ważny fragment kodu
        session.commit()


