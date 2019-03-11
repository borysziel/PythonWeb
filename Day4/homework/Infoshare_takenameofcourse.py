import requests

url = 'https://infoshareacademy.com/?s&city=Gda%C5%84sk'
url_list = ["https://infoshareacademy.com/?s&city=Gda%C5%84sk","https://infoshareacademy.com/?s&city=Krak%C3%B3w","https://infoshareacademy.com/?s&city=Lublin"]
url_number_course = ["10","3","5"]


key_word = 'course-title'
text_to_find = '<span>'
text_to_find2 = '</span>'
key_word2 = '<p class='
text_to_find3 = 'paragraph--date">'
text_to_find4 = '</p>'
town_keyword = 'paragraph--loc">'
for x in range(len(url_list)):

    response = requests.get(url_list[x])
    content = str(response.content)
    results_position = content.find(key_word)
    results_position2 = content.find(key_word2)

    town_position1 = content.find(town_keyword,results_position) + len(town_keyword)
    town_position2 = content.find(text_to_find4,town_position1)
    print("\n")
    print(content[town_position1:town_position2])
    for i in range(int(url_number_course[x])):
        results_position0 = content.find(text_to_find,results_position)
        position1 = content.find(text_to_find2,results_position0)


        date_position1 = content.find(text_to_find3,results_position2)
        date_position2 = content.find(text_to_find4,date_position1)
        print(content[results_position0 + len(text_to_find):position1])
        print(content[date_position1 + len(text_to_find3):date_position2])

        results_position = position1
        results_position2 = date_position2

    # span_pos1 = content.find('span', result_number_pos) + len('span>')
    # span_pos2 = content.find('</span', span_pos1)
    #
    # print(content[span_pos1:span_pos2])
    # result_number_pos = span_pos2 + len('span')