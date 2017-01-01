import networkx as nx #Para a parte de criar e gerenciar grafos
import numpy as np
import matplotlib.pyplot as plt #Para exibir na tela

G = nx.Graph()

G.add_edge('a','b',weight=4)
G.add_edge('a','h',weight=8)
G.add_edge('b','c',weight=8)
G.add_edge('b','h',weight=11)
G.add_edge('c','d',weight=7)
G.add_edge('c','i',weight=2)
G.add_edge('c','f',weight=4)
G.add_edge('d','e',weight=9)
G.add_edge('d','f',weight=14)
G.add_edge('e','f',weight=10)
G.add_edge('f','g',weight=2)
G.add_edge('g','i',weight=6)
G.add_edge('g','h',weight=1)
G.add_edge('h','i',weight=7)

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

TREE = Dijkstra(G,['a','e'])

pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, node_color = 'b')
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='r', arrows=True)

nx.draw_networkx_nodes(TREE, pos, node_color = 'b')
nx.draw_networkx_edges(TREE, pos, edgelist=TREE.edges(), edge_color='g', arrows=True)

nx.draw_networkx_labels(G,pos,font_size=12)

labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

plt.show()