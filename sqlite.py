import os
import sqlite3

BD_PRODUCCION = "ruc.db"

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

# def insertar_txt():
#     # 1 Recorremos los txt
#     # 2   Recorremos las líneas
#     # 3     Insertamos solo los contribuyentes nuevos

#     conn = sqlite3.connect(BD_PRODUCCION)

#     cursor = conn.cursor()

#     # Carpeta actual
#     carpeta_actual = os.getcwd()

#     # Listar todos los archivos en la carpeta actual
#     files = os.listdir(carpeta_actual)

#     # Recorrer los archivos
#     for file in files:
#         # Validar que el archivo sea txt
#         if file.endswith(".txt"):
#             # Abrir el archivo
#             with open(file, "r") as archivo:
#                 # Recorrer las líneas
#                 for linea in archivo:
#                     ruc, nombre, dv, codigo, estado = linea.strip().split("|")
#                     cursor.execute(
#                         "INSERT INTO contribuyentes(ruc, nombre, dv, codigo, estado) VALUES (?, '?', ?, ?, ?)",
#                         (ruc, nombre, dv, codigo, estado),
#                     )

# def insertar_txt(ruc, nombre, dv, codigo, estado):
#     conn = sqlite3.connect(BD_PRODUCCION)
#     cursor = conn.cursor()
#     cursor.execute(
#         "SELECT COUNT(*) FROM contribuyentes WHERE ruc LIKE ?", ("%" + ruc + "%",)
#     )

#     resultado = cursor.fetchone()
#     conn.close()
#     if resultado[0] == 0:
#         __insertar_contribuyente(ruc, nombre, dv, codigo, estado)

# def __insertar_contribuyente(ruc, nombre, dv, codigo, estado):
#     conn = sqlite3.connect(BD_PRODUCCION)
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT INTO contribuyentes(ruc, nombre, dv, codigo, estado) VALUES (?, ?, ?, ?, ?)",
#         (ruc, nombre, dv, codigo, estado),
#     )
#     conn.commit()
#     conn.close()

def eliminarBD():
    if os.path.exists(BD_PRODUCCION):
        os.remove(BD_PRODUCCION)
        print("BD eliminada")