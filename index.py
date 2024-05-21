from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contacto')
def contacto():
    nombres = ["Cuesta", "Carnalito", "Pajan"]
    return render_template("contacto.html", nombres=nombres)

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # Aquí procesas los datos del formulario
    nombre = request.form['nombre']
    return f'Formulario enviado por {nombre}'

if __name__ == '__main__':
    app.run(debug=True)
