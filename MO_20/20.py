with open("./MO_20/knihy.txt", "r", encoding="UTF-8") as subor:
    riadky = subor.readlines()

knihy = []
dates_pairs = []
naj_pozic = (-1, -1)
for i in range(1, len(riadky), 2):  
    dates = [int(x) for x in riadky[i].split()]  
    date_pairs = [(num // 100, num % 100) for num in dates]
    pozicane = 0
    upom = False
    for j in range(1, len(date_pairs)):  
        if date_pairs[j][0] > date_pairs[j-1][0]:
            pridaj = date_pairs[j][0] - date_pairs[j-1][0] + 30*(date_pairs[j][1] - date_pairs[j-1][1])
            pozicane += pridaj
        else:
            pridaj = 30-date_pairs[j-1][0] - (0-date_pairs[j][0])+ 30*(date_pairs[j][1] - date_pairs[j-1][1] - 1)
            pozicane += pridaj
        if(pridaj > 30):
            upom = True
            
    dates_pairs.append(date_pairs)  
    knihy.append((riadky[i-1], pozicane, upom)) 
print("treba poslat upominku:")

for i in range(len(knihy)):
    if knihy[i][2] == True:
        print(knihy[i][0])

print("najviac pozicana kniha:")
print(knihy[knihy.index(max(knihy, key=lambda x: x[1]))][0])

zoradene = sorted(knihy, key=lambda x: x[1])
print("Zoradene podla doby vypozicania:")

for item in zoradene:
    print(item[0])

