import os
import sqlite as sq
import sqlite3
#import datetime

# Definir BD de producción
BD_PASARELA = "ruc_pasarl.db"

BD_PRODUCCION = "ruc_produc.db"

# Carpeta actual
carpeta_actual = os.getcwd()

# Concatenar la ruta actual con la carpeta "txt_files"
carpeta_txt = os.path.join(carpeta_actual, "txt_files")

#def insertar():
#
#    # Listar todos los archivos en la carpeta actual
#    files = os.listdir(carpeta_txt)
#
#    # Recorrer los archivos
#    for file in files:
#        # Validar que el archivo sea txt
#        if file.endswith(".txt"):
#            # Ruta de 1 archivo txt
#            txt_file_path = os.path.join(carpeta_txt, file)
#
#            # Abrir el archivo
#            with open(txt_file_path, "r", encoding="utf-8") as archivo:
#                # Recorrer las líneas
#                for linea in archivo:
#                    ruc, nombre, dv, codigo, estado, fin = linea.strip().split(
#                        "|"
#                    )
#                    sq.insertar_txt(ruc, nombre, dv, codigo, estado)
#            os.remove(txt_file_path)


def insertar1raVez():
    # Insertamos todo lo que está en los txt's, asumiendo que la BD está vacia

    # Listar todos los archivos en la carpeta actual
    files = os.listdir(carpeta_txt)

    # Recorrer los archivos
    for file in files:
        # Validar que el archivo sea txt
        if file.endswith(".txt"):
            # Conectar a la base de datos
            conn = sqlite3.connect(BD_PASARELA)
            cursor = conn.cursor()

            # Iniciar una transacción
            conn.execute("BEGIN")
            # Ruta de 1 archivo txt
            txt_file_path = os.path.join(carpeta_txt, file)

            # Abrir el archivo
            with open(txt_file_path, "r", encoding="utf-8") as archivo:
                # Recorrer las líneas
                for linea in archivo:

                    if "6681449||" in linea:
                        linea = linea.replace("6681449||", "6681449|")
                    elif linea.count("|") == 6:
                        linea = linea.replace("||", "|")
                        linea = linea.replace("M|LLER", "MULLER")
                        linea = linea.replace("N|", "N")
                        linea = linea.replace("KASPROWICZ|", "KASPROWICZ")

                    # Si hay más de 5 campos, saltar
                    if linea.count("|") > 5:
                        escribir_error(linea)
                        continue

                    # Tomar datos de la línea
                    ci_ruc, nombre_razon, dv, codigo, estado, fin = linea.strip().split("|")

                    cursor.execute(
                        "INSERT INTO contribuyentes(ruc, nombre, dv, codigo, estado) VALUES (?, ?, ?, ?, ?)",
                        (ci_ruc, nombre_razon, dv, codigo, estado),
                    )

            # Comiteamos los datos y cerramos la conexión
            conn.commit()
            conn.close()

            # # Eliminar el archivo txt
            # os.remove(txt_file_path)

def insertar_producc():
    # Insertamos desde la BD de pasarela a producción ordenado alfabéticamente por nombre

    # Connect to the BD_PASARELA database
    conn_pasarela = sqlite3.connect(BD_PASARELA)
    cursor_pasarela = conn_pasarela.cursor()

    # Connect to the BD_PRODUCCION database
    conn_produccion = sqlite3.connect(BD_PRODUCCION)
    cursor_produccion = conn_produccion.cursor()

    # Read all records from the contribuyentes table in BD_PASARELA, ordered by name
    cursor_pasarela.execute("SELECT ruc, nombre, dv, codigo, estado FROM contribuyentes ORDER BY ruc")
    records = cursor_pasarela.fetchall()

    # Insert all records into the contribuyentes table in BD_PRODUCCION
    cursor_produccion.executemany("INSERT INTO contribuyentes(ruc, nombre, dv, codigo, estado) VALUES (?, ?, ?, ?, ?)", records)
    #cursor_produccion.executemany("INSERT INTO contribuyentes VALUES (ruc, nombre, dv, codigo, estado)", records)

    # Commit the changes and close the connections
    conn_produccion.commit()
    conn_produccion.close()
    conn_pasarela.close()

def escribir_error(texto):
    try:
        #fecha_hora_actual = datetime.datetime.now()
        #nombre_fecha = fecha_hora_actual.strftime("%y%m%d_%H%M%S")
        error_file_path = os.path.join(carpeta_actual, f"RUCs con errores.txt")
        with open(error_file_path, "a") as archivo:
            archivo.write(texto)
        print(f"Se ha escrito el texto en el archivo: {error_file_path}")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")


def validar_primera_ocurrencia(string, palabra_a_buscar):
    # Utiliza una expresión regular para buscar la palabra al comienzo de la cadena
    pattern = f"^{re.escape(palabra_a_buscar)}"
    if re.search(pattern, string):
        return True
    return False
