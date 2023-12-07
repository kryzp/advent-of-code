import functools

ll = [x for x in open("input.txt").read().strip().split("\n")]

strength = "AKQT98765432J"[::-1]
cards = []

def calc_card_n(card, nn):
	ordering = -1
	jokers = 0
	ccs = {}
	for c in card:
		if c not in ccs:
			ccs[c] = 0
		ccs[c] += 1 if c != 'J' else 0
		jokers += 1 if c == 'J' else 0
	cc = sorted(ccs.values())[::-1]
	if cc[0] + jokers == 5:
		# five of a kind
		ordering = 6
	elif cc[0] + jokers == 4:
		# four of a kind
		ordering = 5
	elif (cc[0] + jokers == 3 and cc[1] == 2) or (cc[0] == 3 and cc[1] + jokers == 2):
		# full house
		ordering = 4
	elif (cc[0] + jokers == 3):
		# three of a kind
		ordering = 3
	elif (cc[0] + jokers == 2 and cc[1] == 2) or (cc[0] == 2 and cc[1] + jokers == 2):
		# two pair
		ordering = 2
	elif (cc[0] + jokers == 2):
		# one pair
		ordering = 1
	else:
		# high card
		ordering = 0
	return (ordering, nn, card)

for l in ll:
	card = l.split(" ")[0]
	nn = int(l.split(" ")[1])
	cards.append(calc_card_n(card, nn))

def comparison_function(card0, card1):
	if card0[0] > card1[0]:
		return 1
	elif card0[0] < card1[0]:
		return -1
	for i in range(len(card0[2])):
		ch0 = card0[2][i]
		ch1 = card1[2][i]
		if strength.index(ch0) > strength.index(ch1):
			return 1
		elif strength.index(ch0) < strength.index(ch1):
			return -1

total = 0
cards = sorted(cards, key=functools.cmp_to_key(comparison_function))

for i, c in enumerate(cards):
	total += (i + 1) * c[1]

print(total)
