import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Establecer la carpeta de carga para los archivos ZIP
UPLOAD_FOLDER = 'zip_files'
ALLOWED_EXTENSIONS = {'zip'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/zips', methods=['POST'])
def upload_zips():
    if 'files' not in request.files:
        return jsonify({'error': 'No se ha proporcionado ningún archivo'}), 400
    
    files = request.files.getlist('files')
    
    for file in files:
        if file.filename == '':
            return jsonify({'error': 'Nombre de archivo vacío'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Extensión de archivo no permitida, debe ser .zip'}), 400
        
    for file in files:        
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    return jsonify({'message': 'Archivos ZIP subidos exitosamente'}), 201

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
    app.run()