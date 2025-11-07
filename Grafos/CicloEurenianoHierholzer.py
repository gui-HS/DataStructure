from arestaDP import *

class Hierholzer:
    def __init__(self, G):
        self.H = G #Graph
        self.Vvisit = list #List of visited vertices
        self.nVvisit = 0 
        self.k = int() #Number of vertices visited, closed and open

    def HierholzerAlgorithm(self, s):
        #Inicialização
        self.Vvisit[0] = s
        self.nVvisit = 1
        self.k = 1
        e3 = ArestaDP()

        while self.k <= self.nVvisit:
            u = self.Vvisit[self.k]
            while u.arestas != None:
                e0 = u.arestas[0]
                v = e0.getV2()
                self.H.removeA(e0)
                e1 = e0
            while v != u:
                if v not in self.Vvisit:
                    self.nVvisit += 1
                    self.Vvisit[self.nVvisit] = v
                e2 = v.aresta[0]
                e2.setNextEdge() = e1
                e1.setPrevEdge() = e2
                if v.getEulerEdge == None:
                    v.setEulerEdge(e2)
                e1 = e2
                v = e2.getV2()
                self.H.removeA(e1)
            #Um subciclo em u acabou de ser completado
            e0.setPrevEdge(e1)
            e1.setNextEdge(e0)

            if u.getEulerEdge() == None:
                u.setEulerEdge(e0)
            else:
                #Insere um novo subciclo preexistente em u
                e1.setEulerEdge(u)
                e2.setPrevEdge(e1)
                e3.setPrevEdge(e0)
                e2.setNextEdge(e0)
                e3.setNextEdge(e1)
        k += 1 
                