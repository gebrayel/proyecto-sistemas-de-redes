import sys
from node import *
from graph import *

# print(sys.maxsize)

nodes:int = 0
nodesId = []
edges = {}
graphJ : Graph
graphA : Graph
startNodeJ = "5414"
startNodeA = "5213"
Brewery = "5012"
Disco = "5014"
Bar = "5411"


def create():

    graphJ = Graph()
    graphA = Graph()
    for i in range (50,56):
        for j in range (10, 16):
            # nodeX = Node(f'{i}:{j}')
            # nodes.append(nodeX)
            # nodesId.append(nodeX.id)
            graphJ.add_node(f'{i}:{j}')
            graphA.add_node(f'{i}:{j}')
            nodesId.append(f'{i}:{j}')
            # print(f'calle {i} con carrera {j}')
    print(nodes)
    print(nodesId)

def shortestPath(graphX: Graph,nodeActual: Node):
    if not (nodeActual.distMin == 0):
        return nodeActual.distMin + shortestPath (graphX.nodes_dict[nodeActual.pred])
    return 0

def dijkstra(graphX: Graph, startNode:str):

    graphX.nodes_dict[startNode].distMin(0)

    nonVisitedNodes = nodesId

    while nonVisitedNodes >0:
        lessDist: int = sys.maxsize
        lessId: str

        for i in range (len(nonVisitedNodes)+1):
            curValue = graphX.nodes_dict[nonVisitedNodes[i]].distMin
            if curValue < lessDist:
                lessDist = curValue
                lessId = nonVisitedNodes[i]
        
        # visit graphX.nodes_dict[lessId]
        items = graphX.nodes_dict[lessId].adj.items()
        distTillAct: int = shortestPath(graphX, graphX.nodes_dict[lessId])
        for j in (len(items)+1):
            if not ((graphX.nodes_dict[items[j][0]]).visited):
                sum = distTillAct + (graphX.nodes_dict[items[j][1]])
                if (sum < graphX.nodes_dict[items[j][0]].distMin):
                    graphX.nodes_dict[items[j][0]].distMin = sum
                    graphX.nodes_dict[items[j][0]].pred = items[j][0]
        #mark visited actual node
        graphX.nodes_dict[lessId].visted = True
        nonVisitedNodes.remove(lessId)


    return 0

def path():
    create()
    dijkstra(graphJ, startNodeJ)
    dijkstra(graphA, startNodeA)
    pathJavierSum = shortestPath(graphJ, graphJ.nodes_dict[Disco])
    pathAndreinaSum = shortestPath(graphA, graphA.nodes_dict[Disco])
    print(f'Javier Min Path = {pathJavierSum} \n Andreina Min Path = {pathAndreinaSum}')
    return 
def main():
    path()

main()
