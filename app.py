from flask import Flask, render_template, request, jsonify
from chatbot import responder 
import os

app = Flask(__name__, static_folder='pagina', template_folder='pagina')

# Rota para a interface principal (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para receber mensagens e retornar respostas do chatbot
@app.route('/mensagem', methods=['POST'])
def mensagem():
    mensagem_usuario = request.form['mensagem']
    resposta_chatbot = responder(mensagem_usuario)  # Chama a função que você criou no chatbot.py
    return jsonify({'resposta': resposta_chatbot})

if __name__ == '__main__':
    app.run(debug=True)
