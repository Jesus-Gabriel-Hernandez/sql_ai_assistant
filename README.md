[ENGLISH] — AI ASSISTANT FOR SQL
This AI‑powered SQLite IDE lets you practice SQL while learning interactively. You can ask the Ollama model how SQLite works, generate ERD diagrams, run SQL queries, or retrieve data using natural language without knowing SQL at all. I built this project because I enjoy working with databases, and it allowed me to review concepts like NLP and the integration of LLMs into real applications.

[!NOTE]
The assistant works fully offline thanks to Ollama + Llama 3.1, running locally on your machine.

[!TIP]
You can freely mix SQL and natural language — the system automatically detects what you want.

[!IMPORTANT]
You must have Ollama running in the background for AI features to work.

[!WARNING]
If you see “database is locked”, close any external SQLite viewer (DB Browser, VSCode SQLite extension, etc.) and try again.

[!CAUTION]
Avoid deleting the temporary database file while the app is running.

📋 Pre‑requirements
Python 3.10 or higher

Ollama installed

Llama 3.1 model downloaded

Graphviz installed (for ERD generation)

All dependencies from requirements.txt

⚙️ Installation
1. Install Ollama
Download from:
https://ollama.com/download

2. Pull the Llama 3.1 model
Run this in any terminal (CMD, PowerShell, Bash, etc.):

bash
ollama pull llama3.1
3. Verify the model
bash
ollama run llama3.1
If it responds, everything is ready.

4. Clone the project
bash
git clone <your-repo>
cd <your-repo>
5. Create a virtual environment
bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
6. Install dependencies
bash
pip install -r requirements.txt
7. Run the project
bash
streamlit run final_project.py
🛠️ Project Resources
Streamlit — UI and interactive components

SQLite — Local database engine

Ollama — Local LLM runtime

Llama 3.1 — Natural language → SQL + explanations

Graphviz — ERD generation

Pandas — Data handling

Python — Core logic

📦 What the Project Covers & Why It’s Helpful
Learn SQL by doing, not just reading

Understand queries with AI‑generated explanations

Generate SQL from natural language

Visualize database structure with ERDs

Practice DDL, DML, and SELECT queries

Explore any SQLite database you upload

Use it as a teaching tool or personal learning environment

🎯 Project Goals, Methodology & Results
Goals
Build an interactive SQL learning assistant

Integrate AI to explain and generate SQL

Provide visual tools (ERD, summaries)

Support real SQLite databases

Methodology
Streamlit for UI

SQLite for real execution

Llama 3.1 for reasoning and SQL generation

Modular architecture (utils/ folder)

Iterative testing with DDL/DML/SELECT

Results
Fully functional AI‑powered SQL IDE

Natural language interface for databases

Automatic schema understanding

Real‑time ERD generation

Clear explanations for any SQL query

🗂️ requirements.txt
The project includes a curated set of dependencies for:

Streamlit

Pandas

Ollama client

Graphviz

OpenAI/Ollama integration

Utility libraries

(Already included in the repository.)

📅 Project Planning
GitHub repository with frequent commits

Modular development (UI, DB utils, NLP utils, ERD utils)

Iterative debugging and testing

Clear separation of concerns

[ESPAÑOL] — ASISTENTE DE SQL POTENCIADO POR IA
Este IDE de SQLite potenciado por IA te permite practicar SQL mientras aprendes de forma interactiva. Puedes preguntarle al modelo de Ollama cómo funciona SQLite, generar diagramas ERD, ejecutar consultas SQL o recuperar datos usando lenguaje natural sin saber SQL. Creé este proyecto porque me gusta el mundo de las bases de datos y quería repasar conceptos como NLP y el uso de LLMs en aplicaciones reales.

[!NOTE]
El asistente funciona completamente offline gracias a Ollama + Llama 3.1, ejecutándose localmente.

[!TIP]
Puedes mezclar SQL y lenguaje natural libremente — el sistema detecta automáticamente tu intención.

[!IMPORTANT]
Ollama debe estar ejecutándose en segundo plano para que las funciones de IA funcionen.

[!WARNING]
Si aparece “database is locked”, cierra cualquier visor externo de SQLite y vuelve a intentarlo.

[!CAUTION]
No elimines el archivo temporal de la base de datos mientras la app está en ejecución.

📋 Pre‑requisitos
Python 3.10 o superior

Ollama instalado

Modelo Llama 3.1 descargado

Graphviz instalado

Dependencias de requirements.txt

⚙️ Instalación
1. Instalar Ollama
Descargar desde:
https://ollama.com/download

2. Descargar el modelo Llama 3.1
Ejecutar en cualquier terminal (CMD, PowerShell, Bash, etc.):

bash
ollama pull llama3.1
3. Verificar el modelo
bash
ollama run llama3.1
4. Clonar el proyecto
bash
git clone <tu-repo>
cd <tu-repo>
5. Crear entorno virtual
bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
6. Instalar dependencias
bash
pip install -r requirements.txt
7. Ejecutar el proyecto
bash
streamlit run final_project.py
🛠️ Recursos del Proyecto
Streamlit — Interfaz interactiva

SQLite — Motor de base de datos

Ollama — Ejecución local de LLMs

Llama 3.1 — Generación y explicación de SQL

Graphviz — Diagramas ERD

Pandas — Manejo de datos

Python — Lógica principal

📦 Qué Cubre el Proyecto y Por Qué Es Útil
Aprender SQL practicando

Entender consultas con explicaciones generadas por IA

Generar SQL desde lenguaje natural

Visualizar la estructura de la base de datos

Practicar DDL, DML y SELECT

Explorar cualquier base de datos SQLite

Útil como herramienta educativa o de autoaprendizaje

🎯 Objetivos, Metodología y Resultados
Objetivos
Crear un asistente interactivo para aprender SQL

Integrar IA para explicar y generar SQL

Proveer herramientas visuales (ERD, resúmenes)

Soportar bases de datos SQLite reales

Metodología
Streamlit para la interfaz

SQLite para ejecución real

Llama 3.1 para razonamiento y generación

Arquitectura modular

Pruebas iterativas con DDL/DML/SELECT

Resultados
IDE de SQL potenciado por IA completamente funcional

Interfaz de lenguaje natural para bases de datos

Comprensión automática del esquema

ERDs en tiempo real

Explicaciones claras para cualquier consulta

📅 Planificación del Proyecto
Repositorio GitHub con commits frecuentes

Desarrollo modular

Depuración iterativa

Separación clara de responsabilidades