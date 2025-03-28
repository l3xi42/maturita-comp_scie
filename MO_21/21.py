def policko(size_rect, x, y, vypln, fil, pismeno):
    canvas.create_rectangle(x, y, x+size_rect, y+size_rect, fill = fil, outline="black")

    if vypln:
        canvas.create_text(x + (size_rect)//2, (size_rect)//2 + y, text=pismeno)

def krizovka(size_rect, x, y,slova, riadky, max_L, max_R):
    for i in range(len(riadky)):
        index, slovo = slova[i]
        for j in range(len(slovo)):
            fil = "dark green" if index - 1 == j else "light green"
            policko(size_rect, x + size_rect * (max_L - index + 1 + j), y + i * size_rect, False, fil, slovo[j])
            policko(size_rect, x +(2*max_L + max_R + 2 - index + j) * size_rect, y + i * size_rect, True, fil, slovo[j])
    

import tkinter
with open("krizovky1-1.txt", "r") as subor:
    riadky = subor.readlines()

size_rect, x, y = (int(x) for x in input().split())

slova = []
max_L = 0
max_R = 0

for i in range(len(riadky)):
    slova.append(riadky[i].split())
    slova[i][0] = int(slova[i][0])
    max_L = max(slova[i][0] - 1, max_L)
    max_R = max(len(slova[i][1]) - slova[i][0], max_R)
canvas = tkinter.Canvas(width=10000, height=10000)
canvas.pack()
krizovka(size_rect, x, y,slova, riadky, max_L, max_R)
canvas.mainloop()