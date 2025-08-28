import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_weighted_edges_from(
    [('A', 'B', 2), ('A', 'C', 4), ('B', 'E', 1), ('B', 'D', 3), ('C', 'E', 3), ('D', 'E', 5), ('D', 'G', 2)])
# pos = nx.spring_layout(G)
# labels = nx . get_edge_attributes (G , 'weight')
# nx.draw (G, pos, with_labels = True, node_color ='lightblue')
# nx . draw_networkx_edge_labels (G , pos , edge_labels = labels )
# plt.show()
chemin = nx . dijkstra_path (G , source ='A', target ='G')
distance = nx . dijkstra_path_length (G , source ='A', target ='G'
)
print ("Chemin :", chemin)
print ("Distance :", distance)