from node import *
class Graph():

    def __init__(self):
        self.nodes_dict = {}
        self.num_vertices = 0 #no reelevante
    
    def add_node(self, nodeId: str):  #str tipo calle callecarrera (5010, 5011, 5012)
        self.num_vertices = self.num_vertices + 1
        new_node = Node(nodeId)
        self.nodes_dict[nodeId] = new_node
        return new_node

    def add_edge(self, nodeFrom: str, nodeTo: str, time: int):
        # if nodeFrom not in self.nodes_dict:
        #     self.add_node(nodeFrom)
        # if nodeTo not in self.nodes_dict:
        #     self.add_node(nodeTo)

        self.nodes_dict[nodeFrom].add_neighbor(self.nodes_dict[nodeTo], time)
        self.nodes_dict[nodeTo].add_neighbor(self.nodes_dict[nodeFrom], time)

