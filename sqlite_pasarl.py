import os
import sqlite3

BD_PASARELA = "ruc_pasarl.db"

def crear_estruc():
    # Conectar a la BD o crearla si no existe
    conn = sqlite3.connect(BD_PASARELA)

    cursor = conn.cursor()

    # Crear una tabla
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS contribuyentes (
            id INTEGER PRIMARY KEY,
            ruc INTEGER,
            nombre TEXT,
            dv INTEGER,
            codigo TEXT,
            estado TEXT
        )
        """
    )
    # # Crear indice
    # cursor.execute('CREATE INDEX idx_contribuyentes_ruc ON contribuyentes(ruc)')
    conn.commit()
    conn.close()

def eliminarBD():
    if os.path.exists(BD_PASARELA):
        os.remove(BD_PASARELA)
        print("BD eliminada")