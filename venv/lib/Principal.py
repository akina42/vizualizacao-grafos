import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def draw(G, pos, labels, custom_node_labels, pos_text_coordinates, measures, measure_name):

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)

    nx.draw(G, pos, with_labels=True, node_size=250, cmap=plt.cm.Blues,
                                   node_color=list(measures.values()),
                                   nodelist=measures.keys(),
                                ax=ax1)
    nodes = nx.draw_networkx_nodes(G, pos, node_size=250, cmap=plt.cm.Blues,
                                   node_color=list(measures.values()),
                                   nodelist=measures.keys(),
                                   ax=ax1)

    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1))

    labels_draw = nx.draw_networkx_labels(G, pos_text_coordinates, labels=custom_node_labels)
    edges = nx.draw_networkx_edges(G, pos)

    plt.title(measure_name)
    plt.colorbar(nodes)
    plt.axis('off')
    plt.savefig("/home/akina/Dropbox/TCC/Exemplos/Centralidade_Autovetor.png")
    plt.show()

###########################################################################

G = nx.krackhardt_kite_graph()
pos = {3:(2,3),5:(4,4),2:(2,5),0:(0,4),6:(4,2),4:(2,1),1:(0,2),7:(6,3),8:(8,3),9:(10,3)}
#pos = {3:(2,3),5:(4,4),2:(2,5),0:(0,4),6:(4,2),4:(2,1),1:(0,2),7:(6,3),8:(8,3),9:(10,3)}
#pos = {'A':(2,3),'B':(3.5,4),'C':(2,5),'D':(0.5,4),'E':(3.5,2),'F':(2,1),'G':(0.5,2),'H':(5,3),'I':(6,3),'J':(7,3)}

labels = {}
labels[0] = r'D'
labels[1] = r'E'
labels[2] = r'C'
labels[3] = r'A'
labels[4] = r'F'
labels[5] = r'B'
labels[6] = r'G'
labels[7] = r'H'
labels[8] = r'I'
labels[9] = r'J'

'''
G = nx.Graph()
G.add_nodes_from(['B', 'G', 'C', 'A', 'F', 'D', 'E', 'J', 'I', 'H'])
G.add_edges_from([(0, 1), (0, 2), (0, 3), (0, 5), (0, 9), (1, 3), (1, 4), (1, 6), (1, 9), (2, 3), (2, 5), (3, 4), (3, 5), (3, 6), (4, 6), (5, 6), (7, 8), (8, 9)])
fixed_positions = {3:(2,3),0:(3,4),2:(2,5),5:(1,4),6:(1,2),4:(2,1),1:(-3,2),9:(5,3),8:(6,3),7:(7,3)}
fixed_nodes = fixed_positions.keys()
pos = nx.spring_layout(G,pos=fixed_positions, fixed=fixed_nodes)
pos=nx.spring_layout(G)


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



#draw(G, pos, labels, nx.degree_centrality(G), 'Centralidade de Grau')

eigenvector_centrality = nx.eigenvector_centrality_numpy(G, "weight", len(G), 0)

pos_text_coordinates = {}
for node, coords in pos.items():
    #pos_text_coordinates[node] = (coords[0], coords[1] + 0.08)
    pos_text_coordinates[node] = (coords[0], coords[1] - 0.23)

myFormattedList = [ round(elem, 2) for elem in eigenvector_centrality.values() ]

custom_node_labels={}
for v in G.nodes():
    custom_node_labels[v]=round(eigenvector_centrality[v], 2)
    print("%0.2d %5.3f" % (v, eigenvector_centrality[v]))

draw(G, pos, labels, custom_node_labels, pos_text_coordinates, eigenvector_centrality, 'Centralidade de Autovetor')

#closeness_centrality = nx.closeness_centrality(G, None, None, True, True)
#draw(G, pos, labels, closeness_centrality, 'Centralidade de Proximidade')


#betweenness_centrality = nx.betweenness_centrality(G, len(G), True, "weight", False, None)
#draw(G, pos, labels, betweenness_centrality, 'Centralidade de Intermediação')

