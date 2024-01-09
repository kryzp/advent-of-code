
ll = [x for x in open("input.txt").read().strip().split("\n")]

x = 0

def find_arrangements(data, nums, streak):
	if streak > 0 and len(nums) == 0:
		return 0

	if data == "":
		if (len(nums) == 0 and streak == 0) or (len(nums) == 1 and streak == nums[0]):
			return 1
		return 0

	upcoming_spaces = 0
	for c in data:
		if c == "#" or c == "?":
			upcoming_spaces += 1
	
	if upcoming_spaces + streak < sum(nums):
		return 0
	
	chere = data[0]
	arrangements = 0

	if chere in ["?", "."] and len(nums) > 0 and streak == nums[0]:
		# fully completed one streak, start over
		arrangements += find_arrangements(data[1:], nums[1:], 0)
	
	if chere == "." and streak > 0 and streak != nums[0]:
		# abort this branch, not enough room
		return 0

	if chere in ["?", "#"]:
		# continue moving on
		arrangements += find_arrangements(data[1:], nums, streak + 1)

	if chere in ["?", "."] and streak == 0:
		# start a new branch
		arrangements += find_arrangements(data[1:], nums, 0)

	return arrangements

for l in ll:
	data, numsstr = l.split(" ")
	nums = [int(x) for x in numsstr.split(",")]
	x += find_arrangements(data, nums, 0)

print(x)
