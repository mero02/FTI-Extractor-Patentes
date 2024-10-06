# Proyecto Extractor de Patentes

### Integrantes del Grupo 2:
- **Gonzalo Bustamante**
- **San Pedro Mauro**

---

## Explicación del Programa

El proyecto desarrollado es una **aplicación web** que permite **extraer y validar patentes de vehículos** a partir de un texto de entrada, según los **formatos oficiales de Argentina**. Los formatos de patente válidos en Argentina son:

- **ABC-1234** (con guión y cuatro dígitos).
- **XYZ 567** (sin guión y con tres dígitos).

La aplicación toma el texto ingresado por el usuario, busca las patentes que coincidan con estos formatos y devuelve las patentes encontradas en un mensaje de salida.

---

## Pasos para Hacer Funcionar el Programa

1. **Clonar el proyecto.**
2. **Crear un entorno virtual** dentro de la carpeta del proyecto (`/Grupo_2/`):

    ```bash
    python -m venv env
    ```

3. **Activar el entorno:**
    - En **Windows**:

      ```bash
      .\env\Scripts\activate
      ```
    - En **Linux/Mac**:

      ```bash
      source env/bin/activate
      ```

4. **Instalar las dependencias** desde `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

5. **Posicionarse en la carpeta `proyecto_er`:**

    ```bash
    cd proyecto_er
    ```

6. **Ejecutar la aplicación:**

    ```bash
    python app.py
    ```

---

## Tecnologías Utilizadas

- **Flask**: Utilizamos Flask como framework para desarrollar la aplicación web, ya que es ligero, flexible y permite trabajar con Python, nuestro lenguaje de elección.
- **HTML y CSS**: Implementamos una interfaz sencilla utilizando HTML y CSS para personalizar la apariencia de la página.
- **Bootstrap**: Agregamos Bootstrap para darle un mejor estilo a la aplicación y facilitar el diseño responsivo.

---

## ¿Por Qué Elegimos Flask?

Elegimos Flask porque:

- Es un framework **minimalista** que permite un control detallado sobre el desarrollo de la aplicación.
- Facilita la **integración con otros módulos de Python**, como el uso de expresiones regulares para el procesamiento de texto.
- Permite la rápida creación de prototipos y la integración de una **interfaz sencilla** con HTML y CSS.
