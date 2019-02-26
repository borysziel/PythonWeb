from collections import Counter
import linecache
import fileinput



linia = []

number = 0
counter_ost = []
for number in range(29):
    file = open("word_%d.txt" % number)
    tmp = file.readline()
    linia.append(tmp)
    linia[number] = linia[number].lower()
    if number == 0:
        counter0 = Counter(linia[number])
    else:
        counter = Counter(linia[number])
        counter0 = counter0 + counter

print(counter0)
# linia = file.readline()
# mala_linia = linia.lower()
# counter = Counter(mala_linia)
# print(counter)
