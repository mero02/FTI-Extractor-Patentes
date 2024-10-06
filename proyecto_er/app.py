from flask import Flask, render_template, request
import re

app = Flask(__name__)

def extraer_patentes(texto):
    # Definición de los dos formatos de patentes en Argentina:
    formato_patente = r'\b[A-Z]{3} \d{3}\b|\b[A-Z]{3}-\d{4}\b'

    # Buscar coincidencias en el texto
    patentes = re.findall(formato_patente, texto)
    
    # Unir los resultados
    return patentes 

@app.route('/', methods=['GET', 'POST'])
def home():
    patentes = []
    form_submitted = False 
    if request.method == 'POST':
        texto = request.form.get('texto')
        patentes = extraer_patentes(texto)
        form_submitted = True

    return render_template('home.html', patentes=patentes, form_submitted=form_submitted)

if __name__ == '__main__':
    app.run(debug=True)
