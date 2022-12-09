import itertools as it

ll = [x for x in open("input.txt").read().strip().split("\n")]

head_position = [0, 0]
tail_position = [0, 0]
last_head_position = [0, 0]
positions = []

def update_tail():
    global head_position
    global tail_position
    global positions
    dx = head_position[0] - tail_position[0]
    dy = head_position[1] - tail_position[1]
    if abs(dx) > 1 or abs(dy) > 1:
        tail_position[0] = last_head_position[0]
        tail_position[1] = last_head_position[1]
    elif abs(dx) > 1:
        tail_position[0] = last_head_position[0]
    elif abs(dy) > 1:
        tail_position[1] = last_head_position[1]

def move_head_by_one(dir):
    global head_position
    global tail_position
    global positions
    if dir == 'L':
        head_position[0] -= 1
    elif dir == 'R':
        head_position[0] += 1
    elif dir == 'U':
        head_position[1] += 1
    elif dir == 'D':
        head_position[1] -= 1

for l in ll:
    direction, amount_char = l.split(" ")
    amount = int(amount_char)
    for i in range(amount):
        move_head_by_one(direction)
        update_tail()
        positions.append([tail_position[0], tail_position[1]])
        last_head_position[0] = head_position[0]
        last_head_position[1] = head_position[1]

unique_positions = []

for pos in positions:
    if not (pos in unique_positions):
        unique_positions.append(pos)

print("unique positions = " + str(len(unique_positions)))
