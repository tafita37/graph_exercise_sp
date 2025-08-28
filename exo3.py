import networkx as nx
import matplotlib.pyplot as plt

# Création du graphe orienté
G = nx.DiGraph()

# Ajout des arêtes avec capacités (exemple : à adapter avec ton énoncé exact)
# G.add_edge(source, target, capacity=valeur)
G.add_edge("A", "T", capacity=5)
G.add_edge("B", "A", capacity=15)
G.add_edge("B", "T", capacity=10)
G.add_edge("S", "A", capacity=10)
G.add_edge("S", "B", capacity=5)

# Calcul du flot maximal avec Ford-Fulkerson (implémenté en interne)
flow_value, flow_dict = nx.maximum_flow(G, "S", "T")

print("Flot maximal :", flow_value)
print("Répartition des flots :")
for u, v_dict in flow_dict.items():
    for v, flow in v_dict.items():
        if flow > 0:
            print(f"{u} -> {v} : {flow}")
                
pos = nx.spring_layout(G)
labels = nx . get_edge_attributes (G , 'capacity')
nx.draw (G, pos, with_labels = True, node_color ='lightblue')
nx . draw_networkx_edge_labels (G , pos , edge_labels = labels )
plt.show()
