ll = [x for x in open("input.txt").read().strip().split("\n")]

def visible_tree_count():
    result = 0
    width = len(ll[0])
    height = len(ll)
    trees_solved = []
    for yy in range(height):
        trees_solved.append([])
        for xx in range(width):
            trees_solved[yy].append(False)
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
    return count + width + width + height + height - 4

print(visible_tree_count())
