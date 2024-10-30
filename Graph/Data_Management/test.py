from py2neo import Graph

# Verbindung zur Neo4j-Datenbank herstellen
graph = Graph("neo4j+s://9df9a03f.databases.neo4j.io", auth=("neo4j", "MgDR4X6UnRMmXoJ-awLtSZKZkzY43jKpUuqnZKlnqn0"))
try:
    graph.run("RETURN 1")
    print("Verbindung erfolgreich!")
except Exception as e:
    print(f"Verbindungsfehler: {e}")

# Beispielhafte Abfrage für Knoten und Beziehungen
query = """
MATCH p = (c1:District)<-[n]-(c2:City WHERE c2.Name = 'Siegburg')-[n2]->(c3:City) RETURN c1, n, c2, n2, c3
"""
data = graph.run(query).data()

import networkx as nx

# Netzwerk in NetworkX erstellen
G = nx.Graph()

for record in data:
    node_a = record["c1"]
    node_b = record["c2"]
    node_c = record["c3"]
    relationship = record["n"]
    relationship_2 = record["n2"]

    # Knoten und Kanten hinzufügen
    G.add_node(node_a["Name"], label=node_a["label"])
    G.add_node(node_b["Name"], label=node_b["label"])
    G.add_node(node_b["Name"], label=node_c["label"])
    G.add_edge(node_a["Name"], node_b["Name"], relationship=relationship[""])
    G.add_edge(node_b["Name"], node_c["Name"], relationship=relationship_2[""])

import plotly.graph_objects as go
import numpy as np

# 3D-Positionen für die Knoten festlegen
positions = {node: np.random.rand(3) for node in G.nodes}

# 3D-Koordinaten extrahieren
x_nodes = [positions[node][0] for node in G.nodes]
y_nodes = [positions[node][1] for node in G.nodes]
z_nodes = [positions[node][2] for node in G.nodes]

# Visualisierung für Knoten
node_trace = go.Scatter3d(
    x=x_nodes, y=y_nodes, z=z_nodes,
    mode='markers+text',
    marker=dict(size=5, color='blue'),
    text=list(G.nodes),
)

# Visualisierung für Kanten
edge_trace = []
for edge in G.edges:
    x_edge = [positions[edge[0]][0], positions[edge[1]][0], None]
    y_edge = [positions[edge[0]][1], positions[edge[1]][1], None]
    z_edge = [positions[edge[0]][2], positions[edge[1]][2], None]
    
    edge_trace.append(
        go.Scatter3d(
            x=x_edge, y=y_edge, z=z_edge,
            mode='lines',
            line=dict(color='black', width=2)
        )
    )

# Plot erstellen
fig = go.Figure(data=[node_trace] + edge_trace)
fig.update_layout(scene=dict(aspectmode="cube"))
fig.show()
