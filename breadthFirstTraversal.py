#still in progress

def breadthFirstTraversal(visitedNodes, graph, start):
    if start not in visitedNodes:
        visitedNodes.append(start)
        print(start, end=" ")
    for node in graph[start]:
        if node not in visitedNodes:
            print(node, end=" ")
    for node in graph[start]:
        if node not in visitedNodes:
            visitedNodes.append(node)
            breadthFirstTraversal(visitedNodes, graph, node)


graph = {'A' : ['B','C','D'],
         'B' : ['A'],
         'C' : ['A','E','F'],
         'D' : ['A','F'],
         'E' : ['C','F'],
         'F' : ['C','D'],
         }

visited = []
breadthFirstTraversal(visited, graph, 'A')