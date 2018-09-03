import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def draw(G, pos, measures, measure_name):
    nodes = nx.draw_networkx_nodes(G, pos, node_size=250, cmap=plt.cm.plasma,
                                   node_color=list(measures.values()),
                                   nodelist=measures.keys())
    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1))

    labels = nx.draw_networkx_labels(G, pos)
    edges = nx.draw_networkx_edges(G, pos)

    plt.title(measure_name)
    plt.colorbar(nodes)
    plt.axis('off')
    plt.savefig("/home/akina/Dropbox/TCC/Exemplos/teste.png")
    plt.show()



G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
G.add_edges_from([(0, 1), (0, 2), (0, 3), (0, 5), (0, 9), (1, 3), (1, 4), (1, 6), (1, 9), (2, 3), (2, 5), (3, 4), (3, 5), (3, 6), (4, 6), (5, 6), (7, 8), (8, 9)])


pos=nx.spring_layout(G)

'''
colors=range(20)
cmap=plt.cm.Blues
vmin = min(colors)
vmax = max(colors)

degree_centrality = nx.degree_centrality(G)

nx.draw(G, pos, node_color=list(degree_centrality.values()), edge_color='#D3D3D3', width=4, edge_cmap=cmap,
           with_labels=False, vmin=vmin, vmax=vmax)


sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
plt.colorbar(sm)
plt.savefig("node_colormap.png")
plt.show()
'''

#draw(G, pos, nx.degree_centrality(G), 'Centralidade de Grau')

#eigenvector_centrality = nx.eigenvector_centrality_numpy(G, "weight", len(G), 0)
#draw(G, pos, eigenvector_centrality, 'Centralidade de Autovetor')

#closeness_centrality = nx.closeness_centrality(G, None, None, True, True)
#draw(G, pos, closeness_centrality, 'Centralidade de Proximidade')


#betweenness_centrality = nx.betweenness_centrality(G, len(G), True, "weight", False, None)
#draw(G, pos, betweenness_centrality, 'Centralidade de Intermediação')
