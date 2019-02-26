import linecache

file = open("rows.txt")

i = 0
tab = []
line = file.readline()
prev_val = 0
max_val = 0
min_val = 999999
controlSum = 0
controlSum2 = 0
controlSum1 = 0
while line:
    line = file.readline()
    i += 1


for Line in range(i+1):
    tab.append(linecache.getline('rows.txt',Line+1))

print(tab[0])

for row in range(i):
    for val in tab[row].split():
        val2 = int(val)
        if val2 > max_val:
            max_val = val2
        if val2 < min_val:
            min_val = val2
    sr_val = max_val - min_val

    print(sr_val)
    controlSum += sr_val
    max_val = 0
    min_val = 999999

print(controlSum)
