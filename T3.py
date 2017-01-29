import networkx as nx #Para a parte de criar e gerenciar grafos
import numpy as np
import matplotlib.pyplot as plt #Para exibir na tela

def Dijkstra(G,raizes):
    Q = [] # Fila de prioridades

    for v in G.nodes():
        if v in raizes:
            G.node[v]['lambda'] = 0
        else:
            G.node[v]['lambda'] = np.Infinity

        G.node[v]['predecessor'] = None
        Q.append([v, G.node[v]['lambda']])

    print(Q)
    S = [] # Ja finalizados
    while(Q):
        Q.sort(key=lambda item: item[1])
        print(Q)
        u = Q.pop(0)
        S.append(u[0])
        for v in G.neighbors(u[0]):
            if (v not in S):
                if (G.node[v]['lambda'] >= G.node[u[0]]['lambda'] + G.edge[u[0]][v]['weight']):
                    Q.remove([v, G.node[v]['lambda']])
                    G.node[v]['lambda'] = G.node[u[0]]['lambda'] + G.edge[u[0]][v]['weight']
                    G.node[v]['predecessor'] = u[0]
                    Q.append([v, G.node[v]['lambda']])
                print(v)
    TREE = nx.Graph()
    TREE.add_nodes_from(G.nodes())
    for v in S:
        if G.node[v]['predecessor'] != None:
            u = G.node[v]['predecessor']
            TREE.add_edge(v, u, weight=G.edge[v][u]['weight'])
    print(TREE.edge)
    return TREE

def main():

    G = nx.read_weighted_edgelist("/home/felipe/pycharmprojects/Grafos/testeEdgeList.txt")

    TREE = Dijkstra(G,['a','e'])

    pos = nx.circular_layout(G)
    # nx.draw_networkx_nodes(G, pos, node_color = 'r')
    # nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='r', arrows=True)

    nx.draw_networkx_nodes(TREE, pos, node_color = 'b')
    nx.draw_networkx_edges(TREE, pos, edgelist=TREE.edges(), edge_color='g', arrows=True)

    nx.draw_networkx_labels(TREE,pos,font_size=12)

    labels = nx.get_edge_attributes(TREE,'weight')
    nx.draw_networkx_edge_labels(TREE,pos,edge_labels=labels)

    plt.show()

if __name__=='__main__':
    main()
