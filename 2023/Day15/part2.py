
ll = [x for x in open("input.txt").read().strip().split(",")]

def hashof(l):
	ret = 0
	for c in l:
		ret += ord(c)
		ret = (ret * 17) % 256
	return ret

seen = set()
boxes = []

for _ in range(256):
	boxes.append([])

for l in ll:
	if '=' in l:
		label = l.split("=")[0]
		focal_length = int(l.split("=")[1])
		idx = hashof(label) % len(boxes)
		box = boxes[idx]
		found = False
		for entry in box:
			if entry[0] == label:
				entry[1] = focal_length
				found = True
				break
		if not found:
			boxes[idx].append([label, focal_length])
		seen.add(label)
	elif '-' in l:
		label = l[:-1]
		idx = hashof(label) % len(boxes)
		entryidx = -1
		for i, entry in enumerate(boxes[idx]):
			if entry[0] == label:
				entryidx = i
				break
		if entryidx != -1:
			boxes[idx].pop(entryidx)
			seen.remove(label)

x = 0

for lens in seen:
	box = -1
	slot = -1
	foc = -1
	for i, b in enumerate(boxes):
		for j, elem in enumerate(b):
			if elem[0] == lens:
				box = i
				slot = j
				foc = elem[1]
				break
		if box != -1:
			break
	x += (box + 1) * (slot + 1) * foc

print(x)
