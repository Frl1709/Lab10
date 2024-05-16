import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()
        anno = self._view._txtAnno.value
        try:
            intYear= int(anno)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Il valore inserito non è un intero."))
            self._view.update_page()
            return

        self._model.creaGrafo(intYear)
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {nx.number_connected_components(self._model._grafo)} componenti connessi"))
        lista = []
        for node in self._model._grafo.nodes:
            lista.append((node.StateAbb ,node.StateNme,self._model._grafo.degree[node]))
        sorted_list = sorted(lista, key=lambda x: x[0])
        self._view._txt_result.controls.append(ft.Text("Elenco degli stati:"))
        for e in sorted_list:
            self._view._txt_result.controls.append(ft.Text(f"{e[1]} -- {e[2]} vicini"))
        self._view.update_page()

    def fillDD(self):
        for c in self._model._countryList:
            self._view._ddStato.options.append(ft.dropdown.Option(c.StateNme))

    def handleRaggiungibili(self, e):
        stateName = self._view._ddStato.value
        tree = self._model.createTree(stateName)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Partendo dallo stato {stateName} è possibile raggiungere: "))
        for e in tree.nodes:
            if e.StateNme != stateName:
                self._view._txt_result.controls.append(ft.Text(f"{e.StateNme}"))
        self._view.update_page()

    def recursiveRaggiungibili(self, e):
        stateName = self._view._ddStato.value
        firstNode = ""
        for e in self._model._idMap.values():
            if e.StateNme == stateName:
                firstNode = self._model._idMap[e.CCode]
                break
        res = self._model.dfs_recursive(firstNode, [])
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Partendo dallo stato {stateName} è possibile raggiungere: "))
        for e in res:
            if e.StateNme != stateName:
                self._view._txt_result.controls.append(ft.Text(f"{e.StateNme}"))
        self._view.update_page()
