
segtree = {}

def build( segtree, values ):
	
	size = len(values)

	for i in range(size):
		segtree[ size + i ] = values[i]

	for i in range(size-1, 0, -1):
		segtree[i] = max(segtree[ i<<1 ] , segtree[ i<<1 | 1 ])

def query( left, right , segtree , values ):
	
	value = 0
	size = len(values)

	left += size
	right += size

	while left < right:
		if left&1:
			value = max( value , segtree[left] )
			left += 1
		if right&1:
			right -= 1
			value = max( value , segtree[right] )
		left = left//2
		right = right//2
	return value


v = []

answer = 0

n = int(input())

for i in range(n):
	v.append( int(input()) )

build( segtree , v )


for i in range(1,n-1):
	if v[i] < min( query(0,i,segtree,v) , query(i+1,n,segtree,v) ):
		answer += 1

print(answer)
