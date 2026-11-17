class Graph:
    def __init__(self, Nodes):
        self.nodes = Nodes
        self.adjList = {}
        for node in self.nodes:
            self.adjList[node] = []

    def printGraph(self):
        for node in self.nodes:
            print(node, ":", self.adjList[node])

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)


myNode = ["A","B","C","D"]
myGraph = Graph(myNode)
myGraph.printGraph()
myGraph.addEdge("A","B")
myGraph.addEdge("A","D")
myGraph.addEdge("B","C")
myGraph.addEdge("B","D")
myGraph.addEdge("C","D")
myGraph.printGraph()