from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # Controllo se il filtro museo è Nessun filtro, vuoto o None
        if museo == "Nessun filtro" or museo == "" or museo is None:
            museo_id = None
        else:
            museo_id = None
            # Leggo tutti i musei
            lista_musei = self._museo_dao.leggi_musei()
            # Cerco l'id del museo corrispondente al nome selezionato
            for m in lista_musei:
                if m.nome == museo:
                    museo_id = m.id
                    break
        # Controllo se il filtro epoca è Nessun filtro, vuoto o None
        if epoca == "Nessun filtro" or epoca == "" or epoca is None:
            epoca = None
        # Leggo gli artefatti filtrati
        artefatti = self._artefatto_dao.leggi_artefatti_filtrati(museo_id, epoca)
        return artefatti

    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        return self._artefatto_dao.leggi_epoche()

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        return self._museo_dao.leggi_musei()

