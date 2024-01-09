import numpy as np

ll = [x for x in open("input.txt").read().strip().split("\n")]

DIRS = {
	"U": (0, 1),
	"D": (0, -1),
	"L": (-1, 0),
	"R": (1, 0)
}

curr_pos_x = 0
curr_pos_y = 0

num_points = 0

xs = []
ys = []

for l in ll:
	dirstr, nstr, code = l.split(" ")
	hexcode = code[1:-1]
	n = int(nstr)
	direction = DIRS[dirstr]
	curr_pos_x += direction[0] * n
	curr_pos_y += direction[1] * n
	num_points += n
	xs.append(curr_pos_x)
	ys.append(curr_pos_y)

area = num_points

for i in range(len(xs) - 1):
	area += xs[i + 1] * ys[i] - xs[i] * ys[i + 1]

print(1 + area // 2)
