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

slots = {0: "9h-11h", 1: "11h-13h", 2: "14h-16h"}
timetable = {subject: slots[color] for subject, color in coloring.items()}
print(timetable)

pos = nx.spring_layout (G)
nx.draw (G, pos, with_labels = True, node_color =node_colors)
plt.show()