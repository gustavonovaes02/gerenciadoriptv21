from flask import Flask, render_template, request, redirect

app = Flask(__name__)

clientes = []

@app.route('/')
def index():
    return render_template('index.html', clientes=clientes)

@app.route('/adicionar_cliente', methods=['POST'])
def adicionar_cliente():
    nome = request.form['nome']
    email = request.form['email']
    clientes.append({'nome': nome, 'email': email})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
