import ply.lex as lex
from flask import Flask, render_template,request

app = Flask(__name__)

# Definir los tokens
tokens = {
    'for': 'Reservada For',
    'do': 'Reservada Do',
    'while': 'Reservada While',
    'if': 'Reservada If',
    'else': 'Reservada Else',
    '(': 'Paréntesis de apertura',
    ')': 'Paréntesis de cierre'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['code']
    lines = text.splitlines()
    results = []
    
    for i, line in enumerate(lines, start=1):
        words = line.split()
        for word in words:
            token = tokens.get(word, 'Desconocido')
            results.append({'line': i, 'token': token, 'symbol': word})
    
    return render_template('index.html', results=results, code=text)

if __name__ == '__main__':
    app.run(debug=True)