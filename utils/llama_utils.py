# =========================================
# LLAMA_UTILS Module
# =========================================

import os
from datetime import datetime
from ollama import chat

from utils.db_utils import (
    list_tables,
    get_columns,
    get_foreign_keys
)


# Default model
model = "llama3.1"

# System-level modes for the LLM
modes = {
    "explain": "Act as a SQL instructor who explains queries and concepts clearly.",
    "generate_sql": """
        Act as an expert in SQL for SQLite.
        Convert the user's request into valid SQL.
        You may generate SELECT, INSERT, UPDATE, DELETE, 
        CREATE TABLE, ALTER TABLE, DROP TABLE, CREATE INDEX,
        and any other SQL statement supported by SQLite.
        Do not add explanations, return only SQL.
    """,
    
    "erd": "Automatic ERD generator. No explanations."
}


# ============================================================
# 1. Send prompt to LLaMA (Ollama)
# ============================================================

def use_llama(prompt: str, role_system: str = "") -> str:
    """
    Sends a prompt to the LLaMA model using Ollama and returns the response.
    Also logs the full prompt and the generated response.

    Args:
        prompt (str): Text sent to the model.
        role_system (str): System instructions guiding the LLM behavior.

    Returns:
        str: Model-generated response.

    Example:
        response = use_llama("Explain SELECT * FROM Customers;", role_system=modes["explain"])
        print(response)
    """

    response = chat(
        model=model,
        messages=[
            {"role": "system", "content": role_system},
            {"role": "user", "content": prompt}
        ]
    )

    content = response.message.content

    # Save log
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "Llama-Response.log")

    log_entry = f"""
==================================================
[{timestamp}]
MODEL: {model}
==================================================
PROMPT:
----------------------------------------
{prompt}
RESPONSE:
----------------------------------------
{content}
==================================================
"""
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)

    return content


# ============================================================
# 2. Structured database summary for the LLM
# ============================================================

def summary_for_llm(conn) -> str:
    """
    Generates a compact and structured summary of the database so the LLM
    can work without inventing table or column names.

    The summary includes:
    - Tables in double quotes
    - Columns with PK and FK annotations
    - Explicit N:1 relationships

    Args:
        conn (sqlite3.Connection): Active database connection.

    Returns:
        str: Structured summary ready for the LLM.

    Example:
        summary = summary_for_llm(conn)
        print(summary)

        Output:
        [TABLES]
        "Customers"("CustomerID" PK, "City", ...)
        ...

        [RELATIONSHIPS]
        "Orders"."CustomerID" → "Customers"."CustomerID" (N:1)
    """

    try:
        tables = list_tables(conn)
        if not isinstance(tables, list) or not tables:
            return "Could not read tables."

        lines = []
        relationships = []

        for table in tables:
            table_sql = f'"{table}"'
            columns = get_columns(conn, table)
            fks = get_foreign_keys(conn, table)

            if columns.empty:
                continue

            col_descriptions = []
            for _, col in columns.iterrows():
                name = col["name"]
                desc = f'"{name}"'

                if col["pk"]:
                    desc += " PK"

                fk_match = fks[fks["from"] == name] if not fks.empty else None
                if fk_match is not None and not fk_match.empty:
                    ref_table = fk_match.iloc[0]["table"]
                    ref_col = fk_match.iloc[0]["to"]
                    desc += f' FK→"{ref_table}"."{ref_col}"'
                    relationships.append(
                        f'"{table}"."{name}" → "{ref_table}"."{ref_col}" (N:1)'
                    )

                col_descriptions.append(desc)

            lines.append(f'{table_sql}({", ".join(col_descriptions)})')

        summary = "[TABLES]\n" + "\n".join(lines)

        if relationships:
            summary += "\n\n[RELATIONSHIPS]\n" + "\n".join(relationships)

        return summary

    except Exception as e:
        return f"Error generating summary: {e}"
