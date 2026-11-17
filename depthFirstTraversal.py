visited = []
def depthFirstTraversal(graph, start, visitedList):
    if start not in visitedList:
        visitedList.append(start)
        print(start, end=" ")
        for node in graph[start]:
            if node not in visitedList:
                depthFirstTraversal(graph, node, visitedList)


graph = {
    'A' : ['B','C','D'],
    'B' : ['A', 'E', 'F'],
    'C' : [],
    'D' : ['A','G', 'H'],
    'E' : ['B'],
    'F' : ['B'],
    'G' : ['B'],
    'H' : ['B']
}

depthFirstTraversal(graph, 'A', visited)
