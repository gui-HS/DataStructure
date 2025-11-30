import heapq
from grafo import *
from random import randint
from queue import PriorityQueue
import time
from pympler import asizeof

# Estrutura de dados para conjuntos, porque python não tem identificadores neles (bruh)
# Passei a lista de vértices direto, pois python é paia e estou 0% paciência
class RealSet:
    def __init__(self, G):
        self.G = G
        self.V = self.G.listaVertices
        self.p = {} 
        self.rank = {}
        self.id = 0

    def makeSet(self):
        for x in self.V:
            self.p[x] = x
            self.rank[x] = 0

    def union(self, x, y):
        self.link(self.find_set(x), self.find_set(y))

    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]

class Kruskal:
    def __init__(self, G):
        self.G = G
        self.V = self.G.listaVertices
        self.E = self.G.listaAresta

    def kruskal(self, G):
        # Inicialização do grafo
        self.G = G

        # Inicialização da árvore
        A = [] # Conjunto de arestas que formar a árvore geradora mínima

        # Inicialização dos conjuntos. Talvez não a mais bela
        realSet1 = RealSet(self.G)
        realSet1.makeSet()

        # Ordenação das arestas
        # heapq._heapify_max(self.E)

        ordenado = sorted(self.E) # Muito mais simples do que usar heap, meu deus

        # Loop principal 
        for aresta in ordenado: 
            u = aresta.getV1()
            v = aresta.getV2()
            uRep = realSet1.find_set(u)
            vRep = realSet1.find_set(v)
            if uRep != vRep:
                A.append(aresta) #Cria uma tupla
                realSet1.union(u,v)

        
        print(f"Vértices: {len(self.V)}, Arestas disponíveis: {len(self.E)}, e retornou {len(A)} arestas")
        return A    

class Prim:
    def __init__(self, G):
        self.A = None
        self.G = G
        self.Q = PriorityQueue()
        self.V = self.G.listaVertices

    def prim(self):
        # Inicialização
        for u in self.V:
            u.d = float('inf')
        # Inicialização do vértice raiz
        self.V[0].d = 0 # Nota: no algoritmo é chamado de chave, é o custo mínimo atual parar conectar v à árvote
        self.V[0].roteamento = None

        # Inicialização da fila de prioridades
        self.Q = [x for x in self.V]
        heapq.heapify(self.Q)

        # Laço principal
        while self.Q:
            u = heapq.heappop(self.Q)
            for v in u.adjV():
                if self.G.adjV2(u, v): # Um if adicional ao pseudo código, para verificar se aresta existe primeiro
                    custoAresta = self.G.adjV2(u, v).getValor()
                    if (v in self.Q) and (custoAresta < v.d):
                        v.roteamento = u
                        v.d = custoAresta
                        heapq.heapify(self.Q)
    

def test():
    #Teste com grafo euleriano para comparação
    grafo2 = Grafo()
    for _ in range(6):
        grafo2.insereV()

    #Criar arestas
    vertices = grafo2.listaVertices
    grafo2.insereA(vertices[0], vertices[1])
    grafo2.insereA(vertices[1], vertices[2])
    grafo2.insereA(vertices[2], vertices[3])
    grafo2.insereA(vertices[3], vertices[4])
    grafo2.insereA(vertices[4], vertices[5])
    # Atribuir valores aos vértices e arestas
    for vertice in grafo2.listaVertices:
        vertice.d = randint(0, 15)
    for aresta in grafo2.listaAresta:
        aresta.setValor(randint(0,5))
    kruskal = Kruskal(grafo2)
    inicio1 = time.time()
    A = kruskal.kruskal(kruskal.G)
    fim1 = time.time()

    prim = Prim(grafo2)
    inicio2 = time.time()
    prim.prim()
    fim2 = time.time()

    # Tentativa de imprimir a árvore
    for aresta in A:
        print(aresta.getValor())

    print("-"*5 + " Nome " + "-"*5 + " Pai " + "-"*10 + " Peso ")
    for vertice in prim.V:
        if vertice.roteamento:
            pai = vertice.roteamento.nome
        else:
            pai = None
        print(" "*5, vertice.nome, " "*5, pai, " "*10, vertice.d)

    """
    Análise final:

        Prim foi fácil de implementar (apesar de umas desventuras)

        Kruskal me deu câimbra e dor de cabeça
    
    Análise de velocidade e memória:
    """
    print("      Velocidade    Memória       Custo da árvore")
    print("Kruskal: {:.4f},     {:.4f}B          {}".format(fim1-inicio1, asizeof.asizeof(kruskal), sum(vertice.getValor() for vertice in A)))
    print("Prim:    {:.4f},     {:.4f}B          {}".format(fim2 - inicio2, asizeof.asizeof(prim), sum(vertice.d for vertice in prim.V)))


test()