import sqlite as sq
import txt
import zip as zp

zp.unzip_ruc_files()
sq.crear_estruc()
txt.insertar1raVez()
print("Archivos ZIP descomprimidos y eliminados exitosamente.")