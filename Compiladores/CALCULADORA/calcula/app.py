from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

ultimo_resultado = None  # Variable global para guardar el último resultado

# Función para analizar la expresión
def analizar_expresion(expresion):
    operadores = {'+': 'PLUS', '-': 'MINUS', '*': 'TIMES', '/': 'DIVIDE'}
    tokens = []

   # Función para construir el árbol respetando precedencia de operadores
    def construir_arbol(expr):
        expr = expr.strip()
        
        # Primero chequeamos sumas y restas (menor precedencia)
        if '+' in expr or '-' in expr:
            for op in '+-':
                if op in expr:
                    partes = expr.rsplit(op, 1)  # Dividimos en dos partes
                    return [op, construir_arbol(partes[0]), construir_arbol(partes[1])]
        
        # Luego chequeamos multiplicación y división (mayor precedencia)
        elif '*' in expr or '/' in expr:
            for op in '*/':
                if op in expr:
                    partes = expr.rsplit(op, 1)  # Dividimos en dos partes
                    return [op, construir_arbol(partes[0]), construir_arbol(partes[1])]
        
        else:
            return expr  # Caso base: si no hay más operadores, devolver el número
    
    # Generar árbol de derivación a partir de la expresión
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
    global ultimo_resultado
    expression = request.form['expression']
    try:
        resultado = eval(expression)  # Calculamos el resultado de la expresión
        tokens, _ = analizar_expresion(expression)  # Realizamos el análisis léxico

        ultimo_resultado = resultado  # Guardar el último resultado
        return jsonify({
            'resultado': resultado,
            'tokens': tokens
        })
    except Exception as e:
        return jsonify({
            'resultado': 'Error',
            'tokens': []
        })

@app.route('/get_last_result', methods=['GET'])
def get_last_result():
    global ultimo_resultado
    return jsonify({
        'ultimo_resultado': ultimo_resultado if ultimo_resultado is not None else ''
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

