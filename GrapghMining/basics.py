import networkx as nx
import matplotlib.pyplot as plt

"""
networkx is a graph mining package, it is useful to analyze the networking system and also to solve some of the graph related problems.

"""
# this is the undirected graph
G = nx.Graph()
G.add_node("a",)
G.add_node("b")
G.add_node("c")
G.add_node("d")
G.add_node("e")
#add the edge explicitly
G.add_edge("a","b")
G.add_edge("a","e")
G.add_edge("a","d")
#draw method 
nx.draw(G,with_labels = True,font_weight='bold')
#create graph by importing the edgelist data from a txt file( data format : a b, where a and b are the nodes of a graph)
H = nx.read_edgelist("graph_data.txt")
nx.edges(H)
nx.draw(H,with_labels = True,font_weight='bold')
plt.show()

#getting the degree of each node
deg = H.degree()

#.............rgfdg.....
# gfg.
# gg.............................................................................