from flask import Flask, render_template, request

app = Flask(__name__)

# Tokens para palabras reservadas, símbolos, y otros
reserved_words = {'int', 'float', 'if', 'else', 'for', 'while', 'return', 'printf'}
symbols = {'+', '-', '*', '/', '=', '(', ')', '{', '}', ';'}
numbers = '0123456789'

def is_reserved_word(token):
    return token in reserved_words

def is_symbol(token):
    return token in symbols

def is_number(token):
    return token.isdigit()

def analyze_lexical(code):
    # Separar el código en tokens por espacios y símbolos
    tokens = []
    current_token = ""
    for char in code:
        if char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ""
        elif is_symbol(char):
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
        else:
            current_token += char

    if current_token:
        tokens.append(current_token)

    # Clasificación de tokens
    lexical_results = []
    for token in tokens:
        lexical_results.append({
            'token': token,
            'reservada': 'x' if is_reserved_word(token) else '',
            'identificador': 'x' if not is_reserved_word(token) and not is_symbol(token) and not is_number(token) else '',
            'simbolo': 'x' if is_symbol(token) else '',
            'numero': 'x' if is_number(token) else ''
        })
    
    return lexical_results

def analyze_syntactic(code):
    stack = []
    errors = []

    # Dividir el código en líneas
    lines = code.splitlines()

    for line_num, line in enumerate(lines, start=1):
        # Verificar paréntesis y llaves
        for i, char in enumerate(line):
            if char in ['(', '{']:
                stack.append((char, line_num))
            elif char == ')':
                if not stack or stack[-1][0] != '(':
                    errors.append(f"Error de sintaxis: Paréntesis ')' en línea {line_num}, posición {i + 1} no tiene apertura.")
                else:
                    stack.pop()
            elif char == '}':
                if not stack or stack[-1][0] != '{':
                    errors.append(f"Error de sintaxis: Llave '}}' en línea {line_num}, posición {i + 1} no tiene apertura.")
                else:
                    stack.pop()

        # Verificar si la línea termina con ';' si es necesario
        stripped_line = line.strip()
        if stripped_line and not stripped_line.endswith(';') and not stripped_line.endswith('}') and not stripped_line.startswith('printf'):
            errors.append(f"Error de sintaxis: Falta ';' al final de la línea {line_num}.")

        # Verificación de la función printf
        if "printf" in stripped_line and not stripped_line.endswith(');'):
            errors.append(f"Error de sintaxis: La llamada a 'printf' en línea {line_num} no está cerrada correctamente con ');'.")

        # Verificar operadores mal colocados como '+++'
        if '+++' in stripped_line or '--' in stripped_line:
            errors.append(f"Error de sintaxis: Uso incorrecto de operadores en línea {line_num}.")

    # Verificación de paréntesis y llaves no cerradas
    if stack:
        for symbol, line_num in stack:
            errors.append(f"Error de sintaxis: '{symbol}' en línea {line_num} no tiene cierre.")

    return errors

@app.route("/", methods=["GET", "POST"])
def index():
    code = ""
    lexical_results = []
    syntax_errors = []

    if request.method == "POST":
        code = request.form['code']
        lexical_results = analyze_lexical(code)
        syntax_errors = analyze_syntactic(code)

    return render_template("index.html", code=code, lexical_results=lexical_results, syntax_errors=syntax_errors)

if __name__ == "__main__":
    app.run(debug=True)
