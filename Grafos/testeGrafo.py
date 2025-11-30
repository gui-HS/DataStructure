from grafo import *
from graphicRepresentation import graphic

def main():
    print("OK")

    grafo1 = Grafo()
    for i in range(25):
        grafo1.insereV()

    grafo1.vertices()

    #Lista após remoção
    print("\n"*5)
    grafo1.vertices()
    print(grafo1.getOrdem())
    print(grafo1.getTamanho())

    for i in range((len(grafo1.listaVertices)-1)):
        grafo1.insereA(i,i+1)
    
    grafo1.insereA(24,0)

    #estrela
    grafo1.insereA(19,6)
    grafo1.insereA(6, 0)
    grafo1.insereA(0, 14)
    grafo1.insereA(14, 2)
    grafo1.insereA(2, 19)

    graphic(grafo1)

if __name__ == "__main__":
    main()
