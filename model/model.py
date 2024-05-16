import networkx as nx
from database.DAO import DAO


class Model:

    def __init__(self):
        self._countryList = DAO.getAllCountry()
        self._grafo = nx.Graph()
        # self._grafo.add_nodes_from(self._countryList)
        self._idMap = {}
        for c in self._countryList:
            self._idMap[c.CCode] = c

    def creaGrafo(self, anno):
        self.addEdges(anno)

    def addEdges(self, anno):
        self._grafo.clear_edges()
        allEdges = DAO.getAllConnection(anno)
        for c in allEdges:
            self._grafo.add_node(self._idMap[c.state1no])
            self._grafo.add_node(self._idMap[c.state2no])
            if c.conttype == 1:
                self._grafo.add_edge(self._idMap[c.state1no], self._idMap[c.state2no])

    def createTree(self, stateName):
        firstNode = ""
        for e in self._idMap.values():
            if e.StateNme == stateName:
                firstNode = self._idMap[e.CCode]
                break
        tree = nx.dfs_tree(self._grafo, firstNode)
        return tree

    def dfs_recursive(self, country, visited):
        visited.append(country)

        for n in self._grafo.neighbors(country):
            if n not in visited:
                self.dfs_recursive(n, visited)
        return visited
