import sys
class  Node:

    def __init__(self, id: str) -> None:
        self.id = id
        self.distMin = sys.maxsize
        self.visited = False
        self.pred = ""
        self.adj = {}

    def visit (self):
        self.visited = True

    def set_predec (self, pred:str):
        self.pred = pred

    def set_distMin(self, distMin: int):
        self.distMin = distMin

    def add_neighbor(self, neighbor: str, time: int):
        self.adj[neighbor] = time
