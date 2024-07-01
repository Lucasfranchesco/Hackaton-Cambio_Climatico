# Importar
from flask import Flask, render_template


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Variables que permiten calcular el consumo energético de los aparatos
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

# La primera página
@app.route('/')
def index():
    return render_template('medio_transporte.html')

# La segunda página
@app.route('/<size>')
def lights(size):
    return render_template(
                            'desechos.html', 
                            size=size
                           )

# La tercera página
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'dispositivos.html',
                            size = size, 
                            lights = lights                           
                           )

# La cuarta página
@app.route('/<size>/<lights>/<agua>')
def agua(size, lights, agua):
    return render_template(
                            'consumo_agua.html',
                            size = size, 
                            lights = lights,
                            agua = agua                           
                           )
# La quinta página
@app.route('/<size>/<lights>/<agua>/<uso_transporte>')
def uso_transporte(size, lights, agua, uso_transporte):
    return render_template(
                            'Uso_auto.html',
                            size = size, 
                            lights = lights,
                            agua = agua,
                            uso_transporte = uso_transporte                           
                           )

# La sexta página
@app.route('/<size>/<lights>/<agua>/<uso_transporte>/<tala>')
def tala_arboles(size, lights, agua, uso_transporte, tala):
    return render_template(
                            'deforestacion.html',
                            size = size, 
                            lights = lights,
                            agua = agua,
                            uso_transporte = uso_transporte,
                            tala = tala                           
                           )

# La séptima página
@app.route('/<size>/<lights>/<agua>/<uso_transporte>/<tala>/<reciclaje>')
def recicla_plastico(size, lights, agua, uso_transporte, tala, reciclaje):
    return render_template(
                            'reciclaje.html',
                            size = size, 
                            lights = lights,
                            agua = agua,
                            uso_transporte = uso_transporte,
                            tala = tala,
                            reciclaje = reciclaje                           
                           )

# La octava página
@app.route('/<size>/<lights>/<agua>/<uso_transporte>/<tala>/<reciclaje>/<aire>')
def aire_acondicionado(size, lights, agua, uso_transporte, tala, reciclaje, aire):
    return render_template(
                            'aire_acondicionado.html',
                            size = size, 
                            lights = lights,
                            agua = agua,
                            uso_transporte = uso_transporte,
                            tala = tala,
                            reciclaje = reciclaje,
                            aire = aire                           
                           )

 # La novena página
@app.route('/<size>/<lights>/<agua>/<uso_transporte>/<tala>/<reciclaje>/<aire>/<carne>')
def consumo_de_carne(size, lights, agua, uso_transporte, tala, reciclaje, aire, carne):
    return render_template(
                            'consumo_carne.html',
                            size = size, 
                            lights = lights,
                            agua = agua,
                            uso_transporte = uso_transporte,
                            tala = tala,
                            reciclaje = reciclaje,
                            aire = aire,
                            carne = carne                           
                           )

#la décima pagina
@app.route('/<size>/<lights>/<agua>/<uso_transporte>/<tala>/<reciclaje>/<aire>/<carne>/<vuelo>')
def vuelos(size, lights, agua, uso_transporte, tala, reciclaje, aire, carne, vuelo):
    return render_template(
                            'vuelos.html',
                            size = size, 
                            lights = lights,
                            agua = agua,
                            uso_transporte = uso_transporte,
                            tala = tala,
                            reciclaje = reciclaje,
                            aire = aire,
                            carne = carne,
                            vuelo = vuelo                           
                           )

#la onceava página y última
@app.route('/<size>/<lights>/<agua>/<uso_transporte>/<tala>/<reciclaje>/<aire>/<carne>/<vuelo>/<final>')
def cierre(size, lights, agua, uso_transporte, tala, reciclaje, aire, carne, vuelo, final):
    return render_template(
                            'página_final.html',
                            size = size, 
                            lights = lights,
                            agua = agua,
                            uso_transporte = uso_transporte,
                            tala = tala,
                            reciclaje = reciclaje,
                            aire = aire,
                            carne = carne,
                            vuelo = vuelo,
                            final = final                           
                           )
                                                                                      
app.run(debug=True)
