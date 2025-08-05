<h1 align="center">📊 Backend - Dashboard de Análisis Financiero</h1>

<p align="center">
  Aplicación Backend modular desarrollada con <b>Flask</b> y estructurada con <b>FlaskKit</b>, diseñada para alimentar un dashboard de análisis financiero.
</p>

<hr/>

<h2>🚀 Características principales</h2>

<ul>
  <li>🔁 Estructura modular limpia usando <code>FlaskKit</code>.</li>
  <li>🧩 Módulos independientes con sus propias rutas (<code>routers.py</code>) y lógica de base de datos (<code>db.py</code>).</li>
  <li>⚙️ Configuración centralizada en <code>config/settings.py</code>.</li>
  <li>🔐 Uso de variables de entorno con <code>.env</code>.</li>
  <li>🔌 Adaptadores externos separados en <code>conexiones/adaptadores.py</code>.</li>
</ul>

<hr/>

<h2>📁 Estructura del proyecto</h2>

<pre>
├── run.py                  # Archivo principal para iniciar la app
├── .env                   # Variables de entorno
├── config/
│   └── settings.py        # Configuración global
│
├── conexiones/
│   └── adaptadores.py     # Conectores externos o adaptadores
│
├── apps/                  # Módulos independientes como Blueprints
│   ├── __init__.py
│   ├── modulo1/
│   │   ├── routers.py     # Rutas del módulo
│   │   └── db.py          # Lógica de base de datos
│   ├── modulo2/
│   │   ├── routers.py
│   │   └── db.py
│   └── ...
</pre>

<hr/>

<h2>🧪 Cómo ejecutar el proyecto</h2>

<h3>1. Clonar el repositorio</h3>


git clone https://github.com/tuusuario/tu-repositorio.git
cd tu-repositorio

<h3>2. Crear entorno virtual</h3>
python -m venv venv
source venv/bin/activate

<h3>3. Instalar dependencias</h3>
pip install -r requirements.txt

<h3>4. Configurar variables de entorno</h3>
Editar el archivo <code>.env</code>:

FLASK_ENV=development
SECRET_KEY=tu_clave_secreta
DATABASE_URL=sqlite:///data.db


<h3>5. Ejecutar la aplicación</h3>

<hr/> <h2>🧱 Estructura típica de un módulo</h2>
Cada módulo dentro de <code>apps/</code> contiene:

<ul> <li><b>routers.py</b>: define los endpoints del módulo.</li> <li><b>db.py</b>: contiene funciones para manejar la base de datos.</li> </ul>
Esto permite una organización clara y escalabilidad sencilla.

<hr/> <h2>📂 Ejemplo de endpoint</h2>

<hr/> <h2>🛠️ Tecnologías utilizadas</h2> <ul> <li>🐍 Python 3.10+</li> <li>🔥 Flask</li> <li>🧰 FlaskKit</li> <li>🔐 python-dotenv</li> <li>🛢️ SQLAlchemy u otro ORM (dependiendo del módulo)</li> </ul> <hr/> <h2>🤝 Contribuciones</h2> <p>Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, puedes:</p> <ul> <li>📥 Crear un <code>Pull Request</code></li> <li>🐞 Reportar un <code>Issue</code></li> </ul> <hr/> <h2>📄 Licencia</h2> <p>Este proyecto está licenciado bajo la <b>MIT License</b>.</p> <hr/> <h2>✉️  ```


