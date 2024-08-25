#Karla Carolina Lopez Ruiz
# A221641
#18/08/2024
# 50 Tokens,Lexema, Patron.

import re

# Definir los patrones de tokens
token_patterns = {
    'FOR': r'\bfor\b',
    'WHILE': r'\bwhile\b',
    'IF': r'\bif\b',
    'ELSE': r'\belse\b',
    'RETURN': r'\breturn\b',
    'DEF': r'\bdef\b',
    'CLASS': r'\bclass\b',
    'IMPORT': r'\bimport\b',
    'FROM': r'\bfrom\b',
    'AND': r'\band\b',
    'OR': r'\bor\b',
    'NOT': r'\bnot\b',
    'TRUE': r'\bTrue\b',
    'FALSE': r'\bFalse\b',
    'NONE': r'\bNone\b',
    'IN': r'\bin\b',
    'IS': r'\bis\b',
    'PASS': r'\bpass\b',
    'BREAK': r'\bbreak\b',
    'CONTINUE': r'\bcontinue\b',
    'TRY': r'\btry\b',
    'EXCEPT': r'\bexcept\b',
    'FINALLY': r'\bfinally\b',
    'WITH': r'\bwith\b',
    'AS': r'\bas\b',
    'ASSERT': r'\bassert\b',
    'LAMBDA': r'\blambda\b',
    'DEL': r'\bdel\b',
    'YIELD': r'\byield\b',
    'GLOBAL': r'\bglobal\b',
    'NONLOCAL': r'\bnonlocal\b',
    'NUMERO': r'\d+',
    'IDENTIFICADOR': r'[A-Za-z_]\w*',
    'SUMA': r'\+',
    'RESTA': r'-',
    'MULTIPLICACION': r'\*',
    'DIVISION': r'/',
    'MODULO': r'%',
    'POTENCIA': r'\\',
    'IGUAL': r'=',
    'DOBLE_IGUAL': r'==',
    'MAYOR_QUE': r'>',
    'MENOR_QUE': r'<',
    'MAYOR_IGUAL': r'>=',
    'MENOR_IGUAL': r'<=',
    'DIFERENTE': r'!=',
    'PARENTESIS_IZQ': r'\(',
    'PARENTESIS_DER': r'\)',
    'LLAVE_IZQ': r'\{',
    'LLAVE_DER': r'\}',
    'CORCHETE_IZQ': r'\[',
    'CORCHETE_DER': r'\]',
    'COMA': r',',
    'PUNTO_Y_COMA': r';',
    'PUNTO': r'\.',
    'DOS_PUNTOS': r':',
    'COMILLAS_SIMPLES': r"'",
    'COMILLAS_DOBLES': r'"',
    'ESPACIO': r'\s+',
    'SIMBOLO': r'.',  # Otros caracteres
}

# Compilar expresiones regulares
compiled_patterns = [(name, re.compile(pattern)) for name, pattern in token_patterns.items()]

def tokenize(code):
    position = 0
    tokens = []
    token_count = 0

    while position < len(code):
        match = None
        for name, pattern in compiled_patterns:
            match = pattern.match(code, position)
            if match:
                lexeme = match.group(0)
                if name != 'ESPACIO':
                    token_count += 1
                    tokens.append((token_count, name, lexeme, token_patterns[name]))
                position = match.end()
                break
        
        if not match:
            raise RuntimeError(f'Error de análisis en la posición {position}')
    
    return tokens

# Código de ejemplo con 50 tokens
code = (
    "for i in range(10):\n"
    "    if i % 2 == 0:\n"
    "        print(i)\n"
    "while x < 100:\n"
    "    x += 1\n"
    "return x + 42\n"
    "def foo():\n"
    "    pass\n"
    "a = 5 + 2 * (3 - 1) ** 2 / 4"
)

tokens = tokenize(code)

# Imprimir tokens, lexemas y patrones numerados
for token in tokens:
    print(f"{token[0]}. Token: {token[1]}, Lexema: '{token[2]}', Patrón: '{token[3]}'")