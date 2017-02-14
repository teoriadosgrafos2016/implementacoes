import networkx as nx  # Para a parte de criar e gerenciar grafos
import numpy as np
from random import randint
import matplotlib.pyplot as plt  # Para exibir na tela


def Desenha(G,pos,lineColor,filename):
    nx.draw_networkx_nodes(G, pos, node_color='b', node_size=150)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color=lineColor, arrows=True)

    nx.draw_networkx_labels(G, pos, font_size=8)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

    plt.savefig(filename+'.png',dpi=250)
    plt.clf()


def MST_Prim(G,r):
    Q = []  # Fila de prioridades

    for v in G.nodes():
        if v is r:
            G.node[v]['lambda'] = 0
        else:
            G.node[v]['lambda'] = np.Infinity

        G.node[v]['predecessor'] = None
        Q.append([v, G.node[v]['lambda']])

    S = []  # Ja finalizados
    while(Q):
        Q.sort(key=lambda item: item[1])
        u = Q.pop(0)
        S.append(u[0])
        for v in G.neighbors(u[0]):
            if (v not in S):
                if (G.node[v]['lambda'] >= G.edge[u[0]][v]['weight']):
                    Q.remove([v, G.node[v]['lambda']])
                    G.node[v]['lambda'] = G.edge[u[0]][v]['weight']
                    G.node[v]['predecessor'] = u[0]
                    Q.append([v, G.node[v]['lambda']])
    MST = nx.Graph()
    MST.add_nodes_from(G.nodes())
    for v in S:
        if G.node[v]['predecessor'] != None:
            u = G.node[v]['predecessor']
            MST.add_edge(v, u, weight=G.edge[v][u]['weight'])

    return MST

def TSP_TwiceAround(G):
    H = [] # Conjunto solução inicia vazio (será preenchido com o ciclo hamiltoniano)

    raiz = randint(0,G.number_of_nodes()-1) # Para calcular a MST no passo seguinte, escolhemos uma raiz aleatória
    T = MST_Prim(G, raiz) # MST do grafo

    D = nx.MultiGraph()  # Para que seja possível duplicar as arestas, devido as arestas paralelas, é necessário utilizar um multigrafo
    D.add_weighted_edges_from(T.edges(data=True))  # Duplicamos as arestas adicionando-as duas vezes no mesmo grafo
    D.add_weighted_edges_from(T.edges(data=True))

    L = list(nx.eulerian_circuit(D,source=raiz)) # Lista com as arestas que formam um Tour de Euler

    # Com o Tour de Euler em seu formato apropriado, iniciamos o processo de eliminação de repetição de vértices
    peso = 0
    H.append(L[0][0])

    for u,v in L:
        if v not in H:
            H.append(v)
            u = D.get_edge_data(u,v)
            peso = peso + u[0]['weight']['weight']

    # Adiciona o vértice origem no final do caminho para completar o ciclo
    H.append(H[0])

    return L,H,peso

def main():

    A = np.loadtxt('matriz.txt')
    G = nx.from_numpy_matrix(A)
    with open("resultado.txt", 'w') as arquivo:
        for i in range(10):
            arquivo.write("Iteracao "+str(i+1))
            cicloHamiltoniano = TSP_TwiceAround(G)
            arquivo.write("\nTour de Euler extraido: " + str(cicloHamiltoniano[0]))
            arquivo.write("\nCiclo Hamiltoniano Final: "+str(cicloHamiltoniano[1]))
            arquivo.write("\nPeso: " + str(cicloHamiltoniano[2]))
            arquivo.write("\n___________________________________________________________\n")

if __name__=='__main__':
    main()
