
ll = [x for x in open("input.txt").read().strip().split("\n")]

x = [0] * len(ll)

deck = ll

while deck:
	new_deck = []
	for l in deck:
		spl = l.split(": ")
		curr_card_id = int(spl[0].split("ard")[1])
		spl2 = spl[1].split(" | ")
		winning = set()
		for m in spl2[0].split(" "):
			if m != "":
				winning.add(int(m.strip()))
		mine = set()
		for p in spl2[1].split(" "):
			if p != "":
				mine.add(int(p.strip()))
		won_cards = winning.intersection(mine)
		for card in range(len(won_cards)):
			x[curr_card_id + card - 1] += 1
			new_deck.append(ll[curr_card_id + card])
	deck = new_deck

print(len(ll) + sum(x))
