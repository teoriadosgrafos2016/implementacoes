import networkx as nx #Para a parte de criar e gerenciar grafos
import numpy as np
import matplotlib.pyplot as plt #Para exibir na tela

#Criacao de um Digrafo nulo
# G = nx.DiGraph()
# pos=nx.spring_layout(G)
# #Mapeamento do tabuleiro do jogo
# G.add_edge(1, 15) #Sobe a escada
# G.add_edge(1, 3)
# G.add_edge(3, 4)
# G.add_edge(3, 7) #Sobe a escada
# G.add_edge(4, 7) #Sobe a escada
# G.add_edge(4, 6)
# G.add_edge(6, 7)
# G.add_edge(6, 8)
# G.add_edge(7, 8)
# G.add_edge(7, 27) #Sobe a escada
# G.add_edge(8, 27) #Sobe a escada
# G.add_edge(8, 10)
# G.add_edge(10, 11)
# G.add_edge(10, 12)
# G.add_edge(11, 12)
# G.add_edge(11, 13)
# G.add_edge(12, 13)
# G.add_edge(12, 14)
# G.add_edge(13, 14)
# G.add_edge(13, 15)
# G.add_edge(14, 15)
# G.add_edge(14, 16)
# G.add_edge(15, 16)
# G.add_edge(15, 4) #Desce pela cobra
# G.add_edge(16, 4) #Desce pela cobra
# G.add_edge(16, 29) #Sobe a escada
# G.add_edge(19, 6) #Desce pela cobra
# G.add_edge(19, 21)
# G.add_edge(21, 22)
# G.add_edge(21, 23)
# G.add_edge(22, 23)
# G.add_edge(22, 16) #Desce pela cobra
# G.add_edge(23, 16) #Desce pela cobra
# G.add_edge(23, 35) #Sobe a escada
# G.add_edge(26, 27)
# G.add_edge(26, 28)
# G.add_edge(27, 28)
# G.add_edge(27, 29)
# G.add_edge(28, 29)
# G.add_edge(28, 30)
# G.add_edge(29, 30)
# G.add_edge(29, 31)
# G.add_edge(30, 31)
# G.add_edge(30, 30) #Desce pela cobra
# G.add_edge(31, 30) #Desce pela cobra
# G.add_edge(31, 33)
# G.add_edge(33, 12) #Desce pela cobra
# G.add_edge(33, 35)
# G.add_edge(35, 36)

G = nx.DiGraph()
G.add_edges_from([(1,3),(2,1),(2,4),(3,2),(3,4),(4,3),(5,1),(5,3)])

print(G.edge)


def matrizProbabilidade(G):
    A = nx.to_numpy_matrix(G) # Matriz de adjacencia de G
    for linha in A:
        grau = np.sum(linha)
        if(grau != 0):
            for i in range(len(linha)):
                linha[i] /= grau
    return A

P = matrizProbabilidade(G)
print(P)

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

w = [1]
for i in range(G.number_of_nodes()-1):
    w.append(0)
A = powerMethod(G,w,100)
print(A)
print(np.sum(A))
print(distEstacionaria(G))
print(np.sum(distEstacionaria(G)))

'''A = matrizProbabilidade(G)
print(A)
pos = nx.spring_layout(G,k=0.15,iterations=20)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color = 'b')
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='g', arrows=True)
nx.draw_networkx_labels(G,pos,font_size=12)
plt.show()'''