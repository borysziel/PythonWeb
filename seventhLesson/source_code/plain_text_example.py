from helpers import *
from pprint import pprint
import csv





if __name__ == '__main__':
    person = get_person(1)
    people = get_people_list()

    with open('pain.txt','w',encoding='UTF-8') as file_in:
        file_in.write(str(person))

    with open('people.csv','w',newline='\n') as csvfile:
        luke = csv.writer(csvfile)
        results = people['results']
        headers = results[0].keys()
        luke.writerow(headers)

        for i in range(10):
            entity = results[i].values()
            luke.writerow(entity)

    # with open('people.csv','r') as csvfile:
    #     reader = csv.reader(csvfile,delimiter=' ')
    #     for row in reader:
    #         print(', '.join(row))
    #
    # with open('people2.csv','w',newline='') as data2:
    #     save = csv.DictWriter(data2,person.keys())
    #     save.writeheader()
    #     save.writerow(person)

    with open('person2.csv','w',newline='') as data2:
        results = people['results']
        headers = results[0].keys()
        save = csv.DictWriter(data2,headers)
        save.writeheader()
        # for person in results:
        #     save.writerow(person)
        save.writerows(results)

    with open('person2.csv','r') as data2:
        reader = csv.DictReader(data2)
        print(reader.fieldnames)
        # for row in reader:
        #     for key,value in row.items():
        #         print(key,value)
