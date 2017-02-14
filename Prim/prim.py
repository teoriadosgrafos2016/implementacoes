import networkx as nx #Para a parte de criar e gerenciar grafos
import numpy as np
import matplotlib.pyplot as plt #Para exibir na tela

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

def main():

    G = nx.read_weighted_edgelist("../Grafo.txt")

    MST = MST_Prim(G,'1')

    pos = nx.circular_layout(G)
    Desenha(G, pos, 'r', 'GrafoOriginal')
    Desenha(MST, pos, 'g', 'MST')

def Desenha(G, pos,lineColor, filename):

    nx.draw_networkx_nodes(G, pos, node_color='b', node_size=150)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color=lineColor, arrows=True)

    nx.draw_networkx_labels(G, pos, font_size=8)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

    plt.savefig('primImages/'+filename+'.png',dpi=250)
    plt.clf()

if __name__=="__main__":
    main()