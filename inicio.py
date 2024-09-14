from flask import Flask,render_template,request,redirect,session,url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey' #substitua por uma chave secreta real

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/autenticar',methods=['POST','GET'])
Def autenticar():
    if request.method =='POST':
        if request.form['senha'] == 'senac' and request.form['usuario'] =='walter':
            return 'logado com sucesso'
        else:
            return 'erro na autenticacao'

@app.route('/logout')
def saur():
    session.pop('usuario_logodo',None)
    return redirect(url_for('index'))

app.run(debug.true)


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

