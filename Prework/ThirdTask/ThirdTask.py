import linecache

file = open("zadanie_4_triangle_big.txt")

line = file.readline()
lineNumber = 0
sum = 0
tab = [[]]
placeinRow = 0
column = 0
while line:
    line = file.readline()
    lineNumber += 1

for row in range(lineNumber + 1):
    tab.append(linecache.getline("zadanie_4_triangle_big.txt",row +1))
    tab[row] = tab[row].strip()


for row in range(lineNumber):
    tab.append([])
    for val in tab[row].split():
        val2 = int(val)
        tab[row][column] = val2
    column = 0

print(tab[2])
print(lineNumber)
