from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Estilo do Rei Barbearia"

@app.route('/novofuncionario')
def funcionario():
    return "funcionarioadicionado"

@app.route('/novocliente')
def cliente():
    return "clienteadicionado"

@app.route('/novoservico')
def servico():
    return "servicoadicionado"

@app.route('/novoagendamento')
def agendamento():
    return "agendamentoadicionado"
    





app.run(debug=True)

