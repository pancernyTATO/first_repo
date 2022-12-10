path = "C:\\Users\\vdi-student\\Desktop\\rozliczenie.csv"
mode = 'r'

with open (path, mode) as plik1:
    content = plik1.readlines()
print(content)
for i in range(len(content)):
    content[i] = content[i].split(',')
print(content)
print(content[3][3]) #pierwsze 3 to linia, drugie 3 to pole w tablicy

#obliczanie sredniej wyplaty
total = 0
for i in range(1,len(content)):
    total = total + int(content[i][1])
average = total / (len(content)-1)
print(round(average,2))

#ile kobiet na macierzynskim
total = 0
for i in range(1,len(content)):
    if content[i][3] == 'k' and content[i][4] == 't':
        total += 1
print(total)
