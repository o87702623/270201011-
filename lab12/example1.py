def selsort(nums):  
	n = len(nums)

	for bottom in range(n-1):
		mp = bottom    
		for i in range(botttom + 1, n): 
			if nums[i] < nums[mp]:		 
				mp = i                  

		nums[bottom], nums[mp] = nums[mp], nums[bottom] 

print(selsort([4,5,8,2,6,1,9,3,7,10]))