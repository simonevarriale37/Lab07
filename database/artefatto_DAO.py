
from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

# Creo un metodo per leggere gli artefatti filtrati per museo e epoca
    @staticmethod
    def leggi_artefatti_filtrati(id_museo=None, epoca=None):
        # Mi connetto al database senza creare un'istanza
        connessione = ConnessioneDB.get_connection()
        # Creo un cursore di tipo dictionary
        cursor = connessione.cursor(dictionary=True)
        # Metto come where nella query il fatto che se id_museo è null, allora ignora
        # il filtro sul museo e la stessa cosa per l'epoca
        query = '''SELECT * FROM artefatto 
                    WHERE (%s IS NULL OR id_museo = %s) 
                    AND (%s IS NULL OR epoca = %s)
                    ORDER BY nome
        '''
        # Metto due volte id_museo e epoca perchè uno deve verificare se è null e
        # l'altro va a confrontarlo con il campo del database
        cursor.execute(query, (id_museo, id_museo, epoca, epoca))
        # Creo una lista vuota
        artefatti = []
        # Leggo tutte le righe restituite dalla query, creo un nuovo oggetto Artefatto
        # e lo appendo alla lista artefatti
        for row in cursor.fetchall():
            artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"], row["id_museo"])
            artefatti.append(artefatto)
        cursor.close()
        connessione.close()
        return artefatti
    @staticmethod
    def leggi_epoche():
        connessione = ConnessioneDB.get_connection()
        cursor = connessione.cursor()
        # Prendo tutte le epoche distinte e ordinate in ordine alfabetico
        query = '''SELECT DISTINCT epoca FROM artefatto ORDER BY epoca'''
        cursor.execute(query)
        epoche = []
        for row in cursor.fetchall():
            epoche.append(row[0])
        cursor.close()
        connessione.close()
        return epoche