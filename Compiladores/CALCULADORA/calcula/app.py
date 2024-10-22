from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Función para analizar la expresión
def analizar_expresion(expresion):
    operadores = {'+': 'PLUS', '-': 'MINUS', '*': 'TIMES', '/': 'DIVIDE'}
    tokens = []
    
    def construir_arbol(expr):
        expr = expr.strip()
        if '*' in expr or '/' in expr:
            for op in '*/':
                if op in expr:
                    partes = expr.rsplit(op, 1)
                    return [op, construir_arbol(partes[0]), construir_arbol(partes[1])]
        elif '+' in expr or '-' in expr:
            for op in '+-':
                if op in expr:
                    partes = expr.rsplit(op, 1)
                    return [op, construir_arbol(partes[0]), construir_arbol(partes[1])]
        else:
            return expr

    arbol = construir_arbol(expresion)
    
    linea = 1
    for token in re.findall(r'\d+\.\d+|\d+|[\+\-\*/]', expresion):
        if re.match(r'\d+\.\d+', token):  # Para números decimales
            tokens.append(f"LINEA {linea}, TOKEN = \"NUMBER\", DECIMAL = \"{token}\"")
        elif token.isdigit():
            tokens.append(f"LINEA {linea}, TOKEN = \"NUMBER\", DIGITO = \"{token}\"")
        elif token in operadores:
            tokens.append(f"LINEA {linea}, TOKEN = \"{operadores[token]}\", OPERADOR = \"{token}\"")
        linea += 1
    
    return tokens, arbol


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        resultado = eval(expression)  # Calculamos el resultado de la expresión
        tokens, _ = analizar_expresion(expression)  # Realizamos el análisis léxico
        
        return jsonify({
            'resultado': resultado,
            'tokens': tokens  # Incluimos los tokens en la respuesta JSON
        })
    except Exception as e:
        return jsonify({
            'resultado': 'Error',
            'tokens': []
        })

@app.route('/generate_tree', methods=['POST'])
def generate_tree():
    expression = request.form['expression']
    try:
        _, arbol = analizar_expresion(expression)
        return jsonify({
            'arbol': arbol
        })
    except Exception as e:
        return jsonify({
            'arbol': []
        })

if __name__ == '__main__':
    app.run(debug=True)
