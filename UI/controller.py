import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None
        self.popola_dropdown()
        self._view.mostra_artefatti_btn.on_click = self.mostra_artefatti

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        # Pulisco eventuali opzioni già presenti
        self._view.museo_dropdown.options.clear()
        # Aggiungo l'opzione iniziale 'Nessun filtro'
        self._view.museo_dropdown.options.append(ft.dropdown.Option("Nessun filtro"))
        # prendo la lista dei musei dal model
        musei = self._model.get_musei()
        # Aggiungo ogni museo alla lista del dropdown
        for m in musei:
            self._view.museo_dropdown.options.append(ft.dropdown.Option(m.nome))
        # Imposto come valore di default 'Nessun filtro'
        self._view.museo_dropdown.value = "Nessun filtro"
        # Collego il metodo di callback da eseguire quando cambia la selezione del museo
        self._view.museo_dropdown.on_change = self.museo_changed
        # Faccio la stessa cosa anche per le epoche
        self._view.epoca_dropdown.options.clear()
        self._view.epoca_dropdown.options.append(ft.dropdown.Option("Nessun filtro"))
        epoche = self._model.get_epoche()
        for e in epoche:
            self._view.epoca_dropdown.options.append(ft.dropdown.Option(e))
        self._view.epoca_dropdown.value = "Nessun filtro"
        self._view.epoca_dropdown.on_change = self.epoca_changed

    # CALLBACKS DROPDOWN
    def museo_changed(self, e):
        # Aggiorna la variabile con il museo selezionato dal dropdown
        self.museo_selezionato = e.control.value
    def epoca_changed(self, e):
        # Aggiorna la variabile con l'epoca selezionata dal dropdown
        self.epoca_selezionata = e.control.value

    # AZIONE: MOSTRA ARTEFATTI
    def mostra_artefatti(self, e: ft.ControlEvent):
        # Prendo gli artefatti filtrati dal model
        artefatti = self._model.get_artefatti_filtrati(
            self.museo_selezionato,
            self.epoca_selezionata,
        )
        self._view.artefatti_listview.controls.clear()
        # Se la lista è vuota mostra l'alert altrimenti aggiunge ogni artefatto come riga
        if len(artefatti) == 0:
            self._view.show_alert("Nessun artefatto trovato")
        else:
            for a in artefatti:
                self._view.artefatti_listview.controls.append(ft.Text(str(a)))
        self._view.update()
