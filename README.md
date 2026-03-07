# AI ASSISTANT FOR SQL  
### *AI‑Powered SQLite IDE with Natural Language Support*

This AI‑powered SQLite IDE lets you practice SQL while learning interactively. You can ask the Ollama model how SQLite works, generate ERD diagrams, run SQL queries, or retrieve data using natural language without knowing SQL at all. I built this project because I enjoy working with databases, and it allowed me to review concepts like NLP and the integration of LLMs into real applications.

> [!NOTE]  
> The assistant works fully offline thanks to **Ollama + Llama 3.1**, running locally on your machine.

> [!TIP]  
> You can freely mix SQL and natural language — the system automatically detects your intent.

> [!IMPORTANT]  
> You must have **Ollama running** in the background for AI features to work.

> [!WARNING]  
> If you see “database is locked”, close any external SQLite viewer (DB Browser, VSCode SQLite extension, etc.) and try again.

> [!CAUTION]  
> Avoid deleting the temporary database file while the app is running.

> [!WARNING]  
> If you want to use your own database, the extension is .db .
---

## 📋 Pre‑requirements

- Python 3.10 or higher  
- Ollama installed  
- Llama 3.1 model downloaded  
- Mermaid.js installed (for ERD generation)  
- All dependencies from `requirements.txt`

---

## ⚙️ Installation

### 1. Install Ollama  
Download from:  
https://ollama.com/download

### 2. Pull the Llama 3.1 model  
Run this in any terminal (CMD, PowerShell, Bash, etc.):

```bash
ollama pull llama3.1
```
3. Verify the model

```bash
ollama run llama3.1
```
4. Clone the project

```bash
git clone <your-repo>
cd <your-repo>
```
5. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```
6. Install dependencies
```
bash
pip install -r requirements.txt
```
7. Run the project
```
bash
streamlit run final_project.py
```

## 🛠️ Project Resources
- Streamlit for the UI and interactive components
- SQLite for the Local database engine
- Ollama for the Local LLM runtime
- Llama 3.1 for the Natural language, SQL and explanations
- Mermaid.js for the ERD generation
- Pandas for the Data handling
- Python 

## 📦 What the Project Covers & Why It’s Helpful

- Learn SQL by doing, not just reading
- Understand queries with AI‑generated explanations
- Generate SQL from natural language
- Visualize database structure with ERDs
- Practice SQL queries
- Explore any SQLite database you upload
- Use it as a teaching tool or personal learning environment

## 🎯 Project Goals, Methodology & Results
Goals
- Build an interactive SQL learning assistant
- Integrate AI to explain and generate SQL
- Provide visual tools (ERD, summaries)
- Support real SQLite databases

Methodology
1. Streamlit for UI
2. SQLite for real execution
3. Llama 3.1 for reasoning and SQL generation
4. Modular architecture (utils/ folder)
5. Iterative testing with SQL queries

Results
* Fully functional AI‑powered SQL IDE
* Natural language interface for databases
* Automatic schema understanding
* Real‑time ERD generation
* Clear explanations for any SQL query

🗂️ requirements.txt
The project includes a curated set of dependencies for:

- Streamlit
- Pandas
- Ollama client
- Mermaid.js
- Ollama integration
- Utility libraries
(Already included in the repository.)

📅 Project Planning

1. Modular development
2. Iterative debugging and testing
3. Clear separation of responsibilities

# [ESPAÑOL] — ASISTENTE DE SQL POTENCIADO POR IA  
### *IDE de SQLite con soporte de IA y lenguaje natural*

Este IDE de SQLite potenciado por IA te permite practicar SQL mientras aprendes de forma interactiva. Puedes preguntarle al modelo de Ollama cómo funciona SQLite, generar diagramas ERD, ejecutar consultas SQL o recuperar datos usando lenguaje natural sin saber SQL. Creé este proyecto porque me gusta el mundo de las bases de datos y quería repasar conceptos como NLP y el uso de LLMs en aplicaciones reales.

> [!NOTE]  
> El asistente funciona completamente offline gracias a **Ollama + Llama 3.1**, ejecutándose localmente.

> [!TIP]  
> Puedes mezclar SQL y lenguaje natural libremente — el sistema detecta automáticamente tu intención.

> [!IMPORTANT]  
> Ollama debe estar ejecutándose en segundo plano para que las funciones de IA funcionen.

> [!WARNING]  
> Si aparece “database is locked”, cierra cualquier visor externo de SQLite y vuelve a intentarlo.

> [!CAUTION]  
> No elimines el archivo temporal de la base de datos mientras la app está en ejecución.

> [!WARNING]  
> Si quieres usar tu propia base de datos, la extensión debe ser **.db**.

---

## 📋 Pre‑requisitos

- Python 3.10 o superior  
- Ollama instalado  
- Modelo Llama 3.1 descargado  
- Mermaid.js instalado (para generar ERDs)  
- Dependencias de `requirements.txt`  

---

## ⚙️ Instalación

### 1. Instalar Ollama  
Descargar desde:  
https://ollama.com/download

### 2. Descargar el modelo Llama 3.1  
Ejecutar en cualquier terminal (CMD, PowerShell, Bash, etc.):

```bash
ollama pull llama3.1
```
3. Verificar el modelo
```bash
ollama run llama3.1
```
4. Clonar el proyecto
```bash
git clone <tu-repo>
cd <tu-repo>
```
5. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```
6. Instalar dependencias
```bash
pip install -r requirements.txt
```
7. Ejecutar el proyecto
```bash
streamlit run final_project.py
```

🛠️ Recursos del Proyecto
- Streamlit para una Interfaz interactiva
- SQLite como motor de base de datos local
- Ollama para la Ejecución local de modelos LLM
- Llama 3.1 para Lenguaje natural, SQL y explicaciones
- Mermaid.js para la generación de diagramas ERD
- Pandas que Maneja los datos

📦 Qué Cubre el Proyecto y Por Qué Es Útil
- Aprender SQL practicando
- Entender consultas con explicaciones generadas por IA
- Generar SQL desde lenguaje natural
- Visualizar la estructura de la base de datos con ERDs
- Practicar consultas SQL
- Explorar cualquier base de datos SQLite que subas
- Usarlo como herramienta educativa o de autoaprendizaje

🎯 Objetivos, Metodología y Resultados
Objetivos
- Crear un asistente interactivo para aprender SQL
- Integrar IA para explicar y generar SQL
- Proveer herramientas visuales (ERD, resúmenes)
- Soportar bases de datos SQLite reales

Metodología
1. Streamlit para la interfaz
2. SQLite para ejecución real
3. Llama 3.1 para razonamiento y generación de SQL
4. Arquitectura modular (utils/ folder)
5. Pruebas iterativas con consultas SQL

Resultados
* IDE de SQL potenciado por IA completamente funcional
* Interfaz de lenguaje natural para bases de datos
* Comprensión automática del esquema
* ERDs en tiempo real
* Explicaciones claras para cualquier consulta

🗂️ requirements.txt
El proyecto incluye un conjunto de dependencias seleccionadas para:

- Streamlit
- Pandas
- Cliente de Ollama
- Mermaid.js
- Integración con Ollama
- Librerías utilitarias
(Ya incluidas en el repositorio.)

📅 Planificación del Proyecto
1. Desarrollo modular
2. Depuración y pruebas iterativas
3. Separación clara de responsabilidades
