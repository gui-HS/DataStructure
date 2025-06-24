
#Heap Data Structure
#https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/hpsrt.html Resource
#root = 0. right = 2*i, left = 2*i + 1, Parents = i/2

vetor = [5,25,432,10,19,23]

def heapify(arr, n, i):
    j = i

    while (2*j+1) < n:
        f = j*2+1

        #Checa se esquerda é maior que direita
        if f+1 < n and arr[f] < arr[f+1]:
            f = f+1
        
        #Termina se o elemento pai for maior que filhos
        if arr[j] >= arr[f]:
            j = n
        else:
            #Troca pai e nó de lugar
            arr[j], arr[f] = arr[f], arr[j]
            j = f

def constroi_max_heap(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)


def heapsort(arr):
    constroi_max_heap(arr)
    n = len(arr)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] 
        heapify(arr, i, 0)

heapsort(vetor)
print(vetor)

