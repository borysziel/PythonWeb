import requests

url = 'https://www.lotto.pl'
# response = requests.get(url)
# content = response.text
# lotto_numbers_start_pos = content.find('resultsItem lotto')
# result_number_pos = content.find('resultnumber', lotto_numbers_start_pos)
bets_start_pos = ["resultsItem lotto","resultsItem lottoPlus","resultsItem lottoSzansa","resultsItem euroJackpot","resultsItem EkstraPensja"]
bets_number_of_digits = ["6","6","7","8","7"]
file = open("LottoData.txt","w")
lotto_data = requests.get(url)
file.write(str(lotto_data.content))

read_file = open("LottoData.txt","r")
file_information = read_file.read()
# read file


for x in range(len(bets_start_pos)):


    lotto_numbers_start_pos = file_information.find(bets_start_pos[x])
    result_name_pos = file_information.find('<a href', lotto_numbers_start_pos)
    # Znalezienie nazwy, nie dziala dobrze
    name_pos1 = file_information.find('>',result_name_pos) + 1
    name_pos2 = file_information.find('</a',name_pos1)

    name = file_information[name_pos1:name_pos2]
    print(name.strip())

    # Znalezienie daty
    result_date_pos = file_information.find('resultsTime', lotto_numbers_start_pos)
    date_pos1 = file_information.find('<strong',result_date_pos) + len('<strong>')
    date_pos2 = file_information.find('</stron',date_pos1)
    time_pos1 = file_information.find('<strong',date_pos1) + len('<strong>')
    time_pos2 = file_information.find('</strong',time_pos1)
    print("Wyniki z dnia: " + file_information[date_pos1:date_pos2] + " Godzina: " + file_information[time_pos1:time_pos2])
    result_number_pos = file_information.find('resultnumber', lotto_numbers_start_pos)

    for i in range(int(bets_number_of_digits[x])):
        span_pos1 = file_information.find('span', result_number_pos) + len('span>')
        span_pos2 = file_information.find('</span', span_pos1)

        print(file_information[span_pos1:span_pos2])
        result_number_pos = span_pos2 + len('span')


file.close()

