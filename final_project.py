# =========================================
# AI Powered SQL Assistant — Final Project - Jesús G. Hernández Matamoros
# =========================================

import pandas as pd
import streamlit as st
import time

# =========================================
# Custom Modules
# =========================================

from utils.db_utils import (
    connect_sqlite_db,
    list_tables,
    validate_sql,
    execute_query,
    get_columns,
    summarize_database
)

from utils.llama_utils import use_llama, modes
from utils.generate_images_utils import generate_image
from utils.erd_utils import generate_erd, erd_to_image

from utils.nlp_utils import (
    get_schema_for_llm,
    nlp_to_sql,
    explain_sql,
    validate_generated_sql,
    fix_generated_sql
)

# =========================================
# Global CSS — Modern UI
# =========================================

st.markdown("""
<style>

    /* Background */
    .main {
        background-color: #f7f7f9;
    }

    /* Titles */
    h1, h2, h3 {
        font-family: 'Segoe UI', sans-serif;
        font-weight: 600;
    }

    /* Buttons */
    .stButton>button {
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 15px;
        background-color: #0e403e;
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #357ABD;
    }

    /* Text area */
    .stTextArea textarea {
        border-radius: 8px;
        font-size: 14px;
        padding: 10px;
    }

    /* Dataframe */
    .stDataFrame {
        border-radius: 8px;
        overflow: hidden;
    }

</style>
""", unsafe_allow_html=True)

# =========================================
# Header
# =========================================

st.markdown("""
    <h1 style='text-align:center; margin-bottom:0;'>AI Powered SQL Assistant</h1>
    <p style='text-align:center; color:gray; margin-top:0;'>
        Explore databases and learn SQL interactively
    </p>
""", unsafe_allow_html=True)

st.markdown("<hr style='margin:20px 0;'>", unsafe_allow_html=True)

# =========================================
# Ensure editor exists
# =========================================

if "sql_editor" not in st.session_state:
    st.session_state.sql_editor = ""

# =========================================
# Load Database
# =========================================

uploaded_file = st.file_uploader("📁 Upload a .db file (optional)", type="db")

def load_database(uploaded_file=None, default_file="northwind.db"):

    if "conn" not in st.session_state:
        st.session_state.conn = connect_sqlite_db(default_file)

    if uploaded_file:

        try:
            st.session_state.conn.close()
        except:
            pass

        # Reset state
        for key in ["schema_cache", "real_schema", "last_sql", "last_result", "last_columns"]:
            if key in st.session_state:
                del st.session_state[key]

        # Save new DB
        temp_path = "temp_db.db"
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.session_state.conn = connect_sqlite_db(temp_path)

        # Update tables instantly (NO rerun)
        st.session_state["tables"] = list_tables(st.session_state.conn)

        # Update schema instantly
        st.session_state["real_schema"] = get_schema_for_llm(st.session_state.conn)

        st.success("Database loaded successfully.")

    return st.session_state.conn

data_base = load_database(uploaded_file)

# Ensure tables exist
if "tables" not in st.session_state:
    st.session_state["tables"] = list_tables(data_base)

# =========================================
# Show Tables
# =========================================

st.markdown("### 📚 Available Tables")

tables = st.session_state["tables"]

if isinstance(tables, list):
    st.write(", ".join(tables))
else:
    st.error(tables)

st.markdown("<hr style='margin:20px 0;'>", unsafe_allow_html=True)

# =========================================
# SQL Editor
# =========================================

st.markdown("### 📝 SQL Editor")

st.text_area(
    "SQL Editor",
    key="sql_editor",
    height=220,
    placeholder="Write your SQL query or natural language request...",
    label_visibility="visible"
)

user_input = st.session_state.sql_editor.strip()

# =========================================
# Toolbar (NO container → evita reruns)
# =========================================

col1, col2, col3, col4, col5 = st.columns([1.2, 1.2, 1.2, 1.2, 1.2])
btn_execute = col1.button("▶ Execute")
btn_explain = col2.button("💬 Explain")
btn_generate_sql = col3.button("✨ Generate SQL")
btn_erd = col4.button("📊 ERD")
btn_summary = col5.button("📘 Summary")

st.markdown("<hr style='margin:20px 0;'>", unsafe_allow_html=True)

# =========================================
# Helper: Detect SQL vs NLP
# =========================================

def is_sql_query(text: str) -> bool:
    sql_keywords = [
        "select", "insert", "update", "delete",
        "create", "alter", "drop", "with", "pragma"
    ]
    text = text.strip().lower()
    return any(text.startswith(keyword) for keyword in sql_keywords)

# =========================================
# 1. Execute SQL
# =========================================

if btn_execute:

    st.markdown("### 📄 Query Results")

    if user_input == "":
        st.warning("Please enter a SQL query or a natural language request.")
    else:

        if is_sql_query(user_input):
            sql = user_input
        else:
            real_schema = st.session_state.get("real_schema", get_schema_for_llm(data_base))
            sql = nlp_to_sql(user_input, real_schema)

        st.subheader("SQL code")
        st.code(sql, language="sql")

        try:
            cursor = data_base.cursor()
            cursor.execute(sql)
            data_base.commit()

            # Save the last query
            st.session_state["last_sql"] = sql

            # Get results if possible
            if cursor.description:
                rows = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
            else:
                rows = None
                columns = None

            st.session_state["last_result"] = rows
            st.session_state["last_columns"] = columns

            # Update tables and schema
            st.session_state["tables"] = list_tables(data_base)
            st.session_state["real_schema"] = get_schema_for_llm(data_base)

            if rows:
                df = pd.DataFrame(rows, columns=columns)
                st.dataframe(df, width="stretch", hide_index=True)
            else:
                st.info("Query executed successfully (no results).")

        except Exception as error:
            st.error(f"SQL Error: {error}")

# DEBUG 
st.write("DEBUG user_input:", repr(user_input))
st.write("DEBUG tables:", st.session_state.get("tables"))
st.write("DEBUG last_sql:", st.session_state.get("last_sql"))

# =========================================
# 2. Explain SQL
# =========================================

if btn_explain:

    st.markdown("### 💬 Explanation")

    sql = st.session_state.get("last_sql")
    rows = st.session_state.get("last_result")
    columns = st.session_state.get("last_columns")

    if not sql:
        editor_text = st.session_state.sql_editor.strip()
        if not editor_text:
            st.warning("Execute a SQL query first or write one in the editor.")
            st.stop()

        real_schema = st.session_state.get("real_schema", get_schema_for_llm(data_base))
        sql = editor_text if is_sql_query(editor_text) else nlp_to_sql(editor_text, real_schema)
        st.session_state["last_sql"] = sql
        rows = None
        columns = None

    real_schema = st.session_state.get("real_schema", get_schema_for_llm(data_base))

    explanation = explain_sql(sql, columns, rows, real_schema)
    st.subheader("Explanation based on real data")
    st.markdown(explanation)

    llm_explanation = use_llama(sql, role_system=modes["explain"])
    st.subheader("LLM Explanation (teacher mode)")
    st.info(llm_explanation)

    visual_prompt = f"""
A simple whiteboard-style diagram that visually explains the following SQL query:

{sql}
"""

    img_path = generate_image(visual_prompt)

    if isinstance(img_path, str):
        st.image(img_path, caption="Generated Diagram")

# =========================================
# 3. Generate SQL from Natural Language
# =========================================

if btn_generate_sql and user_input.strip():

    st.markdown("### ✨ Generated SQL")

    real_schema = st.session_state.get("real_schema", get_schema_for_llm(data_base))

    sql_generated = nlp_to_sql(user_input, real_schema)

    st.code(sql_generated)

    valid, error = validate_generated_sql(sql_generated, data_base)

    if valid:
        st.success("The generated SQL is valid ✔")
    else:
        st.warning(f"Generated SQL contains errors:\n{error}")

        sql_fixed = fix_generated_sql(sql_generated, error, real_schema)

        st.subheader("Fixed SQL")
        st.code(sql_fixed)

        valid2, error2 = validate_generated_sql(sql_fixed, data_base)

        if valid2:
            st.success("The fixed SQL is valid ✔")
        else:
            st.error(f"The fixed SQL still contains errors:\n{error2}")

# =========================================
# 4. Generate ERD
# =========================================

if btn_erd:

    st.markdown("### 📊 Entity Relationship Diagram")

    try:
        erd_code = generate_erd(data_base)
        erd_to_image(erd_code)
    except Exception as e:
        st.error(f"Error generating ERD: {e}")

# =========================================
# 5. Database Summary
# =========================================

if btn_summary:

    st.markdown("### 📘 Database Summary")

    summary = summarize_database(data_base)

    st.text_area("Complete Database Summary:", summary, height=400)

    prompt = f"""
You are a database analyst (SQLite expert).
Database:
{summary}
"""

    llm_summary = use_llama(prompt, role_system=modes["explain"])
    st.subheader("LLM Summary")
    st.info(llm_summary)

# =========================================
# Footer
# =========================================

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Open source project</p>", unsafe_allow_html=True)
