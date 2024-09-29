# importations des modules necessaires
import numpy as np
import tkinter as tk
from math import sqrt
import random


# créations des variables
size = int(sqrt(int(input("How many cells in the grid ? ")))) # min 1000 cell is recommanded

ants = []
colors = ['green', 'blue', 'red', 'cyan', 'yellow', 'magenta']
count_colors = 0

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # top / right / bottom / left

tab = np.zeros((size, size), dtype=object)

root = tk.Tk()
root.title("Langton ant Simulation")

cell_size = 20
canvas = tk.Canvas(root, width=size * cell_size, height=size * cell_size)
canvas.pack()

running = True


# creations des differentes fonctions
def ant(x, y):
    global count_colors
    new_ant = {'x': x, 'y': y, 'color': colors[count_colors], 'direction': 0}
    count_colors = (count_colors + 1) % len(colors)
    return new_ant

ants.append(ant(size // 2, size // 2))

def rotate_left(ant):
    ant['direction'] = (ant['direction'] - 1) % 4

def rotate_right(ant):
    ant['direction'] = (ant['direction'] + 1) % 4

def forward(ant):
    dx, dy = directions[ant['direction']]
    ant['x'] = (ant['x'] + dx) % size
    ant['y'] = (ant['y'] + dy) % size

def update():
    if running:
        for ant in ants:
            x, y = ant['x'], ant['y']
            if tab[x][y] == 0:
                rotate_right(ant)
                tab[x][y] = ant['color']
            else:
                rotate_left(ant)
                tab[x][y] = 0
            forward(ant)
    
    grid()
    root.after(1, update)


def grid():
    canvas.delete("all")
    for i in range(size):
        for j in range(size):
            color = tab[i][j] if tab[i][j] != 0 else 'black'
            x0 = j * cell_size
            y0 = i * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size
            canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="grey")
    
    for ant in ants:
        ant_x0 = ant['y'] * cell_size
        ant_y0 = ant['x'] * cell_size
        ant_x1 = ant_x0 + cell_size
        ant_y1 = ant_y0 + cell_size
        canvas.create_rectangle(ant_x0, ant_y0, ant_x1, ant_y1, fill='white', outline="grey")

def click_state(event):
    x, y = event.x // cell_size, event.y // cell_size
    if 0 <= x < size and 0 <= y < size:
        if not any(ant['x'] == x and ant['y'] == y for ant in ants):
            new_ant = ant(y, x)
            ants.append(new_ant)
    grid()

canvas.bind("<Button-1>", click_state)

def toggle_sim(event):
    global running
    running = not running
root.bind("<space>", toggle_sim)


# main script
grid()
root.after(1, update)
root.mainloop()
