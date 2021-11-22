import sys
from node import *
from graph import *
from edges import *
from test import *

nodes:int = 0
nodesId = []
edges = {}
graphJ : Graph
graphA : Graph
graphJ1 : Graph
graphA2 : Graph
startNodeJ = "5414"
startNodeA = "5213"
Brewery = "5012"
Disco = "5014"
Bar = "5411"
resultString:str = ""

def maximum(a, b, stdscr):
     
    global resultString
    if a > b:
        c=str(a-b)
        resultString = resultString + "Andreína debe salir "+c+"min después de Javier para llegar al mismo tiempo"
        # stdscr.addstr("Andreína debe salir "+c+"min después de Javier para llegar al mismo tiempo", curses.A_UNDERLINE)
        
        return 
    elif a< b:
        c=str(b-a)
        resultString = resultString + "Javier debe salir "+c+"min después de Andreína para llegar al mismo tiempo"
        
        
        return
    else: 
        resultString = resultString + "Ambos se encuentran si salen al mismo tiempo."
        
        
def create():
    global graphJ 
    global graphA 
    global graphA2
    global graphJ1
    global nodes
    global nodesId
    graphJ = Graph()
    graphA = Graph()
    graphJ1 = Graph()
    graphA2 = Graph()
    for i in range (50,56):

        for j in range (10, 16):
            # nodeX = Node(f'{i}:{j}')
            # nodes.append(nodeX)
            # nodesId.append(nodeX.id)
            graphJ.add_node(f'{i}{j}')
            graphA.add_node(f'{i}{j}')
            graphJ1.add_node(f'{i}{j}')
            graphA2.add_node(f'{i}{j}')
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

def restrictedDijkstra(graphX: Graph, startNode:str, pred:str, target: str):
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
        
        # print(nonVisitedNodes)
        for i in range (len(nonVisitedNodes)):
            
            curValue = graphX.nodes_dict[nonVisitedNodes[i]].distMin
            # print(curValue)
            # print(curValue)
            if curValue < lessDist:
                lessDist = curValue
                lessId = nonVisitedNodes[i]
        
        # visit graphX.nodes_dict[lessId]
        items = graphX.nodes_dict[lessId].adj.items()
        distTillAct: int = graphX.nodes_dict[lessId].distMin
        for j,k in ((items)):
            
            
            # if lessId == pred:
            #     print(f'PRED: lessId={lessId}, pred={pred}, j={j.id}, target={target}')
            
                # print(curValue)
            if (not (j.visited) and (j.id != target or lessId != pred)) :
                
                # if j.id == target:
                #     print(f'lessId={lessId}, pred={pred}, j={j.id}, target={target}, visited={graphX.nodes_dict[target].visited}')
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

    return

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
def path(finalNode:str, stdscr):
    global resultString
    create()
    #aristas javier

    #fila 50
    edgesFunct(graphJ,graphA)
    edgesFunct(graphJ1,graphA2)
    # print('a')

    #---------------------------------------------------------------
    #print("viene javier")
    #---------------------------------------------------------------
    # print('primer dijks')
    dijkstra(graphA, startNodeA)
    # print('segundo dijks')
    restrictedDijkstra(graphJ, startNodeJ, graphA.nodes_dict[finalNode].pred, finalNode)
    # print('tercer dijks')

    dijkstra(graphJ1, startNodeJ)
    # print('cuarto dijks')

    restrictedDijkstra(graphA2, startNodeA, graphJ1.nodes_dict[finalNode].pred, finalNode)


    destinatation :str = finalNode
    # print(graphA.nodes_dict)
    firstMax = max(graphA.nodes_dict[destinatation].distMin, graphJ.nodes_dict[destinatation].distMin)
    secondMax = max(graphJ1.nodes_dict[destinatation].distMin, graphA2.nodes_dict[destinatation].distMin)

    if(firstMax <= secondMax):
        pathAndreinaSum = graphA.nodes_dict[destinatation].distMin
        pathJavierSum = graphJ.nodes_dict[destinatation].distMin
        resultString = resultString + f'El tiempo mímimo de Javier es {pathJavierSum}min por {shortestPath(graphJ, graphJ.nodes_dict[destinatation])} \nEl tiempo mímimo de Andreina es {pathAndreinaSum}min por {shortestPath(graphA, graphA.nodes_dict[destinatation])}\n'
        
        
    else:
        pathAndreinaSum = graphA2.nodes_dict[destinatation].distMin
        pathJavierSum = graphJ1.nodes_dict[destinatation].distMin
    
        resultString = resultString +  f'El tiempo mímimo de Javier es {pathJavierSum}min por {shortestPath(graphJ1, graphJ1.nodes_dict[destinatation])} \nEl tiempo mímimo de Andreina es {pathAndreinaSum}min por {shortestPath(graphA2, graphA2.nodes_dict[destinatation])}\n'
    
    maximum(pathJavierSum,pathAndreinaSum, stdscr)
    return 
def menu():
    loop = "0"
    while loop == "0":
        print("Javier y Andreina deben escojer su destino.")
        print ("1. Ir al Brewery.")
        print ("2. Ir a la Disco.")
        print ("3. Ir al Bar.")
        destino = input("Ingrese 1,2 o 3, segun corresponda: ")
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
def menu2():
    classes = [Brewery, Disco, Bar]
    nombres = ["Cerveceria Mi Rolita", "Discoteca The Darkness", "Bar La Pasion"]
    decisiones = ["Ver otro recorrido", "Salir"]
    numeros = [1,0]
    def character(stdscr):

        bool = True
        while bool:
            global resultString
            resultString = ""
            attributes = {}
            curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
            attributes['normal'] = curses.color_pair(1)

            curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
            attributes['highlighted'] = curses.color_pair(2)

            c = 0  # last character read
            option = 0  # the current option that is marked
            while c != 10:  # Enter in ascii
                stdscr.erase()
                stdscr.addstr("Que recorrido quiere visualizar?\n", curses.A_UNDERLINE)
                for i in range(len(classes)):
                    if i == option:
                        attr = attributes['highlighted']
                    else:
                        attr = attributes['normal']
                    stdscr.addstr("{0}. ".format(i + 1))
                    stdscr.addstr(nombres[i] + '\n', attr)
                c = stdscr.getch()
                if c == curses.KEY_UP and option > 0:
                    option -= 1
                elif c == curses.KEY_DOWN and option < len(classes) - 1:
                    option += 1
            stdscr.erase()

            path(classes[option], stdscr)
            attributes = {}
            curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
            attributes['normal'] = curses.color_pair(1)

            curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
            attributes['highlighted'] = curses.color_pair(2)

            curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
            attributes['exit'] = curses.color_pair(3)

            c = 0  # last character read
            option = 0  # the current option that is marked
            while c != 10:  # Enter in ascii
                stdscr.erase()
                stdscr.addstr(f"\n\n{resultString}\n")
                stdscr.addstr("\n\n\nQue desea hacer?\n", curses.A_UNDERLINE)
                for i in range(len(decisiones)):
                    if i == option:
                        if option == 0:
                            attr = attributes['highlighted']
                        else:
                            attr = attributes['exit']
                    else:
                        attr = attributes['normal']
                    stdscr.addstr("{0}. ".format(i + 1))
                    stdscr.addstr(decisiones[i] + '\n', attr)
                c = stdscr.getch()
                if c == curses.KEY_UP and option > 0:
                    option -= 1
                elif c == curses.KEY_DOWN and option < len(decisiones) - 1:
                    option += 1
            
            if not (numeros[option]):
                bool = False

                

                
            
            
            
                

    def menucito():

        curses.wrapper(character)
    menucito()
def main():
    menu2()
        
        



main()
