# zip.py
import zipfile
import os

def unzip_ruc_files():
	#1 Recorrer archivos zip
	#2	 Descomprimir(origen, destino)
	#3	 Eliminar archivo zip

	# Carpeta actual
	carpeta_actual = os.getcwd()

	# Concatenar la ruta actual con la carpeta "txt_files"
	carpeta_txt = os.path.join(carpeta_actual, 'txt_files')
	if not os.path.exists(carpeta_txt): os.makedirs(carpeta_txt)

	# Concatenar la ruta actual con la carpeta "zip_files"
	carpeta_zip = os.path.join(carpeta_actual, 'zip_files')
	if not os.path.exists(carpeta_zip): os.makedirs(carpeta_zip)

	# Listar todos los archivos en la carpeta "zip_files"
	files = os.listdir(carpeta_zip)

	#1 Recorrer los archivos
	for file in files:
		if file.endswith(".zip"):
			zip_file_path = os.path.join(carpeta_zip, file)

			#2 Crear un objeto ZipFile y descomprimir el archivo ZIP
			with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
				zip_ref.extractall(carpeta_txt)

			##3 Eliminar el archivo ZIP después de descomprimirlo
			#os.remove(zip_file_path)
