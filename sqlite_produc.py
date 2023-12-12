import os
import sqlite3

BD_PRODUCCION = "ruc_produc.db"

def crear_estruc():
    # Conectar a la BD o crearla si no existe
    conn = sqlite3.connect(BD_PRODUCCION)

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

    # Crear indice
    cursor.execute('CREATE INDEX idx_contribuyentes_ruc ON contribuyentes(ruc)')
    conn.commit()
    conn.close()

def eliminarBD():
    if os.path.exists(BD_PRODUCCION):
        os.remove(BD_PRODUCCION)
        print("BD eliminada")

def obtener_contribuyentes(ruc):
    conn = sqlite3.connect(BD_PRODUCCION)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT ruc || '-' || dv AS "ruc", nombre, estado
        FROM contribuyentes
        WHERE ruc LIKE ?
        """, (f'%{ruc}%',)
    )
    contribuyente = cursor.fetchall()
    conn.close()
    return contribuyente
