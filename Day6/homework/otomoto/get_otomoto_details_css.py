import os
from parsel import Selector


def load_offer(_offer):
    file_name = os.path.join('data', _offer)
    with open(file_name, encoding='utf-8') as _file_in:
        _data = _file_in.read()

    return _data


def get_details(_data):
    selector = Selector(text=_data)

    # selector css object wskazujący na tytuł strony
    # zapisy alternatywne
    # print(selector.css('title::text'))
    # print(selector.css('head > title::text'))

    # by wydobyć tekst z HTML trzeba skorzystać z konstrukcji poniżej
    # zapisy alternatywne
    print(selector.css('title::text').get())
    print(selector.css('head > title::text').get())

    # TODO: dodaj kolejne etykietki

    # Uwaga! - Te selektory zostały wygenerowane przez Chrome. FF może zapisać inaczej

    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(2) > span::text').get(), ' ', end="")
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(2) > div > a::attr(title)').get())

    # TODO: dodaj wyszukiwanie waluty
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(6) > span::text').get(), ' ', end="")
    data = selector.css('#parameters > ul:nth-child(1) > li:nth-child(6) > span ~ div::text').get()
    print(data.strip())
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(7) > span::text').get(), ' ', end="")
    data = selector.css('#parameters > ul:nth-child(1) > li:nth-child(7) > span ~ div::text').get()
    print(data.strip())
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(8) > span::text').get(), ' ', end="")
    data = selector.css('#parameters > ul:nth-child(1) > li:nth-child(8) > span ~ div::text').get()
    print(data.strip())
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(9) > span::text').get(), ' ', end="")
    data = selector.css('#parameters > ul:nth-child(1) > li:nth-child(9) > div > a::attr(title)').get()
    print(data.strip())
    print(selector.css('#parameters > ul:nth-child(1) > li:nth-child(10) > span::text').get(), ' ', end="")
    data = selector.css('#parameters > ul:nth-child(1) > li:nth-child(10) > span ~ div::text').get()
    print(data.strip())

    currency = selector.css('.page-offer > section > div:nth-child(3) > div > span >span::text').get()
    print(currency)
    # TODO: dodaj wyszukiwanie lokalizacji
    loc = selector.css('.seller-box__seller-address > span:nth-child(2)::text').get()
    print(loc.strip())

offers = (
    'ford-focus-salon-polska-klima-sprawy-zadbany-polecam-ID6BxpMS.html',
    'ford-focus-1-6-tdci-salon-polska-serwis-aso-klima-ID6BwGlg.html'
)
for offer in offers:
    data = load_offer(offer)
    get_details(data)
    print('-' * 40)
