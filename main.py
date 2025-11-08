import flet as ft

from model.model import Model
from UI.view import View
from UI.controller import Controller


def main(page: ft.Page):
    my_model = Model()
    my_view = View(page)
    my_controller = Controller(my_view, my_model)
    my_view.set_controller(my_controller)
    my_view.load_interface()
    # Aggiungo il metodo del controller per riempire i dropdown della view con i dati
    # presi dal database
    my_controller.popola_dropdown()


ft.app(target=main)
