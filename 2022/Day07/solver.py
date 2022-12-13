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
		current_line += 1
		if l.startswith("dir") or l.startswith("$ ls") or l.startswith("$ cd ..") or l.startswith("$ cd /"):
			if l.startswith("$ cd .."):
				return total_size
			continue
		elif l.startswith("$ cd "):
			size = calc_dir_size()
			if size >= (30000000 - (70000000 - 48008081)) and size < comparable:
				comparable = size
			total_size += size
			if size <= 100000:
				counter += size
		else:
			local_size = int(l.split(" ")[0])
			total_size += local_size
	return total_size

print("total = " + str(calc_dir_size()))
print("counter = " + str(counter))
print("comparable = " + str(comparable))
