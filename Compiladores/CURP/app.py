from flask import Flask, render_template, request, redirect, url_for
from curp_generador import generar_curp

app = Flask(__name__)
curps_generadas = []  # Lista para almacenar las CURPs generadas

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nombre = request.form["nombre"]
        primer_apellido = request.form["primer_apellido"]
        segundo_apellido = request.form["segundo_apellido"]
        año = request.form["año"]
        mes = request.form["mes"]
        dia = request.form["dia"]
        sexo = request.form["sexo"]
        estado = request.form["estado"]
        
        curp = generar_curp(nombre, primer_apellido, segundo_apellido, año, mes, dia, sexo, estado)
        
        # Guardar la CURP generada en la lista
        curps_generadas.append(curp)
        
        return redirect(url_for("index"))
    
    return render_template("index.html", curps=curps_generadas)

if __name__ == "__main__":
    app.run(debug=True)
