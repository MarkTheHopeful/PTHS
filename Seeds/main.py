import tkinter
import random
import time

__author__ = 'Ipatov_Mark'

WIDTH = 500
HEIGHT = 500
START_POS = 200, 200
COLORS = ["red", "yellow", "green", "blue"]
# K = 3
# R = 180
K, R = map(int, input("Enter constants: K, R\n").split())

# Interesting: 5|100 4|120;


class Seed:
    def __init__(self, x, y, canvas, gen=0):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.gen = gen

    def check(self, seed):
        if (((self.x - seed.x) ** 2 + (self.y - seed.y) ** 2) ** 0.5 <= R) and (self.gen != seed.gen):
            return True
        return False

    def paint(self):
        self.id = self.canvas.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, fill=COLORS[self.gen % 4])

    def delete(self):
        self.canvas.delete(self.id)


root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
seeds = [Seed(START_POS[0], START_POS[1], canvas)]
seeds[0].paint()
gen = 0
while True:
    n = len(seeds)
    for i in range(min(int(n * K), 1000)):
        seed = Seed(random.randint(0, WIDTH), random.randint(0, HEIGHT), canvas, gen + 1)
        isAlive = True
        for otherSeed in seeds:
            if (otherSeed.check(seed)):
                isAlive = False
                break
        if isAlive:
            seeds.append(seed)
            seed.paint()
    for i in range(n):
        seeds[i].delete()
    seeds = seeds[n:]
    gen += 1
    time.sleep(0.2)
    root.update()

