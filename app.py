from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')


def home():
    image_url = url_for('static', filename='img/slide-2.jpg')
    return render_template('index.html', image_url=image_url)

@app.route('/buscar_propiedad', methods=['POST'])
def buscar_propiedad():
    # Aquí puedes obtener los datos del formulario
    keyword = request.form.get('keyword')
    print(keyword)

    # Lógica para buscar el departamento
    departamento = buscar_departamento(keyword)

    # Puedes redirigir a una página de resultados o renderizar una plantilla con los resultados
    return render_template('resultados.html', departamento=departamento)

def buscar_departamento(keyword):
    # Ejemplo de datos de departamento
    departamento = {
        'nombre': 'Departamento de Lujo',
        'ubicacion': 'Santiago',
        'precio': '200.000.000 CLP',
        'descripcion': 'Un hermoso departamento en el centro de Santiago.'
    }
    return departamento

if __name__ == '__main__':
    app.run(debug=True)
