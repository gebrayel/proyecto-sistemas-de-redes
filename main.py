import sys
from node import *

# print(sys.maxsize)

nodes =[]
nodesId = []
edges = {}


def create():
    for i in range (50,56):
        for j in range (10, 16):
            nodeX = Node(f'{i}:{j}')
            nodes.append(nodeX)
            nodesId.append(nodeX.id)
            # print(f'calle {i} con carrera {j}')
    print(nodes)
    print(nodesId)

def dijkstra(nodesArray:list, edgesObject:dict, startNode:list):

    pass

def main():
    create()

main()
