import Tkinter as tk
import tkFont as tkf

desk = tk.Tk()
l_label =[]
label_1 = tk.Label(desk, text = "1")
label_2 = tk.Label(desk, text = "2")
label_1.grid(row = 0)
label_2.grid(row = 1)

for i in range(8):
	for j in range(8):
		label = tk.Label(desk, text = i * 8 +j +1)
		label.grid(row = i, column = j)

'''
for i in range(8):
	frame = tk.Frame(desk)
	frame.pack()
	for j in range(8):
		label = tk.Label(frame, text = str(i*8+j), bg = 'white', fg="black")
		label.pack(side = tk.LEFT)

'''





#the_label = tk.Label(desk, text = "tre")
#the_label.pack()
#screen_height = desk.winfo_screenheight()
#screen_width = desk.winfo_screenwidth()
#print(screen_height)
#print(screen_width)

desk.mainloop()
print(1)