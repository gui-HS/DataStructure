
#Heap Data Structure
#https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/hpsrt.html Resource
#root = 0. right = 2*i, left = 2*i + 1, Parents = i/2

vetor = [30, 15, 19, 10, 18, 25]
vetor2 = [5,25,432,10,19,23]

def hipfy(arr, i):
    n = len(arr)-1
    j = i

    while 2*j <= n:
        f = j*2
        if f < n and arr[f] < arr[f+1]:
            f = f+1
        
        if arr[j] >= arr[f]:
            j = n
        else:
            arr[j], arr[f] = arr[f], arr[j]

def constroi_max_heap(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        hipfy(arr, i)


def heapsort(arr):
    constroi_max_heap(arr)
    n = len(arr)

    for i in range(n-1, 1, -1):
        arr[0] = arr[i]
        hipfy(arr, 1)

heapsort(vetor2)
print(vetor2)


