import re
import random
import string

def generar_curp(nombre, primer_apellido, segundo_apellido, año, mes, dia, sexo, estado):
    curp = primer_apellido[0].upper()
    primera_vocal = re.search(r'[AEIOU]', primer_apellido[1:], re.I)
    curp += primera_vocal.group(0).upper() if primera_vocal else "X"
    curp += segundo_apellido[0].upper() if segundo_apellido else "X"
    curp += nombre[0].upper()
    
    curp += año[-2:]
    curp += f"{int(mes):02d}"
    curp += f"{int(dia):02d}"
    
    curp += sexo.upper()[0]
    estados = {
        "AGUASCALIENTES": "AS", "BAJA CALIFORNIA": "BC", "BAJA CALIFORNIA SUR": "BS",
        "CAMPECHE": "CC", "CHIAPAS": "CS", "CHIHUAHUA": "CH", "COAHUILA": "CL",
        "COLIMA": "CM", "DISTRITO FEDERAL": "DF", "DURANGO": "DG", "GUANAJUATO": "GT",
        "GUERRERO": "GR", "HIDALGO": "HG", "JALISCO": "JC", "MEXICO": "MC",
        "MICHOACAN": "MN", "MORELOS": "MS", "NAYARIT": "NT", "NUEVO LEON": "NL",
        "OAXACA": "OC", "PUEBLA": "PL", "QUERETARO": "QT", "QUINTANA ROO": "QR",
        "SAN LUIS POTOSI": "SP", "SINALOA": "SL", "SONORA": "SR", "TABASCO": "TC",
        "TAMAULIPAS": "TS", "TLAXCALA": "TL", "VERACRUZ": "VZ", "YUCATAN": "YN",
        "ZACATECAS": "ZS"
    }
    curp += estados.get(estado.upper(), "NE")
    
    consonantes_extra = [
        re.search(r'[^AEIOU]', primer_apellido[1:], re.I),
        re.search(r'[^AEIOU]', segundo_apellido[1:], re.I) if segundo_apellido else None,
        re.search(r'[^AEIOU]', nombre[1:], re.I)
    ]
    curp += ''.join([c.group(0).upper() if c else "X" for c in consonantes_extra])
    
    # Generar homoclave aleatoria: dos caracteres (números o letras)
    homoclave = ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))
    curp += homoclave
    return curp
