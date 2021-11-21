import sys
from node import *
from graph import *
from edges import *

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


def maximum(a, b):
     
    if a > b:
        c=str(a-b)
        print("Andreína debe salir "+c+"min después de Javier para llegar al mismo tiempo")
        return 
    elif a< b:
        c=str(b-a)
        print("Javier debe salir "+c+"min después de Andreína para llegar al mismo tiempo")
        return
    else: 
         print("Ambos se encuentran si salen al mismo tiempo.")

def create():
    global graphJ 
    global graphA 
    global nodes
    global nodesId
    graphJ = Graph()
    graphA = Graph()
    for i in range (50,56):

        for j in range (10, 16):
            # nodeX = Node(f'{i}:{j}')
            # nodes.append(nodeX)
            # nodesId.append(nodeX.id)
            graphJ.add_node(f'{i}{j}')
            graphA.add_node(f'{i}{j}')
            nodesId.append(f'{i}{j}')
            # print(f'calle {i} con carrera {j}')
    # print(graphA.nodes_dict)
    # print(nodesId)

def shortestPath(graphX: Graph,nodeActual: Node):
    # print('num'+nodeActual.id)
    # print(nodeActual.distMin)
    if not (nodeActual.distMin == 0 ) :
        
        return  shortestPath (graphX, graphX.nodes_dict[nodeActual.pred])+ "-->" + nodeActual.id 
    return nodeActual.id 

def dijkstra(graphX: Graph, startNode:str):
    graphX.nodes_dict[startNode].set_distMin(0)
    #---------------------------------------------------------------
    #print(graphX.nodes_dict)
    #---------------------------------------------------------------
    nonVisitedNodes = []
    if len(nodesId)<1:
        #---------------------------------------------------------------
        #print('entro')
        #---------------------------------------------------------------
        for i in graphX.nodes_dict.keys():
            nonVisitedNodes.append(i)
    else:
        nonVisitedNodes = nodesId

    while len(nonVisitedNodes) >0:
        lessDist: int = sys.maxsize
        lessId: str
        for i in range (len(nonVisitedNodes)):
            
            curValue = graphX.nodes_dict[nonVisitedNodes[i]].distMin
            if curValue < lessDist:
                lessDist = curValue
                lessId = nonVisitedNodes[i]
        
        # visit graphX.nodes_dict[lessId]
        items = graphX.nodes_dict[lessId].adj.items()
        distTillAct: int = graphX.nodes_dict[lessId].distMin
        for j,k in ((items)):
            if not ((j).visited):
                sum = distTillAct + (k)
                if (sum < j.distMin):
                    j.set_distMin(sum)
                    j.set_predec(lessId) 
        #mark visited actual node
        graphX.nodes_dict[lessId].visit()
        nonVisitedNodes.remove(lessId)
    #---------------------------------------------------------------
    #print(nonVisitedNodes)
    #print(nodesId)
    #---------------------------------------------------------------

    return 0
def path(finalNode:str):
    create()
    #aristas javier

    #fila 50
    edgesFunct(graphJ,graphA)
    # print('a')

    dijkstra(graphA, startNodeA)
    #---------------------------------------------------------------
    #print("viene javier")
    #---------------------------------------------------------------
    dijkstra(graphJ, startNodeJ)
    destinatation :str = finalNode
    # print(graphA.nodes_dict)
    pathAndreinaSum = graphA.nodes_dict[destinatation].distMin
    pathJavierSum = graphJ.nodes_dict[destinatation].distMin
    print(f'El tiempo mímimo de Javier es {pathJavierSum}min por {shortestPath(graphJ, graphJ.nodes_dict[destinatation])} \nEl tiempo mímimo de Andreina es {pathAndreinaSum}min por {shortestPath(graphA, graphA.nodes_dict[destinatation])} '+"\n")
    maximum(pathJavierSum,pathAndreinaSum)
    return 

def main():
    loop = "0"
    while loop == "0":
        print("Javier y Andreina deben escojer su destino.")
        print ("1. Ir al Brewery.")
        print ("2. Ir a la Disco.")
        print ("3. Ir al Bar.")
        destino = input("Ingrese 1,2 ó 3, según corresponda: ")
        if destino == "1":
            destino = Brewery
            print ("Javier y Andreina irán al Brewery"+ "\n"*5)
            path(destino)
            print("Oprime 0 si deseas escojer un nuevo destino.")
            loop = input()
            print("\n"*5)
        elif destino == "2":
            destino = Disco
            print ("Javier y Andreina irán a la Disco"+ "\n"*5)
            path(destino)
            print("Oprime 0 si deseas escojer un nuevo destino.")
            loop = input()
            print("\n"*5)
        elif destino == "3":
            destino = Bar
            print ("Javier y Andreina irán al Bar"+ "\n"*5)
            path(destino)
            print("Oprime 0 si deseas escojer un nuevo destino.")
            loop = input()
            print("\n"*5)

        else:
            print ("I'm sorry, I didn't get that" + "\n"*5)
        
        



main()
