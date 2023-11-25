
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe AI")

#set the clicked state
clicked = True
count = 0
title = "AI Tic Tac Toe"
grid = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
#function to disable buttons
def disable_all_buttons():
	for b in [b1,b2,b3,b4,b5,b6,b7,b8,b9]:
		b.config(state=DISABLED)
def bestMove():
    # AI to make its turn
    global grid, clicked, count
    bestScore = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            # Is the spot available?
            if grid[i][j] == ' ':
                grid[i][j] = "O"
                score = minimax(grid, 0, False)
                grid[i][j] = ' '
                if score > bestScore:
                    bestScore = score
                    move = (i, j)
    grid[move[0]][move[1]] = "O"
    set_grid(move[0] * 3 + move[1] + 1)
    clicked = True


scores = {
    'X': 10,
    'O': -10,
    'tie': 0
}

def minimax(grid, depth, isMaximizing):
	result = checkWin()
	if result is not None:
		return scores[result]

	if isMaximizing:
		bestScore = float('-inf')
		for i in range(3):
			for j in range(3):
			# Is the spot available?
				if grid[i][j] == ' ':
					grid[i][j] = "X"
					score = minimax(grid, depth + 1, False)
					grid[i][j] = ' '
					bestScore = max(score, bestScore)
		return bestScore
	else:
		bestScore = float('inf')
		for i in range(3):
			for j in range(3):
			# Is the spot available?
				if grid[i][j] == ' ':
					grid[i][j] = "O"
					score = minimax(grid, depth + 1, True)
					grid[i][j] = ' '
					bestScore = min(score, bestScore)
		return bestScore

#check if there's a winner
def checkWin():
	global winner, count
	winner = False

	if b1["text"] and grid[0][0] == "X" and b2["text"] and grid[0][1] == "X" and b3["text"] and grid[0][2] == "X":
		b1.config(bg="green")
		b2.config(bg="green")
		b3.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif b4["text"] and grid[1][0] == "X" and b5["text"] and grid[1][1] == "X" and b6["text"] and grid[1][2] == "X":
		b4.config(bg="green")
		b5.config(bg="green")
		b6.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif b7["text"] and grid[2][0] == "X" and b8["text"] and grid[2][1] == "X" and b9["text"] and grid[2][2] == "X":
		b7.config(bg="green")
		b8.config(bg="green")
		b9.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif b1["text"] and grid[0][0] == "X" and b4["text"] and grid[1][0] == "X" and b7["text"] and grid[2][0] == "X":
		b1.config(bg="green")
		b4.config(bg="green")
		b7.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif b2["text"] and grid[0][1] == "X" and b5["text"] and grid[1][1] == "X" and b8["text"] and grid[2][1] == "X":
		b2.config(bg="green")
		b5.config(bg="green")
		b8.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif b3["text"] and grid[0][2] == "X" and b6["text"] and grid[1][2] == "X" and b9["text"] and grid[2][2] == "X":
		b3.config(bg="green")
		b6.config(bg="green")
		b9.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif b1["text"] and grid[0][0] == "X" and b5["text"] and grid[1][1] == "X" and b9["text"] and grid[2][2] == "X":
		b1.config(bg="green")
		b5.config(bg="green")
		b9.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif b3["text"] and grid[0][2] == "X" and b5["text"] and grid[1][1] == "X" and b7["text"] and grid[2][0] == "X":
		b3.config(bg="green")
		b5.config(bg="green")
		b7.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	#set for O
	elif b1["text"] and grid[0][0] == "O" and b2["text"] and grid[0][1] == "O" and b3["text"] and grid[0][2] == "O":
		b1.config(bg="green")
		b2.config(bg="green")
		b3.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif b4["text"] and grid[1][0] == "O" and b5["text"] and grid[1][1] == "O" and b6["text"] and grid[1][2] == "O":
		b4.config(bg="green")
		b5.config(bg="green")
		b6.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif b7["text"] and grid[2][0] == "O" and b8["text"] and grid[2][1] == "O" and b9["text"] and grid[2][2] == "O":
		b7.config(bg="green")
		b8.config(bg="green")
		b9.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif b1["text"] and grid[0][0] == "O" and b4["text"] and grid[1][0] == "O" and b7["text"] and grid[2][0] == "O":
		b1.config(bg="green")
		b4.config(bg="green")
		b7.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif b2["text"] and grid[0][1] == "O" and b5["text"] and grid[1][1] == "O" and b8["text"] and grid[2][1] == "O":
		b2.config(bg="green")
		b5.config(bg="green")
		b8.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif b3["text"] and grid[0][2] == "O" and b6["text"] and grid[1][2] == "O" and b9["text"] and grid[2][2] == "O":
		b3.config(bg="green")
		b6.config(bg="green")
		b9.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif b1["text"] and grid[0][0] == "O" and b5["text"] and grid[1][1] == "O" and b9["text"] and grid[2][2] == "O":
		b1.config(bg="green")
		b5.config(bg="green")
		b9.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif b3["text"] and grid[0][2] == "O" and b5["text"] and grid[1][1] == "O" and b7["text"] and grid[2][0] == "O":
		b3.config(bg="green")
		b5.config(bg="green")
		b7.config(bg="green")
		winner = True
		messagebox.showinfo(title, "Congratulations! You won.")
		disable_all_buttons()
	elif count == 9:
		messagebox.showinfo(title, "It's a tie")
		disable_all_buttons()



def set_grid(spt, v):
	print("\n")
	if spt == 1:
		grid[0][0] = v
	elif spt == 2:
		grid[0][1] = v
	elif spt == 3:
		grid[0][2] = v
	elif spt == 4:
		grid[1][0] = v
	elif spt == 5:
		grid[1][1] = v
	elif spt == 6:
		grid[1][2] = v
	elif spt == 7:
		grid[2][0] = v
	elif spt == 8:
		grid[2][1] = v
	elif spt == 9:
		grid[2][2] = v
	for i in grid:
		print(i)

#check if button is clicked
def b_click(b, pos):
	global clicked, count
	#bestMove()
	if b["text"] == " " and clicked == True:
		b["text"] = "X"
		clicked = False
		count += 1
		set_grid(pos, "X")
		checkWin()
	elif b["text"] == " " and clicked == False:

		b["text"] = "O"
		clicked = True

		count += 1
		set_grid(pos, "O")
		checkWin()
	else:
		messagebox.showerror(title, "Spot already occupied.\nPlease pick another empty space")

def reset():
	global grid
	grid = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
	global b1,b2,b3,b4,b5,b6,b7,b8,b9
	global clicked, count
	clicked = True
	count = 0
	b1 = Button(root, text=" ", font=("Poppins", 20), height=3, width=6, bg="silver", command=lambda:b_click(b1,1))
	b2 = Button(root, text=" ", font=("Poppins", 20), height=3, width=6, bg="silver", command=lambda:b_click(b2,2))
	b3 = Button(root, text=" ", font=("Poppins", 20), height=3, width=6, bg="silver", command=lambda:b_click(b3,3))

	b4 = Button(root, text=" ", font=("Poppins", 20), height=3, width=6, bg="silver", command=lambda:b_click(b4,4))
	b5 = Button(root, text=" ", font=("Poppins", 20), height=3, width=6, bg="silver", command=lambda:b_click(b5,5))
	b6 = Button(root, text=" ", font=("Poppins", 20), height=3, width=6, bg="silver", command=lambda:b_click(b6,6))

	b7 = Button(root, text=" ", font=("Poppins", 20), height=3, width=6, bg="silver", command=lambda:b_click(b7,7))
	b8 = Button(root, text=" ", font=("Poppins", 20), height=3, width=6, bg="silver", command=lambda:b_click(b8,8))
	b9 = Button(root, text=" ", font=("Poppins", 20), height=3, width=6, bg="silver", command=lambda:b_click(b9,9))

	#Set button layout
	b1.grid(row=0, column=0)
	b2.grid(row=0, column=1)
	b3.grid(row=0, column=2)

	b4.grid(row=1, column=0)
	b5.grid(row=1, column=1)
	b6.grid(row=1, column=2)

	b7.grid(row=2, column=0)
	b8.grid(row=2, column=1)
	b9.grid(row=2, column=2)

gamemenu = Menu(root)
root.config(menu=gamemenu)

options_menu = Menu(gamemenu, tearoff=False)
gamemenu.add_cascade(label="options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)

reset()

root.mainloop()