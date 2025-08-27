import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from (
    [
        ('Mathématiques', 'Physique'), 
        ('Physique', 'Chimie'), 
        ('Chimie', 'SVT'), 
        ('SVT', 'Informatique'), 
        ('Informatique', 'Mathématiques')
    ]
)
coloring = nx.coloring.greedy_color(G, strategy='largest_first')
node_colors = [coloring[node] for node in G.nodes()]

pos = nx.spring_layout (G)
# labels = nx.get_edge_attributes (G, 'weight')
nx.draw (G, pos, with_labels = True, node_color =node_colors)
# nx.draw_networkx_edge_labels (G , pos , edge_labels = labels)
plt.show()