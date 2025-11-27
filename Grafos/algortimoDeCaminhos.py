import heapq
from grafo import *
import random

class Dijkstra:
    def __init__(self, G):
        self.G = G

    # O algoritmo de Dijkstra serve para encontrar o caminho mínimo
    # de um vértice até outro de um gráfico

    def initialize_Single_Source(self, G, s):
        for v in self.G.listaVertices:
            v.d = float('inf') #numero infinito
            v.roteamento = None
        s.d = 0

        # Verificar se não há valores negativos ou nulos
        v = [x for x in self.G.listaVertices if x.d == None or x.d < 0]
        a = [x for x in self.G.listaAresta if x.getValor() == None or x.getValor() < 0]
        if (a or v):
            raise ValueError(f"Vértices ou arestas com valores negativos ou nulos!")
    
    def custo(self, u, v): #chamado de w, no pseudo código
        if self.G.adjV2(u,v):
            return self.G.adjV2(u,v).getValor()
        else:
            return float('inf')

    def relax(self, u, v):
        if v.d > u.d + self.custo(u,v):
            v.d = u.d + self.custo(u,v)
            v.roteamento = u

    def dijkstra(self, G, w, s):
        self.initialize_Single_Source(G, s)
        S = [] #conjunto dos vértices cujo caminho mínimo já foi calculado
        Q = self.G.listaVertices #fila de prioridades mínimas de vértices (o vértice com menor valor de d[v] tem prioridade para sair da fila)
        heapq.heapify(Q) #Ordenar em heap
        while Q:
            u = heapq.heappop(Q) #Utilizar heap para extraír mínimo
            S.append(u)
            for v in u.adjV():
                self.relax(u, v)
        return self.printDijkstra(w,s)

    def printDijkstra(self, w, s):
        return "A distância do vértice {} até o vértice {} é de: {}".format(w.nome, s.nome, w.d)

def test():
    #Teste com grafo euleriano para comparação
    grafo2 = Grafo()
    for _ in range(4):
        grafo2.insereV()
    
    #Criar arestas
    vertices = grafo2.listaVertices
    grafo2.insereA(vertices[0], vertices[1])
    grafo2.insereA(vertices[1], vertices[2])
    grafo2.insereA(vertices[2], vertices[3])
    grafo2.insereA(vertices[3], vertices[0])
    
    # Atribuir valores aos vértices e arestas
    for vertice in grafo2.listaVertices:
        vertice.d = random.randint(0, 5)
    for aresta in grafo2.listaAresta:
        aresta.setValor(random.randint(0,5))
        
    grafoDijkstra = Dijkstra(grafo2)
    print(grafoDijkstra.dijkstra(grafo2, grafo2.listaVertices[0], grafo2.listaVertices[2]))
test()