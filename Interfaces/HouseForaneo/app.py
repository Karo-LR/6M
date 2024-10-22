from flask import Flask, render_template, request, redirect, url_for
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Lista de propiedades (ejemplo básico)
properties = [
    {"name": "Departamento en el centro", "address": "Calle 123, Ciudad", "lat": 19.432608, "lon": -99.133209},
    {"name": "Casa cerca de la universidad", "address": "Av. Universidad 456, Ciudad", "lat": 19.332608, "lon": -99.203209},
    {"name": "Cuarto económico", "address": "Colonia XYZ, Ciudad", "lat": 19.442608, "lon": -99.153209}
]

# Página principal donde se muestran las propiedades
@app.route('/')
def home():
    return render_template('index.html', properties=properties)

# Detalle de una propiedad
@app.route('/property/<int:property_id>')
def property_detail(property_id):
    selected_property = properties[property_id]
    return render_template('property_detail.html', property=selected_property)

# Simulación de renta de una propiedad
@app.route('/rent/<int:property_id>', methods=['POST'])
def rent_property(property_id):
    # Aquí se podría procesar el registro y renta
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
