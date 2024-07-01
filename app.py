from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    image_url = url_for('static', filename='img/slide-2.jpg')
    return render_template('index.html', image_url=image_url)

@app.route('/buscar_propiedad', methods=['POST'])
def buscar_propiedad():
    # Obtener los datos del formulario
    palabra_clave = request.form.get('palabra_clave')
    dormitorios = request.form.get('dormitorios')
    banos = request.form.get('banos')
    metros_cuadrados = request.form.get('metros_cuadrados')
    centros_comerciales_dist = request.form.get('centros_comerciales_dist_metros_avg')
    clinicas_dist = request.form.get('clinicas_dist_metros_avg')
    colegios_dist = request.form.get('colegios_dist_metros_avg')
    estaciones_de_metro_dist = request.form.get('estaciones_de_metro_dist_metros_avg')
    farmacias_dist = request.form.get('farmacias_dist_metros_avg')
    jardines_infantiles_dist = request.form.get('jardines_infantiles_dist_metros_avg')
    paraderos_dist = request.form.get('paraderos_dist_metros_avg')
    plazas_dist = request.form.get('plazas_dist_metros_avg')
    supermercados_dist = request.form.get('supermercados_dist_metros_avg')
    universidades_dist = request.form.get('universidades_dist_metros_avg')

    # Imprimir los valores obtenidos
    print(f"Palabra clave: {palabra_clave}")
    print(f"Dormitorios: {dormitorios}")
    print(f"Baños: {banos}")
    print(f"Metros cuadrados: {metros_cuadrados}")
    print(f"Distancia a Centros Comerciales: {centros_comerciales_dist}")
    print(f"Distancia a Clínicas: {clinicas_dist}")
    print(f"Distancia a Colegios: {colegios_dist}")
    print(f"Distancia a Estaciones de Metro: {estaciones_de_metro_dist}")
    print(f"Distancia a Farmacias: {farmacias_dist}")
    print(f"Distancia a Jardines Infantiles: {jardines_infantiles_dist}")
    print(f"Distancia a Paraderos: {paraderos_dist}")
    print(f"Distancia a Plazas: {plazas_dist}")
    print(f"Distancia a Supermercados: {supermercados_dist}")
    print(f"Distancia a Universidades: {universidades_dist}")

    # Lógica para buscar el departamento
    departamento = buscar_departamento(palabra_clave, dormitorios, banos, metros_cuadrados,
                                        centros_comerciales_dist, clinicas_dist, colegios_dist, estaciones_de_metro_dist, 
                                        farmacias_dist, jardines_infantiles_dist, paraderos_dist, plazas_dist, 
                                        supermercados_dist, universidades_dist)

    # Puedes redirigir a una página de resultados o renderizar una plantilla con los resultados
    return render_template('resultados.html', departamento=departamento)

def buscar_departamento(palabra_clave, dormitorios, banos, metros_cuadrados, 
                        centros_comerciales_dist, clinicas_dist, colegios_dist, estaciones_de_metro_dist, 
                        farmacias_dist, jardines_infantiles_dist, paraderos_dist, plazas_dist, 
                        supermercados_dist, universidades_dist):
    # Ejemplo de datos de departamento
    departamento = {
        'nombre': 'Departamento de Lujo',
        'ubicacion': 'Santiago',
        'precio': '200.000.000 CLP',
        'descripcion': 'Un hermoso departamento en el centro de Santiago.'
    }
    return departamento

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
