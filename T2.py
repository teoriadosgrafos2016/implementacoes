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

    print(Q)
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
    print(MST.edge)
    return MST

def main():

    G = nx.read_weighted_edgelist("/home/felipe/pycharmprojects/Grafos/testeEdgeList.txt")

    MST = MST_Prim(G,'a')

    pos = nx.circular_layout(G)
    # nx.draw_networkx_nodes(G, pos, node_color = 'b')
    # nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='r', arrows=True)

    nx.draw_networkx_nodes(MST, pos, node_color = 'b')
    nx.draw_networkx_edges(MST, pos, edgelist=MST.edges(), edge_color='g', arrows=True)

    nx.draw_networkx_labels(MST,pos,font_size=12)

    labels = nx.get_edge_attributes(MST,'weight')
    nx.draw_networkx_edge_labels(MST,pos,edge_labels=labels)

    plt.show()

if __name__=="__main__":
    main()