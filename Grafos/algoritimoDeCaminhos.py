import heapq
from grafo import *
import random
from pympler import asizeof
import time

class Dijkstra:
    def __init__(self, G):
        self.G = G

    # O algoritmo de Dijkstra serve para encontrar o caminho mínimo
    # de um vértice até outro de um gráfico

    def initialize_Single_Source(self, s):
        for v in self.G.listaVertices:
            v.d = float('inf') #numero infinito, dah
            v.roteamento = None
        s.d = 0

        # Verificar se não há valores negativos ou nulos
        v = [x for x in self.G.listaVertices if x.d == None or x.d < 0]
        a = [x for x in self.G.listaAresta if x.getValor() == None or x.getValor() < 0]
        if (a or v):
            raise ValueError(f"Vértices ou arestas com valores negativos ou nulos!")
    
    def custo(self, u, v): # chamado de w, no pseudo código
        if self.G.adjV2(u,v):
            return self.G.adjV2(u,v).getValor()
        else:
            return float('inf')

    def relax(self, u, v):
        if v.d > u.d + self.custo(u,v):
            v.d = u.d + self.custo(u,v)
            v.roteamento = u

    def dijkstra(self, w, s):
        self.initialize_Single_Source(s)
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

class FloydWarshall:
    def __init__(self, G):
         self.G = G # Grafo
         self.d = [] # Matriz de distância, armazena a distância mínima de i para j 
         self.V = self.G.listaVertices # Lista de vértices 
         self.n = len(self.G.listaVertices) # Número de vértices
         self.W = [[0] * self.n for _ in range(self.n)] # Matriz de custo inicial    
         self.d = [[0] * self.n for _ in range(self.n)] # Matriz de distância, armazena a distância mínima de i para j
         self.roteamento = [[0] * self.n for _ in range(self.n)] # Matriz de roteamento, contém o pai dos vértices

    def montarW(self):
        # Essa vai ser a matriz W, de custo inicial
        for i in range(self.n):
            u = self.V[i]
            for j in range(self.n):
                v = self.V[j]
                aresta = self.G.adjV2(u, v) # Retorna a aresta entre os vértices i e j, se existir
                if i == j:
                    self.W[i][j] = 0
                else:
                    if aresta:
                        self.W[i][j] = aresta.getValor()
                    else:
                        self.W[i][j] = float('inf')

        # Iniciar matriz de roteamento:
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.W[i][j] < float('inf'):
                    self.roteamento[i][j] = i
                else:
                    self.roteamento[i][j] = None

    def floydWarshall(self):
        # Inicialição 
        # Essa parte serve para montar a matriz de custo inicial, utilizando vértices adjacentes
        self.montarW()

        # Custo inicial 
        self.d = [linha[:] for linha in self.W]

        for k in range(self.n):
            # O pseudo código usa a matriz anterior, então vamos armazená-la
            custoAnterior = self.d
            roteamentoAnterior = self.roteamento

            for i in range(self.n):
                for j in range(self.n):
                    if custoAnterior[i][k] + custoAnterior[k][j] < custoAnterior[i][j]:
                        self.d[i][j] = custoAnterior[i][k] + custoAnterior[k][j]
                        self.roteamento[i][j] = roteamentoAnterior[k][j]
                    else:
                        self.d[i][j] = custoAnterior[i][j]
                        self.roteamento[i][j] = roteamentoAnterior[i][j]
        return self.roteamento, self.d
    
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
    grafo2.insereA(vertices[0], vertices[5])
    grafo2.insereA(vertices[2], vertices[5])
    grafo2.insereA(vertices[1], vertices[5])
    grafo2.insereA(vertices[0], vertices[4])
    grafo2.insereA(vertices[0], vertices[3])
    grafo2.insereA(vertices[0], vertices[2])
    # Atribuir valores aos vértices e arestas
    for vertice in grafo2.listaVertices:
        vertice.d = random.randint(0, 15)
    for aresta in grafo2.listaAresta:
        aresta.setValor(random.randint(0,5))
        
    grafoDijkstra = Dijkstra(grafo2)
    grafoFloyd = FloydWarshall(grafo2)
    #print(grafoDijkstra.dijkstra(grafo2.listaVertices[0], grafo2.listaVertices[3]))
    #print(grafoFloyd.montarW())
    grafoFloyd.floydWarshall()
    print("Distância matriz de custo inicial")
    for coluna in grafoFloyd.W: 
        print(coluna)
    print("\nDistância matriz final")
    for coluna in grafoFloyd.d: 
        print(coluna)
    print("\nMatriz de roteamento")
    for coluna in grafoFloyd.roteamento:
        print(coluna)

    # Agora, vamos fazer uma comparação de memória, criando duas matrizes comicamente grandes C:
    grafo4 = Grafo()
    for _ in range(1000):
        grafo4.insereV()

    vertices4 = grafo4.listaVertices 
    for i in range(999):
        grafo4.insereA(vertices4[i], vertices4[i+1]) 
    
    for vertices in grafo4.listaVertices:
        vertice.d = random.randint(0, 15)
    for aresta in grafo4.listaAresta:
        aresta.setValor(random.randint(0,5)) 

    #Dijkstra
    inicio1 = time.time() 
    grafoDijkstra4 = Dijkstra(grafo4)
    grafoDijkstra4.dijkstra(vertices4[0], vertices4[999])
    fim1 = time.time()

    #Floyd
    inicio2 = time.time()
    grafoFloyd4 = FloydWarshall(grafo4)
    grafoFloyd4.floydWarshall()
    fim2 = time.time()
    print("\n"+"-"*10, "Memória", "-"*10)
    print("Dijkstra: ", asizeof.asizeof(grafoDijkstra4), "B", "Floy: ", asizeof.asizeof(grafoFloyd4), "B")
    print("\n"+"-"*10, "Tempo", "-"*10) 
    print("Dijkstra: ", fim1 - inicio1, "B", "Floy: ", fim2 - inicio2, "B")
test()   