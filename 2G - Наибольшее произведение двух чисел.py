numbers = [1,2,3,4,5,5,7,7,-1,-2]

def find_max_mult(numbers):
	
	max1 = max(numbers)
	numbers2 = numbers.copy()
	numbers2.remove(max1)
	max2 = max(numbers2)
	
	min1 = min(numbers)
	numbers2 = numbers.copy()
	numbers2.remove(min1)
	min2 = min(numbers2)
	
	if max1*max2 > min1*min2:
		return max1, max2
	else:
		return min1, min2 
	
print(find_max_mult(numbers))