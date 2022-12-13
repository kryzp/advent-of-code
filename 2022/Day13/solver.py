import functools as ft

ll = [x for x in open("input.txt").read().strip().split("\n")]

class TreeNode:
	def __init__(self):
		self.value: int = -1
		self.nodes: list[TreeNode] = []

	@classmethod
	def from_value(cls, val):
		result = cls()
		result.value = val
		result.nodes = []
		return result

	def size(self):
		return len(self.nodes)

	def is_leaf(self) -> bool:
		return len(self.nodes) == 0

	def add(self, item):
		self.nodes.append(item)

	def get(self, idx: int):
		return self.nodes[idx]

def compare_trees(tree1: TreeNode, tree2: TreeNode) -> int:
	if tree1.is_leaf() and tree2.is_leaf():
		if tree1.value > tree2.value:
			return 1
		elif tree1.value < tree2.value:
			return -1
		else:
			return 0
	elif not tree1.is_leaf() and not tree2.is_leaf():
		minimum = min(tree1.size(), tree2.size())
		for i in range(minimum):
			result = compare_trees(tree1.get(i), tree2.get(i))
			if result != 0:
				return result
		if tree1.size() > tree2.size():
			return 1
		elif tree1.size() < tree2.size():
			return -1
		else:
			return 0
	elif tree1.is_leaf():
		tmp = TreeNode()
		tmp.add(tree1)
		return compare_trees(tmp, tree2)
	elif tree2.is_leaf():
		tmp = TreeNode()
		tmp.add(tree2)
		return compare_trees(tree1, tmp)

def parse_array(raw: str, begin: int, tree: TreeNode) -> int:
	begin += 1
	end = len(raw)
	i = begin
	n = begin
	while i < end:
		ch = raw[i]
		if ch == '[':
			node = TreeNode()
			i = parse_array(raw, i, node)
			n = i
			tree.add(node)
		elif ch == ']':
			if n != i:
				tree.add(TreeNode.from_value(int(raw[n:i])))
			break
		else:
			if ch == ',':
				if n != i:
					tree.add(TreeNode.from_value(int(raw[n:i])))
				i += 1
				n = i
				continue
			i += 1
	return i + 1

def is_valid_pair(str1: str, str2: str) -> bool:
	tree1 = TreeNode()
	tree2 = TreeNode()
	parse_array(str1, 0, tree1)
	parse_array(str2, 0, tree2)
	return compare_trees(tree1, tree2) <= -1

result = 0
pair_id = 1

for i in range(0, len(ll), 3):
	str1 = ll[i]
	str2 = ll[i+1]
	correctIndex = is_valid_pair(str1, str2)
	if correctIndex:
		result += pair_id
	pair_id += 1

print("sum = " + str(result))

unsorted_list = []

for i in range(len(ll)):
	if ll[i] == "":
		continue
	node = TreeNode()
	parse_array(ll[i], 0, node)
	unsorted_list.append(node)

node_2 = TreeNode()
parse_array("[[2]]", 0, node_2)
unsorted_list.append(node_2)

node_6 = TreeNode()
parse_array("[[6]]", 0, node_6)
unsorted_list.append(node_6)

sorted_list = sorted(unsorted_list, key=ft.cmp_to_key(lambda x, y: compare_trees(x, y)))
decoder_key = (sorted_list.index(node_2) + 1) * (sorted_list.index(node_6) + 1)
print("decoder key = " + str(decoder_key))
