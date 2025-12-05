class Vertice:
    def __init__(self, nome):
        self.aresta = list()  # Lista de arestas conectadas ao vetor
        self.nome = nome
        self.next = None  # Refência ao próximo vetor
        self.cor = None  # BRANCO (On), CINZA (On operation), PRETO (off)
        self.caminho = None  # Caminho de vértices
        self.d = None  # Distância
        self.roteamento = None  # Vértice Pai
        self.abertura = None  # Tempo até abertura do vértice
        self.fechamento = None  # Tempo até fechamento do vértice
        self.eulerEdge = None
        
    # Estrutura para criação de heap, 
    # utilizado no arquivo de caminhos mínimos
    def __lt__(self, other):
        return self.d < other.d
    
    def setEulerEdge(self, aresta):
        self.eulerEdge = aresta

    def getEulerEdge(self):
        return self.eulerEdge

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def addAdjacente(self, aresta):
        self.aresta.append(aresta)

    def lenAresta(self):
        return len(self.aresta)

    def getAresta(self):
        return self.aresta

    def adj(self):
        return self.aresta

    def adjV(self):
        setV = set()
        for i in self.aresta:
            v1 = i.getV1()
            v2 = i.getV2()

            if v1 != self:
                setV.add(v1)
            if v2 != self:
                setV.add(v2)
        return setV
    
    def grauCor(self):
        verticesAdj = self.adjV()
        coresAdj = set()
        for vertices in verticesAdj:
            if vertices.cor != None:
                coresAdj.add(vertices.cor)
        if len(coresAdj) == 0:
            return 0
        else:
            return len(coresAdj)
        
    def listaCores(self):
        verticesAdj = self.adjV()
        coresAdj = set()
        for vertices in verticesAdj:
            if vertices.cor != None:
                coresAdj.add(vertices.cor)
        coresAdj = [x for x in coresAdj]
        coresAdj.sort()
        if len(coresAdj) == 0:
            return []
        else:
            return coresAdj