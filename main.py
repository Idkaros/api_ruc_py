import sqlite as sq
import txt
import zip as zp

def recrearBD():
    sq.eliminarBD()
    sq.crear_estruc()
    zp.unzip_ruc_files()
    txt.insertar1raVez()

recrearBD()
print("Finalizado.")