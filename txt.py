import os
import sqlite as sq
import sqlite3
#import datetime

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
