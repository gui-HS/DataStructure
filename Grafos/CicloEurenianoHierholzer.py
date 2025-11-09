from arestaDP import ArestaDP
from grafo import Grafo
# from aresta import Aresta


class Hierholzer:
    def __init__(self, G):
        self.H = G  # Graph
        self.Vvisit = list()  # List of visited vertices
        self.nVvisit = 0
        self.k = 0  # Number of vertices visited, closed and open

    def HierholzerAlgorithm(self, s):
        # Inicialização
        self.Vvisit = [None] * len(self.H.listaVertices)
        self.Vvisit[0] = s
        self.nVvisit = 0
        self.k = 0
        # e0 = e1 = e2 = e3 = Aresta()
        e2 = e3 = ArestaDP()

        while self.k <= self.nVvisit:
            u = self.Vvisit[self.k]
            while u.aresta is not None:
                e0 = u.aresta[0]  # Recebe a primeira aresta incidente a u
                v = e0.theOtherOne(u)
                self.H.removeA(e0)
                e1 = e0
                while v != u:
                    if v not in self.Vvisit:
                        self.nVvisit += 1
                        self.Vvisit[self.nVvisit] = v
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
                    e1.setEulerEdge(u)
                    e2.setPrevEdge(e1)
                    e3.setPrevEdge(e0)
                    e2.setNextEdge(e0)
                    e3.setNextEdge(e1)
            self.k += 1
        if self.k > 1:
            print("Não euleriano")


def testeGrafo():
    grafo1 = Grafo()
    for _ in range(6):
        grafo1.insereV()

    for i in range(5):
        grafo1.insereA(grafo1.listaVertices[i], grafo1.listaVertices[i + 1])

    grafo2 = Hierholzer(grafo1)
    grafo2.HierholzerAlgorithm(grafo2.H.listaVertices[0])


testeGrafo()

