LARGE_VALUE = 99999
grid = [x for x in open("input.txt").read().strip().split("\n")]
HEIGHT = len(grid)
WIDTH = len(grid[0])
distances = [[-1 for _ in range(WIDTH)] for _ in range(HEIGHT)]
starting_pos = [0, 0]
ending_pos = [0, 0]
nodes = []

def add_node(x, y):
    if x < 0 or x >= WIDTH:
        return
    if y < 0 or y >= HEIGHT: 
        return
    nodes.append([x, y])

def calc_distance(x, y, nx, ny) -> int:
    if nx < 0 or nx >= WIDTH or ny < 0 or ny >= HEIGHT:
        return LARGE_VALUE
    if distances[ny][nx] == -1:
        return LARGE_VALUE
    ch = grid[y][x]
    if ch == 'S': ch = 'a'
    if ch == 'E': ch = 'z'
    nch = grid[ny][nx]
    if nch == 'S': nch = 'a'
    if nch == 'E': nch = 'z'
    delta = ord(ch) - ord(nch)
    if delta > 1:
        return LARGE_VALUE
    return distances[ny][nx]

for y in range(HEIGHT):
    for x in range(WIDTH):
        if grid[y][x] == 'S':
            starting_pos = [x, y]
        elif grid[y][x] == 'E':
            ending_pos = [x, y]

add_node(starting_pos[0], starting_pos[1])

while len(nodes) > 0:
    pos = nodes.pop()
    x = pos[0]
    y = pos[1]
    l1 = calc_distance(x, y, x - 1, y)
    l2 = calc_distance(x, y, x + 1, y)
    l3 = calc_distance(x, y, x, y - 1)
    l4 = calc_distance(x, y, x, y + 1)
    minimum = min(l1, l2, l3, l4)
    if minimum == LARGE_VALUE:
        minimum = -1
        if pos == starting_pos:
            minimum = 0
    else:
        minimum += 1
    if distances[y][x] != -1 and distances[y][x] <= minimum:
        continue
    distances[y][x] = minimum
    if minimum == -1:
        continue
    add_node(x - 1, y)
    add_node(x + 1, y)
    add_node(x, y - 1)
    add_node(x, y + 1)

print("min dist = " + str(distances[ending_pos[1]][ending_pos[0]]))
