from helpers import *
from pprint import pprint
import json




if __name__ == '__main__':
    person_id = 1
    person = get_person(person_id)
    people = get_people_list()

    with open('person.json','w') as output_files:
        json.dump(person,output_files, indent=4)

    with open('person.json','r') as output_files:
        data = json.load(output_files)
        print(data['name'])
    #     zadanie obslizyc wyjatek

    with open('people.json','w') as output_files:
        json.dump(people,output_files, indent=4)

    with open('people.json','r') as output_files:
        data = json.load(output_files)
        print(data['count'])
        print(data['results'][2])
