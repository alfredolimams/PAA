def cut(heights, value):
	answer = 0
	for h in heights:
		h = h - value
		if h > 0:
			answer += h
	return answer

def binarySearchIterative(heights, value, total):
	begin = 0
	end = max(heights)
	mid = -1
	#print( "IN:", begin , end )
	while end-begin > 1E-5:
		mid = (begin+end)/2
		c = cut(heights,mid)
		#print("run", mid, c)
		if c == height or (total-c) == height:
			return mid
		if c < value:
			end = mid
		else:
			begin = mid
	return mid

def binarySearchRecursive(heights, begin, end, height, total):
	if end-begin > 1E-5:
		mid = (begin+end)/2
		c = cut(heights,mid)
		if c == height :#or (total-c) == height:
			return mid
		if c < height:
			return binarySearchRecursive(heights,begin,mid,height, total)
		else:
			return binarySearchRecursive(heights,mid,end,height, total)
	return (begin+end)/2

while True:
	qt, height = map(int,input().split())
	#print (qt, height)
	if qt == height and qt == 0:
		break
	heights = list( map(int,input().split()) )
	total = sum(heights)
	if height > total:
		print("-.-")
	elif total == height or height == 0:
		print(":D")
	else:
		#print( "%.4f" % (binarySearchIterative(heights,height,total)) )
		print( "%.4f" % (binarySearchRecursive(heights,0,max(heights),height,total)) )
		pass
	pass
