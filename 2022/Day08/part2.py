ll = [x for x in open("input.txt").read().strip().split("\n")]

# cmd-c
# aaandd cmd-v

def calc_scenic_score(x, y):
    hh = int(ll[y][x])
    height = len(ll)
    width = len(ll[0])

    # left
    h1 = 0
    xx = x - 1
    while xx >= 0:
        hx = int(ll[y][xx])
        h1 += 1
        if hx >= hh:
            break
        xx -= 1

    # right
    h2 = 0
    xx = x + 1
    while xx < width:
        hx = int(ll[y][xx])
        h2 += 1
        if hx >= hh:
            break
        xx += 1

    # up
    h3 = 0
    yy = y - 1
    while yy >= 0:
        hx = int(ll[yy][x])
        h3 += 1
        if hx >= hh:
            break
        yy -= 1

    # down
    h4 = 0
    yy = y + 1
    while yy < height:
        hx = int(ll[yy][x])
        h4 += 1
        if hx >= hh:
            break
        yy += 1

    return h1 * h2 * h3 * h4

def visible_tree_count():
    result = 0
    width = len(ll[0])
    height = len(ll)
    trees_solved = []
    scenic_scores = []
    for yy in range(height):
        trees_solved.append([])
        scenic_scores.append([])
        for xx in range(width):
            trees_solved[yy].append(False)
            scenic_scores[yy].append(calc_scenic_score(xx, yy))

    # from left -> right
    for yy in range(1, height-1):
        last_tree = int(ll[yy][0])
        for xx in range(1, width-1):
            curr_tree = int(ll[yy][xx])
            if curr_tree > last_tree and trees_solved[yy][xx] == False:
                result += 1
                trees_solved[yy][xx] = True
            last_tree = max(last_tree, curr_tree)

    # from right -> left
    for yy in range(1, height-1):
        last_tree = int(ll[yy][width-1])
        for xx in range(1, width-1):
            curr_tree = int(ll[yy][-xx-1])
            if curr_tree > last_tree and trees_solved[yy][-xx-1] == False:
                result += 1
                trees_solved[yy][-xx-1] = True
            last_tree = max(last_tree, curr_tree)

    # from top -> bottom
    for xx in range(1, width-1):
        last_tree = int(ll[0][xx])
        for yy in range(1, height-1):
            curr_tree = int(ll[yy][xx])
            if curr_tree > last_tree and trees_solved[yy][xx] == False:
                result += 1
                trees_solved[yy][xx] = True
            last_tree = max(last_tree, curr_tree)

    # from bottom -> top
    for xx in range(1, width-1):
        last_tree = int(ll[height-1][xx])
        for yy in range(1, height-1):
            curr_tree = int(ll[-yy-1][xx])
            if curr_tree > last_tree and trees_solved[-yy-1][xx] == False:
                result += 1
                trees_solved[-yy-1][xx] = True
            last_tree = max(last_tree, curr_tree)

    count = 0
    for i in range(1, height-1):
        for j in range(1, width-1):
            if trees_solved[i][j]:
                count += 1
    max_scenic_score = -1
    for i in range(len(scenic_scores)):
        for j in range(len(scenic_scores[i])):
            max_scenic_score = max(max_scenic_score, scenic_scores[i][j])
    print("max scenic score = " + str(max_scenic_score))
    return count + width + width + height + height - 4

print("visible tree count = " + str(visible_tree_count()))
