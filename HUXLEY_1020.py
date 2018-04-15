import queue

graph = {}

def prim( graph ):
	if len(graph) == 0 :	return
	'''
		Iniciando o grafo
	'''
	vstd = {}
	tree = {}
	edges = []
	for i in list(graph.keys()):
		v = i
		tree [i]= {}
	
	vstd[v] = True
	'''
		Colocando os elementos relacionados a v
		na fila prioridade -> ( custo , vértice )
	'''
	q = queue.PriorityQueue()
	for i in graph[v]:
		q.put( ( graph[v][i] , i, v ) )

	cost = 0
	while not q.empty() :
		e = q.get()
		if e[1] in vstd : continue
		vstd[ e[1] ] = True
		cost += e[0]
		''' Contruindo o novo grafo -> MST  '''
		edges.append( (min(e[1],e[2]),max(e[1],e[2])) )
		tree[ e[1] ][ e[2] ] = e[0]
		tree[ e[2] ][ e[1] ] = e[0]
		'''                                 '''
		for v in graph[ e[1] ]:
			if v not in vstd:
				q.put( (graph[ e[1] ][v] , v , e[1] ) )

	return cost , tree , edges

def dfs( graph , v , dist ):
	for u in graph[v] :
		if u not in dist:
			dist[u] = dist[v] + graph[v][u]
			dfs( graph , u , dist )

def main():
	qt_vertex , qt_edges, vel = map( int , input().split() )
	for i in range(qt_edges):
		u, v, w = map( int , input().split() )
		try :
			graph[u][v] = w
		except :
			graph[u] = {}
			graph[u][v] = w
		try :
			graph[v][u] = w
		except :
			graph[v] = {}
			graph[v][u] = w
	
	cost , tree , edges = prim( graph )
	edges.sort()
	dist = {}
	dist[0] = 0
	dfs( tree , 0 , dist )
	print("########################")
	print( "Minimum Cost:")
	print(cost)
	print("########################")
	print("Connections:")
	for e in edges:
		print( e[0] , e[1] )
	print("########################")
	print("Pings:")
	for i in range(1,qt_vertex):
		print("%d: %.3f" %  (i, (2*dist[i])/vel) )
	print("########################")	
main()
