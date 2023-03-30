
ll = [x[::-1] for x in open("input.txt").read().strip().split("\n")]

DEC_TABLE = {
	'=': -2,
	'-': -1,
	'0': 0,
	'1': 1,
	'2': 2
}

ENC_TABLE = {
	0: '0',
	1: '1',
	2: '2',
	3: '=',
	4: '-'
}

numb10 = 0

for l in ll:
	for i in range(len(l)):
		numb10 += 5**i * DEC_TABLE[l[i]]

res = []
carry = 0

while numb10 > 0:
	n = numb10%5 + carry
	numb10 //= 5
	res.insert(0, ENC_TABLE[n%5])
	carry = 1 if n > 2 else 0

print("sum = " + "".join(res))
