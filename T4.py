import networkx as nx #Para a parte de criar e gerenciar grafos
import numpy as np
import matplotlib.pyplot as plt #Para exibir na tela

def metodoHungaro(G, M): # G e grafo bipartido e M um emparelhamento inicial
    S = []
    T = []



def main():

    G = nx.read_weighted_edgelist("/home/felipe/pycharmprojects/Grafos/grafoBipartido")
    print(G.edge)

    M = [('0', '11'),('1', '13')]

    metodoHungaro(G, M)

if __name__=='__main__':
    main()