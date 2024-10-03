from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Definir los tokens
tokens = {
    'for': 'Reservada For',
    'public': 'Identificador',
    'static': 'Reservado',
    'main': 'Identificador',
    'do': 'Reservada Do',
    'while': 'Reservada While',
    'if': 'Reservada If',
    'else': 'Reservada Else',
    'return': 'Reservada Return',
    'int': 'Tipo Entero',
    'float': 'Tipo Flotante',
    'char': 'Tipo Carácter',
    'string': 'Tipo Cadena',
    '(': 'delimitador',
    ')': 'delimitador',
    '{': 'Llave de apertura',
    '}': 'Llave de cierre',
    '[': 'Corchete de apertura',
    ']': 'Corchete de cierre',
    ';': 'Punto y coma',
    ',': 'Coma',
    '+': 'Operador de suma',
    '-': 'Operador de resta',
    '*': 'Operador de multiplicación',
    '/': 'Operador de división',
    '=': 'Operador de asignación',
    '==': 'Operador de igualdad',
    '!=': 'Operador de desigualdad',
    '<': 'Operador menor que',
    '>': 'Operador mayor que',
    '<=': 'Operador menor o igual que',
    '>=': 'Operador mayor o igual que',
    '!': 'Operador de negación',
    '&&': 'Operador lógico AND',
    '||': 'Operador lógico OR',
    '++': 'Operador de incremento',
    '--': 'Operador de decremento'
}

# Historial de tokens analizados
history = []

@app.route('/')
def index():
    return render_template('index.html', results=[], code="", history=history)

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['code']
    lines = text.splitlines()
    results = []
    errors = []

    for i, line in enumerate(lines, start=1):
        words = line.split()
        for word in words:
            if word in tokens:
                result = f'LINEA {i} <{tokens[word]}> {word}'
                results.append(result)
                history.append(result)
            else:
                error_msg = f'LINEA {i} <Error Léxico> {word}'
                results.append(error_msg)
                history.append(error_msg)
                errors.append(error_msg)

    return render_template('index.html', results=results, code=text, history=history, errors=errors)

@app.route('/clear', methods=['POST'])
def clear():
    # Limpiar el historial
    history.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
