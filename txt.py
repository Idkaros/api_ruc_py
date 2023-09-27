import os
import sqlite as sq
import sqlite3


def insertar():
    # Carpeta actual
    carpeta_actual = os.getcwd()

    # Concatenar la ruta actual con la carpeta "txt_files"
    carpeta_txt = os.path.join(carpeta_actual, "txt_files")

    # Listar todos los archivos en la carpeta actual
    files = os.listdir(carpeta_txt)

    # Recorrer los archivos
    for file in files:
        # Validar que el archivo sea txt
        if file.endswith(".txt"):
            # Ruta de 1 archivo txt
            txt_file_path = os.path.join(carpeta_txt, file)

            # Abrir el archivo
            with open(txt_file_path, "r", encoding="utf-8") as archivo:
                # Recorrer las líneas
                for linea in archivo:
                    ruc, apellinombre, dv, codigo, estado, fin = linea.strip().split(
                        "|"
                    )
                    sq.insertar_txt(ruc, apellinombre, dv, codigo, estado)
            os.remove(txt_file_path)

def insertar1raVez():
    # Insertamos todo lo que está en los txt's, asumiendo que la BD está vacia

    # Carpeta actual
    carpeta_actual = os.getcwd()

    # Concatenar la ruta actual con la carpeta "txt_files"
    carpeta_txt = os.path.join(carpeta_actual, "txt_files")

    # Listar todos los archivos en la carpeta actual
    files = os.listdir(carpeta_txt)

    # Recorrer los archivos
    for file in files:
        # Validar que el archivo sea txt
        if file.endswith(".txt"):
            # Conectar a la base de datos
            conn = sqlite3.connect("ruc.db")
            cursor = conn.cursor()

            # Iniciar una transacción
            conn.execute("BEGIN")
            # Ruta de 1 archivo txt
            txt_file_path = os.path.join(carpeta_txt, file)

            # Abrir el archivo
            with open(txt_file_path, "r", encoding="utf-8") as archivo:
                # Recorrer las líneas
                for linea in archivo:
                    # Si hay más de 5 campos, saltar
                    if linea.count("|") > 5:
                        continue
                    
                    # Tomar datos de la línea
                    ruc, apellinombre, dv, codigo, estado, fin = linea.strip().split(
                        "|"
                    )

                    cursor.execute(
                        "INSERT INTO contribuyentes(ruc, apellinombre, dv, codigo, estado) VALUES (?, ?, ?, ?, ?)",
                        (ruc, apellinombre, dv, codigo, estado),
                    )

            # Comiteamos los datos y cerramos la conexión
            conn.commit()
            conn.close()

            # Eliminar el archivo txt
            os.remove(txt_file_path)