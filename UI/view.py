import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        # Metto il dropdown per selezionare i musei
        self.museo_dropdown = ft.Dropdown(width=200)
        # Metto il dropdown per selezionare le epoche
        self.epoca_dropdown = ft.Dropdown(width=200)
        # Metto il bottone per mostrare gli artefatti
        self.mostra_artefatti_btn = ft.ElevatedButton(text="Mostra Artefatti")
        # Imposto la listview per visualizzare gli artefatti
        self.artefatti_listview = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)


    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # Metto la riga dei dropdown del museo e delle epoche
        filtro = ft.Row(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Museo:"), self.museo_dropdown,
                        ft.Text("Epoca:"), self.epoca_dropdown,
                    ],
                    spacing=90,
                ),],)
        # Metto la riga del bottone mostra artefatti
        bottone = ft.Row(
            controls=[self.mostra_artefatti_btn,],
            alignment="center",
            spacing=10,
        )
        # Sezione 3: Artefatti
        # Metto un contenitore per la lista degli artefatti
        artefatti_container = ft.Column(
            controls=[self.artefatti_listview], expand=True
        )

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # Imposto il layout
            filtro,
            bottone,
            ft.Divider(),

            # Sezione 3: Artefatti
            artefatti_container
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
