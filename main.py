def kruskal(listaDeArestas, numIndices):
    listaDeArestas.sort(key=lambda x: x[2])
    pai = [i+1 for i in range(numIndices)]
    count = 0
    pesoDaAGM = 0

    for u, v, w in listaDeArestas:
        if count == numIndices - 1:
            break
        if find(pai, u) != find(pai, v):
            pesoDaAGM += w
            count += 1
            union(pai, u, v)

    print(f"{pesoDaAGM:.3f}")

def find(pai, i):
    if pai[i-1] != i:
        pai[i-1] = find(pai, pai[i-1])
    return pai[i-1]

def union(pai, u, v):
    pai[find(pai, u)-1] = find(pai, v)

def main():
    trash = input()  
    trash = input()  
    trash, numIndices = input().split("n=") 
    numIndices = int(numIndices)
    trash = input()

    listaDeArestas = []

    status = True
    while status: 
        try:        
            (u, v, w) = input().split()
            listaDeArestas.append((int(u), int(v), float(w)))
        except EOFError:
            status = False
    kruskal(listaDeArestas, numIndices)



if __name__ == "__main__":
    main()