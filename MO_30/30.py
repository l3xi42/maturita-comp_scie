import tkinter as tk
import math
with open("./MO_30/priklad.txt", "r", encoding="UTF-8") as subor:
    riadky = subor.readlines()

#tu check

#tu check
max_dlzka = math.ceil(math.sqrt(len(riadky[0])))
canvas = tk.Canvas(width = 1000, height = 1000)
canvas.pack()

for i in range(max_dlzka):
    for j in range(max_dlzka if max_dlzka*max_dlzka < len(riadky[0])+max_dlzka else max_dlzka - 1):
        x1 = 100 + i * 50
        y1 = 100 + j * 50
        x2 = x1 + 50
        y2 = y1 + 50
        canvas.create_rectangle(x1, y1, x2, y2)
        
        index = i * max_dlzka + j
        if 0 <= index < len(riadky[0]):
            # Calculate the center of the rectangle
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2
            # Place the letter at the center
            canvas.create_text(center_y, center_x, text=riadky[0][index])

canvas.mainloop()