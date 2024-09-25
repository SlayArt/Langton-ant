# importations des modules necessaires
import numpy as np
import tkinter as tk


# créations des variables
size = 50

antx, anty = 25, 25

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # top / right / bottom / left
idx_rotation = 0

tab = np.zeros((size, size))


root = tk.Tk()
root.title("Langton ant Simulation")

cell_size = 20
canvas = tk.Canvas(root, width=size * cell_size, height=size * cell_size)
canvas.pack()


# creations des differentes fonctions
def rotate_left():
    global idx_rotation
    idx_rotation = (idx_rotation - 1) % 4

def rotate_right():
    global idx_rotation
    idx_rotation = (idx_rotation + 1) % 4

def forward():
    global antx, anty
    dx, dy = directions[idx_rotation]
    antx = (antx + dx) % size
    anty = (anty + dy) % size

def pheromone():
    tab[antx][anty] = True

def update():
    global antx, anty

    if tab[antx][anty] == 0:
        rotate_right()
        tab[antx][anty] = 1
    else:
        rotate_left()
        tab[antx][anty] = 0
    
    forward()
    grid()
    root.after(1, update)


def grid():
    canvas.delete("all")
    for i in range(size):
        for j in range(size):
            color = 'green' if tab[i][j] == 1 else 'black'
            x0 = j * cell_size
            y0 = i * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="grey")
    
    ant_x0 = anty * cell_size
    ant_y0 = antx * cell_size
    ant_x1 = ant_x0 + cell_size
    ant_y1 = ant_y0 + cell_size
    canvas.create_rectangle(ant_x0, ant_y0, ant_x1, ant_y1, fill='cyan', outline="grey")
        

# main script
grid()
root.after(1, update)
root.mainloop()