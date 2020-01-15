import Tkinter as tk
import tkFont as tkf

class Chess(object):
	def __init__(self):
		self.SCALE = 2
		self.desk, self.labels = self.MakeDesk()

	def OnClick(self, event):
		pass

	def MakeDesk(self):
		desk = tk.Tk()
		frame_num = tk.Frame(desk)
		frame_num.pack(side = tk.LEFT, anchor=tk.NW)
		for i in range(1,9):
			label = tk.Label(frame_num, text = i, bg = "green", width = self.SCALE * 2, height = self.SCALE)
			label.pack(side = tk.BOTTOM)

		frame_let = tk.Frame(desk)
		frame_let.pack(side = tk.BOTTOM, anchor = tk.SE)
		for i in ["A", "B", "C", "D", "E", "F", "G", "H"]:
			label = tk.Label(frame_let, text = i, bg = "red", width = self.SCALE * 2, height = self.SCALE)
			label.pack(side = tk.LEFT)

		chess_frame = tk.Frame(desk)
		chess_frame.pack()

		labels = []
		for i in range(8):
			labels.append([])
			for j in range(8):
				if (j + i) % 2 != 0:
					col = "black"
				else:
					col = "white"
				label = tk.Label(chess_frame, bg = col, width = self.SCALE * 2, height = self.SCALE)
				label.grid(row = i, column = j)
				label.bind("<Button-1>", self.OnClick)

				labels[i].append(label)
				#label["text"] = "a"

		return desk,labels

	def Run(self):
		self.desk.mainloop()
		print(1)


if __name__ == "__main__":
	board = Chess()
	board.Run()

