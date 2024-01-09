import numpy as np

ll = [x for x in open("input.txt").read().strip().split("\n")]

hailstones = []

for l in ll:
	spl = l.split(" @ ")
	position = [int(x) for x in spl[0].split(", ")]
	velocity = [int(x) for x in spl[1].split(", ")]
	hailstones.append((position, velocity))

def get_equation(p1, q1, p2, q2, dp1, dq1, dp2, dq2):
	return (
		[dq2 - dq1, dp1 - dp2, q2 - q1, p2 - p1], # the equation (in coefficient form)
		((q1 * dp1) - (q2 * dp2)) - ((p1 * dq1) - (p2 * dq2)) # result of the equation
	)

coeffs1 = []
results1 = []

coeffs2 = []
results2 = []

def xy(t):
	return (t[0], t[1])

def xz(t):
	return (t[0], t[2])

for i in range(0, 8, 2):
	cur = hailstones[i + 0]
	nxt = hailstones[i + 1]

	cur_pos, cur_vel = cur
	nxt_pos, nxt_vel = nxt

	coeff1, res1 = get_equation(*xy(cur_pos), *xy(nxt_pos), *xy(cur_vel), *xy(nxt_vel))
	coeffs1.append(coeff1)
	results1.append(res1)

	coeff2, res2 = get_equation(*xz(cur_pos), *xz(nxt_pos), *xz(cur_vel), *xz(nxt_vel))
	coeffs2.append(coeff2)
	results2.append(res2)

mat1 = np.array(coeffs1)
col1 = np.array(results1)
ans1 = np.linalg.solve(mat1, col1)

mat2 = np.array(coeffs2)
col2 = np.array(results2)
ans2 = np.linalg.solve(mat2, col2) 

# ans1 holds the x and y coordinates of the rock
# and2 holds the x and z coordinates of the rock

px = ans1[0]
py = ans1[1]
pz = ans2[1]

result = px + py + pz
print(int(result))
