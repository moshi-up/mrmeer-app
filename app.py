from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para la página de productos (Aquí es donde mandas al usuario)
@app.route('/productos')
def pagina_productos():
    return render_template('productos.html') # Necesitas crear este archivo html

# Ruta para contacto
@app.route('/contacto')
def contacto():
    return render_template('contacto.html') # Necesitas crear este archivo html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)