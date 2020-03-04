# -*- coding: utf-8 -*-
import tkinter as tk
class Chess(object):
	def __init__(self):
		self.IsClicked = False 
		self.SCALE = 2 

		self.letter_to_index = {"A":0, "B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7} 
		# lables = list of lists (8, 8)
		self.desk, self.labels = self.MakeDesk()

	def GetFigure(self, row, column):
		pos = column + str(row)
		i, j = self.GetIndexByPos(pos)
		label = self.labels[i][j]
		return label["text"]

	def OnClick(self, row, column):	
		pos = column + str(row)
		i, j = self.GetIndexByPos(pos)
		label = self.labels[i][j]
		#inf = (row, column, label["text"], label["fg"])
		if label["text"] == "P":
			if label["fg"] == "red":
				if row == 2:
					step = (column, row + 1, column, row + 2)
					print(step)
					if str(step[2]) + str(step[3]) == column:
						step.remove(2, 3)
				if row != 2:
					step = (column, row + 1)
					print(step)
					if str(step[0]) + str(step[1]) == column:
						step.remove(0, 1)
			if label["fg"] == "green":
				if row == 7:
					step = (column, row - 1, column, row - 2)
					print(step)
				if row != 7:
					step = (column, row - 1)
					print(step)




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
		letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
		for i in letters:
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
				label.bind("<Button-1>", lambda event, row = 8 - i, column = letters[j]: self.OnClick(row, column))
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

	board.PlaceFigureOnBoard("a7", "P", "W")
	board.PlaceFigureOnBoard("b7", "P", "W")
	board.PlaceFigureOnBoard("c7", "P", "W")
	board.PlaceFigureOnBoard("d7", "P", "W")
	board.PlaceFigureOnBoard("e7", "P", "W")
	board.PlaceFigureOnBoard("f7", "P", "W")
	board.PlaceFigureOnBoard("g7", "P", "W")
	board.PlaceFigureOnBoard("h7", "P", "W")
	board.PlaceFigureOnBoard("a8", "R", "W")
	board.PlaceFigureOnBoard("h8", "R", "W")
	board.PlaceFigureOnBoard("b8", "H", "W")
	board.PlaceFigureOnBoard("c8", "E", "W")
	board.PlaceFigureOnBoard("d8", "Q", "W")
	board.PlaceFigureOnBoard("e8", "K", "W")
	board.PlaceFigureOnBoard("g8", "H", "W")
	board.PlaceFigureOnBoard("f8", "E", "W")

	board.PlaceFigureOnBoard("a2", "P", "B")
	board.PlaceFigureOnBoard("b2", "P", "B")
	board.PlaceFigureOnBoard("c2", "P", "B")
	board.PlaceFigureOnBoard("c3", "P", "B")#3
	board.PlaceFigureOnBoard("b4", "P", "B")#3
	board.PlaceFigureOnBoard("d2", "P", "B")
	board.PlaceFigureOnBoard("e2", "P", "B")
	board.PlaceFigureOnBoard("f2", "P", "B")
	board.PlaceFigureOnBoard("g2", "P", "B")
	board.PlaceFigureOnBoard("h2", "P", "B")
	board.PlaceFigureOnBoard("a1", "R", "B")
	board.PlaceFigureOnBoard("h1", "R", "B")
	board.PlaceFigureOnBoard("b1", "H", "B")
	board.PlaceFigureOnBoard("c1", "E", "B")
	board.PlaceFigureOnBoard("d1", "Q", "B")
	board.PlaceFigureOnBoard("e1", "K", "B")
	board.PlaceFigureOnBoard("g1", "H", "B")
	board.PlaceFigureOnBoard("f1", "E", "B")


	board.Run()
	
	