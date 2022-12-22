import itertools as it

ll = [x for x in open("input.txt").read().strip().split("\n")]

rope = [[0, 0] for i in range(1 + 9)]
positions = []

def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    return 0

def update_tail_rcsv(last_pos, idx):
    global rope
    if idx >= 10:
        return
    curr_pos = rope[idx]
    dx = last_pos[0] - curr_pos[0]
    dy = last_pos[1] - curr_pos[1]
    if abs(dx) > 1 or abs(dy) > 1:
        curr_pos[0] += sign(dx)
        curr_pos[1] += sign(dy)
    update_tail_rcsv(curr_pos, idx+1)

def move_head_by_one(dir):
    global rope
    if dir == 'L':
        rope[0][0] -= 1
    elif dir == 'R':
        rope[0][0] += 1
    elif dir == 'U':
        rope[0][1] += 1
    elif dir == 'D':
        rope[0][1] -= 1

for l in ll:
    direction, amount_char = l.split(" ")
    amount = int(amount_char)
    for i in range(amount):
        move_head_by_one(direction)
        update_tail_rcsv(rope[0], 1)
        positions.append([rope[-1][0], rope[-1][1]])

print("unique positions = " + str(len(set([tuple(p) for p in positions]))))
