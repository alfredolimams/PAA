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
		edges.append( (e[1],e[2]) )
		tree[ e[1] ][ e[2] ] = e[0]
		tree[ e[2] ][ e[1] ] = e[0]
        '''                                 '''
		for v in graph[ e[1] ]:
			if v not in vstd:
				q.put( (graph[ e[1] ][v] , v , e[1] ) )

	return cost , tree , edges

def dfs( graph , v , id , color, connected ):
	color[v] = id
	connected[id].append( v )
	for u in graph[v] :
		if u not in color:
			dfs( graph , u , id , color, connected )

def secondTree( tree , graph, edges ):

	cst = 2**20
	edges.sort()
	for e in edges :
        '''
            Removendo uma aresta da MST, perceba tinhamos um conjunto,
        quando removemos qualquer aresta, ficamos com dois componentes conectados.
        '''
		w = graph[ e[0] ][ e[1] ]
		del tree[ e[0] ][ e[1] ]
		del tree[ e[1] ][ e[0] ]
		color = {}
		connected = []
        '''
            Construcao dos componentes conectados
        '''
		for i in range(2):
			connected.append( [] )
			dfs( tree , e[i] , i , color , connected )
		
        '''
            Perceba que precisamos adicionar uma aresta de um componente conectado
        ao outro, assim tornando-os novamente um grupo só.         
        '''

		for u in connected[0]:
			for v in connected[1]:
				if u in graph[v]:
					if graph[u][v] - w:
						cst = min( graph[u][v] - w , cst )
        '''
            Encontro a menor custo de troca das arestas
        '''
		tree[ e[0] ][ e[1] ] = w
		tree[ e[1] ][ e[0] ] = w

	return cst

def main():
	qt_vertex , qt_edges = map( int , input().split() )
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
	print( "First Spanning Tree Cost" , cost )
	costMore = secondTree( tree , graph , edges )
	print( "Second Spanning Tree Cost:" , cost + costMore )

main()
