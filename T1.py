import networkx as nx #Para a parte de criar e gerenciar grafos
import numpy as np
import matplotlib.pyplot as plt #Para exibir na tela

def matrizProbabilidade(G):
    A = nx.to_numpy_matrix(G) # Matriz de adjacencia de G
    for linha in A:
        grau = np.sum(linha)
        if(grau != 0):
            for i in range(len(linha)):
                linha[i] /= grau
    return A

def distEstacionaria(G):
    E = G.number_of_edges()
    print(E)
    w = []
    for node in G.edge:
        w.append(len(G[node])/E) # Quando o grafo nao e direcionado divide-se por 2E, mas quando e divide-se por E apenas
        #print(w)

    return w

def powerMethod(G, w, k):
    P = matrizProbabilidade(G)

    for i in range(k):
        w = w * P
        #print(w)

    return w

def main():
    G = nx.DiGraph()
    G.add_edges_from([(1, 3), (2, 1), (2, 4), (3, 2), (3, 4), (4, 3), (5, 1), (5, 3)])

    P = matrizProbabilidade(G)
    print("Matriz de probabilidade:\n"+str(P))

    w = []
    n = G.number_of_nodes()
    for i in range(n):
        w.append(1/n)
    print(w) # Teste de inicialização
    A = powerMethod(G,w,100) # Precisamos verificar se os resultados estão corretos, há uma pequena divergencia

    print("Power Method: "+str(A))
    print("Soma do power method: " + str(np.sum(A)))
    print("Distribuicao estacionaria: "+str(distEstacionaria(G)))
    print(np.sum(distEstacionaria(G)))

    '''A = matrizProbabilidade(G)
    print(A)
    pos = nx.spring_layout(G,k=0.15,iterations=20)
    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color = 'b')
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='g', arrows=True)
    nx.draw_networkx_labels(G,pos,font_size=12)
    plt.show()'''

if __name__=="__main__":
    main()