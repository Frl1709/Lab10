import networkx as nx

from database.DAO import DAO
from model.model import Model

res = DAO.getAllCountry()
res1 = DAO.getAllConnection(1980)
model = Model()

model.creaGrafo(1980)
grafo = model._grafo
code = ""
stateName = "Afghanistan"
tree = model.createTree(stateName)
for e in tree.nodes:
    print(e)

print(res)
print(len(res1))
print(nx.number_connected_components(grafo))
