# TODO: zadania do wykonania podczas zajęć i w domu
# TODO: 0. rozpakuj archiwum do katalogu offers, tak aby w tym katalogu były tylko pliki html
# TODO: 1. sprawdź czy wszystkie pliki załadują się i przetworzą (tu wykorzystałem BS4, możesz użyć innego sposobu przetwarzania)
# TODO: 2. utwórz plik na przechowywanie danych (csv lub json - wybór należy do Ciebie)
# TODO: 3. wszystkie oferty zapisz w nowo utworzonym pliku

import os
from bs4 import BeautifulSoup


import json
# import csv

carInfo = {}
def load_offer(_offer):
    file_name = os.path.join('D:\\Python_kurs\\Course\\seventhLesson\\Day07\\small_big_data\\offers', _offer)
    with open(file_name, 'r', encoding="utf-8") as _file_in:
        _data = _file_in.read()

    return _data


def save_offer(dict):
    with open('offer.json','a') as output_files:
        json.dump(dict,output_files, indent=4)


def get_details(_data):
    soup = BeautifulSoup(_data, 'html.parser')
    filtered = soup.find_all(attrs={"data-box-name": "Parameters"})

    labels = ["Faktura", "Informacje dodatkowe",
              "Kierownica po prawej (Anglik)", "Kolor", "Kraj pochodzenia",
              "Lakier", "Liczba drzwi", "Liczba miejsc", "Moc", "Napęd",
              "Pojemność silnika", "Przebieg", "Rodzaj paliwa",
              "Rok produkcji", "Stan", "Uszkodzony", ]

    for element in filtered:
        for label in labels:
            anchor = element.find("div", text=label + ":")
            if anchor != None:
                # print(label, ':', anchor.find_next_sibling("div").text)
                carInfo[label] = anchor.find_next_sibling("div").text
    filtered = soup.find(itemprop="price")
    # print(filtered.get('content'))
    carInfo["Cena"] = filtered.get('content')

    filtered = soup.find(itemprop="priceCurrency")
    # print(filtered.get('content'))
    carInfo["Waluta"] = filtered.get('content')

    filtered = soup.find(attrs={"data-analytics-click-value": "sellerLogin"})

    for i in filtered:
        break
        # print(i, len(filtered), '--')
    carInfo["Login"] = i
    filtered = soup.find(attrs={'data-analytics-interaction-value': "LocationShow"})
    for i in filtered:
        break
        # print(i, '---', len(filtered), '+++')
    carInfo["Location"] = i
    return ''


offers = os.listdir('D:\\Python_kurs\\Course\\seventhLesson\\Day07\\small_big_data\\offers')
for offer in offers:
    # print(offer)
    carInfo["Offer"] = offer
    data = load_offer(offer)
    get_details(data)
    save_offer(carInfo)