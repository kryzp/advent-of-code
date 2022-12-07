import itertools as it

ll = [x for x in open("input.txt").read().strip().split("\n")]

current_line = 0
counter = 0
comparable = 999999999999999999

def calc_dir_size() -> int:
	global current_line
	global counter
	global comparable
	total_size = 0
	while current_line < len(ll):
		l = ll[current_line]
		if l.startswith("$ cd .."):
			current_line += 1
			return total_size
		elif l.startswith("$ cd /"):
			current_line += 1
			continue
		elif l.startswith("$ cd ") :
			current_line += 1
			size = calc_dir_size()
			if size >= (30000000 - (70000000 - 48008081)) and size < comparable:
				comparable = size
			total_size += size
			if size <= 100000:
				counter += size
			continue
		elif l.startswith("dir") or l.startswith("$ ls"):
			current_line += 1
			continue
		else:
			size = int(l.split(" ")[0])
			total_size += size
			current_line += 1
	return total_size

print("total = " + str(calc_dir_size()))
print("counter = " + str(counter))
print("comparable = " + str(comparable))
