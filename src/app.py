from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({
        "Universidad": "UTPL",
        "Curso": "Procesos de Ingenieria de Software",
        "Periodo": "Abr/Ago 2021",
        "Lenguaje de programacion preferido": "Javascript",
        "Aspiracion PostGraduacon": "Arquitecto de Software"
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
