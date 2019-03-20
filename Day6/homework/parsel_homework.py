from parsel import Selector
import requests
import os


def get_page(url,filename):
    if os.path.isfile(filename) and os.stat(filename).st_size:
        with open(filename, 'r', encoding='utf-8') as input_data:
            content = input_data.read()
    else:
        response = requests.get(url)
        content = response.text
        with open(filename, 'w', encoding='utf-8') as output_data:
            output_data.write(content)
    return content



if __name__ == '__main__':
    url = 'https://allegro.pl/ogloszenie/audi-a6-3-0-tdi-skory-bi-xenon-navi-sedan-7877345107'
    filename = 'audi.html'
    html_content = get_page(url,filename)

    selector = Selector(text=html_content)

    nazwa = selector.xpath('//*[@id="user_field"]/article/div/section[1]/div/section/h1/text()').get()
    print(nazwa)

    for i in range(1,11):
        stan = selector.xpath('//*[@data-box-name="Parameters"]/div/ul/li/div/div/ul/li[%d]/div/div/text()' %i).get()
        stan2 = selector.xpath('//*[@data-box-name="Parameters"]/div/ul/li/div/div/ul/li[%d]/div/div[2]/text()' %i).get()
        print(stan + " " + stan2)

    for n in range(1,11):
        stan = selector.xpath('//*[@data-box-name="Parameters"]/div/ul/li/div/div/ul[2]/li[%d]/div/div/text()' %n).get()
        stan2 = selector.xpath('//*[@data-box-name="Parameters"]/div/ul/li/div/div/ul[2]/li[%d]/div/div[2]/text()' %n).get()
        print(stan + " " + stan2)