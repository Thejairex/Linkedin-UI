from flask import Flask, render_template, request, jsonify
import requests

from app.db import Jobs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/jobs')
def jobs():
    jobs = Jobs('static/db/jobs.db').select()
    return render_template('jobs.html', jobs=jobs)

@app.route('/cookies')
def cookies():
    return render_template('form.html')

@app.route('/upload_cookies', methods=['POST'])
def upload_cookies():
    file = request.files['cookies']
    files = {'cookies': (file.filename, file.stream, file.mimetype)}
    
    response = requests.post('http://192.168.1.5:5000/cookies', files=files)
    
    # Comprobar si la solicitud a FastAPI fue exitosa
    if response.status_code == 200:
        # Mostrar el mensaje de respuesta de FastAPI
        return {"message": "Las cookies se han guardado correctamente."}
    else:
            return jsonify({"error": "Error al subir archivo a FastAPI", "status_code": response.status_code})
    
    
if __name__ == '__main__':
    app.run(debug=True)