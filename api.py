import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import zipfile

app = Flask(__name__)

# Establecer la carpeta de carga para los archivos ZIP
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'zip'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/zips', methods=['POST'])
def upload_zips():
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha proporcionado ningún archivo'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'Nombre de archivo vacío'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'message': 'Archivo ZIP subido correctamente'}), 201
    else:
        return jsonify({'error': 'Extensión de archivo no permitida, debe ser .zip'}), 400

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
    app.run()