# Autor: Antonio Gabriel
#* Descrição: Programa que implementa o algoritmo de Kruskal para encontrar o peso da AGM de um grafo


#todo Função onde a magica acontece
#todo Algoritmo de Kruskal
def kruskal(listaDeArestas, numIndices):
    listaDeArestas.sort(key=lambda x: x[2])             #? Ordenando a lista de arestas pelo peso
    representante = [i+1 for i in range(numIndices)]    #? A lista de representantes
    count = 0                   #* contador
    pesoDaAGM = 0               #* peso da AGM

    for u, v, w in listaDeArestas:
        if count == numIndices - 1:         #? se o contador for igual ao numero de indices - 1, significa que a AGM foi encontrada
            break                           #? Pois     
        if find(representante, u) != find(representante, v): #? se os representantes são distintos, então não há ciclo
            pesoDaAGM += w
            count += 1
            union(representante, u, v)                      #? unindo os vertices

    print(f"{pesoDaAGM:.3f}")

#todo funcao que encontra o representante de um vertice
def find(representante, i):
    if representante[i-1] != i:
        representante[i-1] = find(representante, representante[i-1])
    return representante[i-1]

#todo funcao que une dois vertices
def union(representante, u, v):
    representante[find(representante, u)-1] = find(representante, v)

#todo funcao principal
def main():
    trash = input()                         #? variavel a ser descartada
    trash = input()  
    trash, numIndices = input().split("n=") #? pegando o numero de indices
    numIndices = int(numIndices)
    trash = input()

    listaDeArestas = []                     #? criando a lista de arestas

    status = True
    while status: 
        try:        
            (u, v, w) = input().split()
            listaDeArestas.append((int(u), int(v), float(w))) #? adicionando as arestas e seu respectivo peso à lista
        except EOFError:
            status = False
    kruskal(listaDeArestas, numIndices)             #! Onde a magica acontece


#todo Execução do programa
if __name__ == "__main__":
    main()