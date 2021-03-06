import os
from bs4 import BeautifulSoup


def load_offer(_offer):
    file_name = os.path.join('data', _offer)
    with open(file_name, encoding='utf-8') as _file_in:
        _data = _file_in.read()

    return _data


def get_details(_data):
    soup = BeautifulSoup(_data, 'html.parser')

    # szukamy kontenera posiadającego wskazany atrybut
    filtered = soup.find_all(attrs={"data-box-name": "Parameters"})

    labels = ("Faktura", "Informacje dodatkowe", "Pojemność silnika", "Moc", "Kolor")

    for element in filtered:
        for label in labels:
            # szukamy elementu z etykietką
            anchor = element.find("div", text=label + ":")
            # wyświetlamy kolejny element (rodzeństwo)
            print(label, ':', anchor.find_next_sibling("div").text)

    # szukamy elementu z atrybutem itemprop="price"
    filtered = soup.find(itemprop="price")
    print(filtered.get('content'))
    filtered = soup.find(itemprop="priceCurrency")
    print(filtered.get('content'))

    # szukamy loginu sprzedawcy
    filtered = soup.find(attrs={"data-analytics-click-value": "sellerLogin"})
    print(filtered.next)
    # FIXME: allegro wprowadziło nowy układ HTML na stronie, konieczna zmiana na "locationShow"
    filtered = soup.find(attrs={"data-analytics-interaction-value": "LocationShow"})
    print(filtered.next)

    print(soup.title.string)

    return ''


offers = (
    'offer_7192730975_mk3.html',
    'offer_7350326221_mk3.html'
)

for offer in offers:
    data = load_offer(offer)
    get_details(data)
    print('-' * 40)
    break
