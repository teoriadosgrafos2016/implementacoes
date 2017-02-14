import networkx as nx #Para a parte de criar e gerenciar grafos
import numpy as np
from random import randint
import matplotlib.pyplot as plt #Para exibir na tela

def Desenha(G, pos,lineColor, filename):

    nx.draw_networkx_nodes(G, pos, node_color='b', node_size=150)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color=lineColor, arrows=True)

    nx.draw_networkx_labels(G, pos, font_size=8)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

    plt.savefig(filename+'.png',dpi=250)
    plt.clf()

def MST_Prim(G,r):
    Q = [] # Fila de prioridades

    for v in G.nodes():
        if v is r:
            G.node[v]['lambda'] = 0
        else:
            G.node[v]['lambda'] = np.Infinity

        G.node[v]['predecessor'] = None
        Q.append([v, G.node[v]['lambda']])

    S = [] # Ja finalizados
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
    pos = nx.circular_layout(G)
    # Desenha(G, pos, 'r', 'GrafoOriginal')

    H = []
    raiz = randint(0,G.number_of_nodes()-1)
    T = MST_Prim(G, raiz) # MST do grafo
    D = nx.MultiGraph()
    # Desenha(T, pos, 'r', 'GrafoMST')
    print(T.edge)
    D.add_weighted_edges_from(T.edges(data=True))
    D.add_weighted_edges_from(T.edges(data=True))
    print(D.edge)


def main():
    A = np.loadtxt('matriz.txt')
    G = nx.from_numpy_matrix(A)

    print(G.edges(data=True))
    TSP_TwiceAround(G)
if __name__=='__main__':
    main()

#--------------------------------------------------------------------#
