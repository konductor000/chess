import tkinter as tk
class Chess(object):
	def __init__(self):
		self.SCALE = 2

		self.letter_to_index = {"A":0, "B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
		# lables = list of lists (8, 8)
		self.desk, self.labels = self.MakeDesk()

	def OnClick(self, event):
		pass

	def GetIndexByPos(self, pos):
		i = 8 - int(pos[1])
		j = self.letter_to_index[pos[0].upper()]
		return i, j

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

	def PlaceFigureOnBoard(self, pos, figure, color):
		#pos - string ("A2"), figure - string "P", color - string ("W" or "B")
		i, j = self.GetIndexByPos(pos)
		label = self.labels[i][j] # TODO

		label["text"] = figure
		label["fg"] = "green" if color == "W" else "red"


	



	def Run(self):
		self.desk.mainloop()
		print(1)


if __name__ == "__main__":
	board = Chess()

	board.PlaceFigureOnBoard("a7", "П", "W")
	board.PlaceFigureOnBoard("b7", "П", "W")
	board.PlaceFigureOnBoard("c7", "П", "W")
	board.PlaceFigureOnBoard("d7", "П", "W")
	board.PlaceFigureOnBoard("e7", "П", "W")
	board.PlaceFigureOnBoard("f7", "П", "W")
	board.PlaceFigureOnBoard("g7", "П", "W")
	board.PlaceFigureOnBoard("h7", "П", "W")
	board.PlaceFigureOnBoard("a8", "Л", "W")
	board.PlaceFigureOnBoard("h8", "Л", "W")
	board.PlaceFigureOnBoard("b8", "К", "W")
	board.PlaceFigureOnBoard("c8", "С", "W")
	board.PlaceFigureOnBoard("d8", "Д", "W")
	board.PlaceFigureOnBoard("e8", "Б", "W")
	board.PlaceFigureOnBoard("g8", "К", "W")
	board.PlaceFigureOnBoard("f8", "С", "W")

	board.PlaceFigureOnBoard("a2", "П", "B")
	board.PlaceFigureOnBoard("b2", "П", "B")
	board.PlaceFigureOnBoard("c2", "П", "B")
	board.PlaceFigureOnBoard("d2", "П", "B")
	board.PlaceFigureOnBoard("e2", "П", "B")
	board.PlaceFigureOnBoard("f2", "П", "B")
	board.PlaceFigureOnBoard("g2", "П", "B")
	board.PlaceFigureOnBoard("h2", "П", "B")
	board.PlaceFigureOnBoard("a1", "Л", "B")
	board.PlaceFigureOnBoard("h1", "Л", "B")
	board.PlaceFigureOnBoard("b1", "К", "B")
	board.PlaceFigureOnBoard("c1", "С", "B")
	board.PlaceFigureOnBoard("d1", "Д", "B")
	board.PlaceFigureOnBoard("e1", "Б", "B")
	board.PlaceFigureOnBoard("g1", "К", "B")
	board.PlaceFigureOnBoard("f1", "С", "B")





	board.Run()