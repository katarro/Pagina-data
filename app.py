from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# Simulación de tu algoritmo de inteligencia artificial
def get_best_property(criteria):
    # Aquí iría la lógica de tu algoritmo de inteligencia artificial
    # Por ahora, solo retornaremos un ejemplo de propiedad
    return {
        "address": "Calle Falsa 123, Santiago Centro",
        "price": "100,000,000 CLP",
        "description": "Un hermoso apartamento en el corazón de Santiago Centro.",
        # "image_url": "https://via.placeholder.com/150"
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    criteria = request.form['criteria']
    best_property = get_best_property(criteria)
    return render_template('index.html', property=best_property)

if __name__ == '__main__':
    app.run(debug=True)
