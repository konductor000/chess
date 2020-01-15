import Tkinter as tk
import tkFont as tkf

SCALE = 2

desk = tk.Tk()
l_label =[]
frame_num = tk.Frame(desk)
frame_num.pack(side = tk.LEFT, anchor=tk.NW)
for i in range(1,9):
	label = tk.Label(frame_num, text = i, bg = "green", width = SCALE * 2, height = SCALE)
	label.pack(side = tk.BOTTOM)


frame_let = tk.Frame(desk)
frame_let.pack(side = tk.BOTTOM, anchor = tk.SE)
for i in ["A", "B", "C", "D", "E", "F", "G", "H"]:
	label = tk.Label(frame_let, text = i, bg = "red", width = SCALE * 2, height = SCALE)
	label.pack(side = tk.LEFT)



chess_frame = tk.Frame(desk)
chess_frame.pack()
def do_smth(event):
	pass

for i in range(8):
	for j in range(8):
		if (j + i) % 2 != 0:
			col = "black"
		else:
			col = "white"
		label = tk.Label(chess_frame, bg = col, width = SCALE * 2, height = SCALE)


		label.grid(row = i, column = j)
		label.bind("<Button-1>", do_smth)

		#label["text"] = "a"


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