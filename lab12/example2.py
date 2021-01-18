def search(x, nums):
	if len(nums) == 0:
		return -1
	mid = len(nums)//2
	item = nums[mid]
	if item == x:
		return mid
	elif x < item:
		return search(x, nums[:mid])
	else:
		loc = search(x, nums[mid+1:])
		if loc == -1:
			return loc
		else:
			loc = loc + mid + 1
			return loc

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(search(8, nums))
