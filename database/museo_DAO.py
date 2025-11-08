
from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass



    @staticmethod
    def leggi_musei():
        # Mi connetto al database senza creare un'istanza
        connessione = ConnessioneDB.get_connection()
        # Creo un cursore di tipo dictionary perchè così ogni riga dei risultati
        # viene restituita sotto forma di un dizionario
        cursor = connessione.cursor(dictionary=True)
        query = "SELECT * FROM museo"
        cursor.execute(query)
        # Inizializzo una lista vuota
        musei = []
        # Leggo tutte le righe restituite dalla query, creo un nuovo oggetto Museo
        # e lo appendo alla lista musei
        for row in cursor.fetchall():
            museo = Museo(row["id"], row["nome"], row["tipologia"])
            musei.append(museo)
        cursor.close()
        connessione.close()
        return musei
