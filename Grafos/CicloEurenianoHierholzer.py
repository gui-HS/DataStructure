from arestaDP import ArestaDP
from grafo import Grafo

class Hierholzer:
    def __init__(self, G):
        self.H = G  # Grafo
        self.Vvisit = list()  # Lista de vértices visitados
        self.nVvisit = 0
        self.k = 0  # Número de vértices visitados, fechados e aberto

    def HierholzerAlgorithm(self, s):
        # Inicialização
        self.Vvisit = [s]
        self.nVvisit = 1
        self.k = 0
        e2 = e3 = ArestaDP()

        while self.k < self.nVvisit:
            u = self.Vvisit[self.k]
            while u.aresta:
                e0 = u.aresta[0]  # Recebe a primeira aresta incidente a u
                v = e0.theOtherOne(u)
                self.H.removeA(e0)
                e1 = e0
                while v != u:
                    if v not in self.Vvisit:
                        self.Vvisit.append(v) # No pseudo código tá diferente, mas só assim funcionou
                        self.nVvisit += 1
                    
                    if not v.aresta: #Para evitar o erro de list index out of range
                        break

                    e2 = v.aresta[0]
                    e2.setNextEdge(e1)
                    e1.setPrevEdge(e2)
                    if v.getEulerEdge() is not None:
                        v.setEulerEdge(e2)
                    e1 = e2
                    v = e1.theOtherOne(u)
                    self.H.removeA(e1)

                # Um subciclo em u acabou de ser completado
                e0.setPrevEdge(e1)
                e1.setNextEdge(e0)

                if u.getEulerEdge():
                    u.setEulerEdge(e0)
                else:
                    # Insere um novo subciclo preexistente em u
                    e1 = u.getEulerEdge()
                    e2.setPrevEdge(e1)
                    e3.setPrevEdge(e0)
                    e2.setNextEdge(e0)
                    e3.setNextEdge(e1)
            self.k += 1
            
        # Condição para saber se ciclo é euleriano
        if len(self.H.listaAresta) > 0:
            return "Ciclo não euleriano"
        else: return "Ciclo euleriano"

def testeGrafo():
    #Grafo com 2 vértices de grau ímpar
    grafo1 = Grafo()
    for _ in range(4):
        grafo1.insereV()
    
    vertices = grafo1.listaVertices
    # Criar grafo: 0-1-2-3 (caminho simples)
    grafo1.insereA(vertices[0], vertices[1])
    grafo1.insereA(vertices[1], vertices[2])
    grafo1.insereA(vertices[2], vertices[3])

    hierholzer = Hierholzer(grafo1)
    hierholzer.HierholzerAlgorithm(vertices[0])
    
    print(f"{hierholzer.HierholzerAlgorithm(vertices[0])}, {grafo1.getOrdem()} vértices, {grafo1.getTamanho()} arestas")

def testeGrafoEuleriano():
    #Teste com grafo euleriano para comparação
    grafo2 = Grafo()
    for _ in range(4):
        grafo2.insereV()
    
    vertices = grafo2.listaVertices
    # Ciclo: 0-1-2-3-0 (EULERIANO)
    grafo2.insereA(vertices[0], vertices[1])
    grafo2.insereA(vertices[1], vertices[2])
    grafo2.insereA(vertices[2], vertices[3])
    grafo2.insereA(vertices[3], vertices[0])

    hierholzer = Hierholzer(grafo2)
    
    print(f"{hierholzer.HierholzerAlgorithm(vertices[0])}, {grafo2.getOrdem()} vértices, {grafo2.getTamanho()} arestas")

# Testes
testeGrafo()
testeGrafoEuleriano()