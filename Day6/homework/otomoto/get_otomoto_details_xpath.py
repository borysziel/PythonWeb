import os
from parsel import Selector


def load_offer(_offer):
    file_name = os.path.join('data', _offer)
    with open(file_name, encoding='utf-8') as _file_in:
        _data = _file_in.read()

    return _data


def get_details(_data):
    selector = Selector(text=_data)

    # selector xpath object wskazujący na tytuł strony
    # print(selector.xpath('//title/text()'))

    # by wydobyć tekst z HTML trzeba skorzystać z konstrukcji poniżej
    print(selector.xpath('//title/text()').get())  # pojedynczy, pierwszy rezultat

    # TODO: dodaj kolejne etykietki
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[2]/span/text()').get(), ' ', end="")
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[2]/div/a/@title').get())
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[6]/span/text()').get(), ' ', end="")
    data = selector.xpath('//*[@id="parameters"]/ul[1]/li[6]/div/text()').get()
    print(data.strip())
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[7]/span/text()').get(), ' ', end="")
    data = selector.xpath('//*[@id="parameters"]/ul[1]/li[7]/div/text()').get()
    print(data.strip())
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[8]/span/text()').get(), ' ', end="")
    data = selector.xpath('//*[@id="parameters"]/ul[1]/li[8]/div/text()').get()
    print(data.strip())
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[9]/span/text()').get(), ' ', end="")
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[9]/div/a/@title').get())
    print(selector.xpath('//*[@id="parameters"]/ul[1]/li[10]/span/text()').get(), ' ', end="")
    data = selector.xpath('//*[@id="parameters"]/ul[1]/li[10]/div/text()').get()
    print(data.strip())
    # TODO: dodaj wyszukiwanie waluty
    currency= selector.xpath('//*[@id="siteWrap"]/main/section/div[3]/div[1]/span[1]/span/text()').get()
    print(currency.strip())
    # TODO: dodaj wyszukiwanie lokalizacji
    loc = selector.xpath('//*[@id="siteWrap"]/main/div[2]/div[1]/div[1]/div[1]/div[3]/span[2]/text()').get()
    print(loc)
offers = (
    'ford-focus-salon-polska-klima-sprawy-zadbany-polecam-ID6BxpMS.html',
    'ford-focus-1-6-tdci-salon-polska-serwis-aso-klima-ID6BwGlg.html'
)
for offer in offers:
    data = load_offer(offer)
    get_details(data)
    print('-' * 40)
