import numpy as np

ll = [x for x in open("input.txt").read().strip().split("\n")]

hailstones = []

for l in ll:
	spl = l.split(" @ ")
	position = [int(x) for x in spl[0].split(", ")]
	velocity = [int(x) for x in spl[1].split(", ")]
	hailstones.append((position, velocity))

MIN_POS = 200000000000000
MAX_POS = 400000000000000

seen = set()

intersections = 0

for i in range(len(hailstones)):
	for j in range(len(hailstones)):
		if i == j:
			continue
		if (i, j) in seen or (j, i) in seen:
			continue
		seen.add((i, j))
		pax, pay, paz = hailstones[i][0]
		vax, vay, vaz = hailstones[i][1]
		pbx, pby, pbz = hailstones[j][0]
		vbx, vby, vbz = hailstones[j][1]
		ma = vay / vax
		mb = vby / vbx
		mat = np.matrix([[1/ma, -1], [1/mb, -1]])
		det = np.linalg.det(mat)
		if abs(det) < 0.0001:
			continue
		result_matrix = mat.getI() * np.matrix([[pay/ma - pax], [pby/mb - pbx]])
		ipx = result_matrix[1, 0]
		ipy = result_matrix[0, 0]
		crossed_in_past_a = np.dot(np.array([ipx - pax, ipy - pay]), np.array([vax, vay])) < 0.0
		crossed_in_past_b = np.dot(np.array([ipx - pbx, ipy - pby]), np.array([vbx, vby])) < 0.0
		crossed_in_past = crossed_in_past_a or crossed_in_past_b
		inside_test_area = ipx >= MIN_POS and ipx <= MAX_POS and ipy >= MIN_POS and ipy <= MAX_POS
		if inside_test_area and not crossed_in_past:
			intersections += 1

print(intersections)
