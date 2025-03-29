import tkinter

def klikni(index):
    hodnoty[index] += 1

    percent = list(x / sum(hodnoty) * 100 for x in hodnoty)
    max_index = percent.index(max(percent))
    canvas.delete("all")
    canvas.create_text(200, 50, text=riadky[0], fill="black")
    nakresli(max_index, hodnoty, percent)

def nakresli(max_index, hodnoty, percent):
    for i in range(3):
        fil = "red" if i != max_index else "green"
        canvas.create_text(200, 100 + i * 50, text=nazov[i] + str(hodnoty[i]), fill="black", anchor="w")
        canvas.create_rectangle(350, 80 + i * 50, 350 + 10 * percent[i], 120 + i * 50, fill=fil, outline="black")

        tlacidlo = tkinter.Button(root, text="Hlasuj tu", command=lambda i=i: klikni(i))
        tlacidlo.place(x=500, y=90 + i * 50)

with open("./MO_10/anketa.txt", "r", encoding="UTF-8") as subor:
    riadky = subor.readlines()

nazov = ["1)ano - ", "2)nie - ", "3)neviem - "]
hodnoty = list(int(x) for x in riadky[1].split())
percent = list(x / sum(hodnoty) * 100 for x in hodnoty)
max_index = percent.index(max(percent))

root = tkinter.Tk()  
root.title("Anketa")
canvas = tkinter.Canvas(root, width=1000, height=1000)
canvas.pack()
canvas.create_text(200, 50, text=riadky[0], fill="black")
nakresli(max_index, hodnoty, percent)

root.mainloop()