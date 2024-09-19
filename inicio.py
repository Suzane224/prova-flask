from flask import Flask,render_template,request,redirect,session,url_for,flash
from usuario import Usuario

app = Flask(__name__)
app.secret_key = 'supersecretkey' #substitua por uma chave secreta real

usuario1 = Usuario("Bruno Divino", "BD", "alohomora")
usuario2 = Usuario("Camila Ferreira", "Mila", "paozinho")
usuario3 = Usuario("Guilherme Louro", "Cake","python_eh_vida")

usuarios = {usuario1.nome : usuario1,
             usuario2.nome : usuario2,  
             usuario3.nome : usuario3 }


@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form ['usuario'] in usuarios:
        usuario = usuarios [request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nome
            return 'loguei'
        else:
            return 'erro na autenticacao web'

@app.route('/logout')
def sair():
    session.pop('usuario_logodo',None)
    return redirect(url_for('index'))




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

