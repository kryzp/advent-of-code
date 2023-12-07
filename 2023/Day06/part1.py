import itertools

# not sure why my brain shut down for so long for this one :/
# i thought there was some clever trick but you can just try all possibilities lmao

ll = [x for x in open("input.txt").read().strip().split("\n")]

times = [int(x) for x in ll[0].split(" ")[1:] if x != '']
distances = [int(x) for x in ll[1].split(" ")[1:] if x != '']

x = 1

def n_beat_record(time, dist):
	n = 0
	last = False
	for possible_time in range(time + 1):
		held_down = time - possible_time
		distance_travelled = possible_time * held_down
		if distance_travelled > dist:
			n += 1
			last = True
		elif last:
			break
	return n

for i in range(len(times)):
	time = times[i]
	dist = distances[i]
	x *= n_beat_record(time, dist)

print(x)
