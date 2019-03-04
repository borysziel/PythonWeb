import requests

url = 'https://www.nbp.pl/kursy/xml/a223z181116.xml'

response = requests.get(url)
content = response.text
currency_start_pos = content.find('pozycja')
# result_number_pos = content.find('resultnumber', currency_start_pos)

for x in range(35):
    name_currency1 = content.find('nazwa_waluty',currency_start_pos) + len('<nazwa_waluty')
    name_currency2 = content.find('</nazwa_waluty',name_currency1)

    code_currency1 = content.find('kod_waluty',name_currency2) + len('<kod_waluty')
    code_currency2 = content.find('</kod_waluty',code_currency1)

    exchange_rate1 = content.find('kurs_sredni',code_currency2) + len('<kurs_sredni')
    exchange_rate2 = content.find('</kurs_sredni',exchange_rate1)

    currency_start_pos = exchange_rate2
    print("Waluta: " + content[name_currency1:name_currency2] + " Skrót: " + content[code_currency1:code_currency2] + " Kurs: " + content[exchange_rate1:exchange_rate2] + "\n")