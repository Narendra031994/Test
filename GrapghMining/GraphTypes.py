import networkx as nx 
import matplotlib.pyplot as plt

#implementing the complete graph(kn) using networkx

class Graphs:
    def __init__(self,):
        self.edgelist = []

    def create_cg(self,no_of_nodes):
        nodes = range(no_of_nodes)
        for i in nodes:
            for j in nodes:
                self.edgelist.append((i,j))
        G = nx.Graph(self.edgelist)
        nx.draw(G,with_labels = True)
        plt.show()
        self.edgelist.clear()
        return G
obj = Graphs()
#below loop generates complete graphs for the given n values
for i in range(3,11):
    obj.create_cg(i)
    


