import heapq
from grafo import *
import random

class Dijkstra:
    def __init__(self, G):
        self.G = G

    # O algoritmo de Dijkstra serve para encontrar o caminho mínimo
    # de um vértice até os outros de um gráfico

    def initialize_Single_Source(self, G, s):
        for v in G.listaVertices:
            v.d = "inf"
            v.roteamento = None
        s.d = 0

        #Verificar se não há valores negativos
        for a in G.listaAresta:
            try:
                if a.getValor() < 0:
                    raise TypeError
            except TypeError:
                return "valor de aresta inválido"

    def relax(self, u, v, w):
        if v.d > u.d + w(u,v):
            v.d = u.d + w(u,v)
            v.roteamento = u

    def dijkstra(self, G, w, s):
        self.initialize_Single_Source(G, s)
        S = None #conjunto dos vértices cujo caminho mínimo já foi calculado
        Q = self.G.listaVertices #fila de prioridades mínimas de vértices (o vértice com menor valor de d[v] tem prioridade para sair da fila)
        heapq.heapify(Q) #Ordenar em heap

        """while G is not None:
            u = heapq.heappop(Q) #Utilizar heap para extraír mínimo
            S.append(u)
            for v in u.adjV:
                self.relax(u, v, w)"""
        

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
    
    #Criar vértices
    for vertice in grafo2.listaVertices:
        vertice.d = random.randint(0, 5)
        
    grafoDijkstra = Dijkstra(grafo2)
    grafoDijkstra.dijkstra(grafo2, grafo2.listaVertices[0], grafo2.listaVertices[2])
test()