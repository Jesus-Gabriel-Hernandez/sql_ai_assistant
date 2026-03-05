# =========================================
# DB_UTILS Module
# =========================================

import os
import sqlite3 as sql
import pandas as pd


# -----------------------------
# 1. Connect to SQLite database
# -----------------------------

def connect_sqlite_db(path: str) -> sql.Connection:
    """
    Opens a connection to a SQLite database.

    Args:
        path (str): Path to the .db file.

    Returns:
        sqlite3.Connection: Active database connection.

    Example:
        conn = connect_sqlite_db("northwind.db")
    """ 
        
    try:
        conn = sql.connect(path, check_same_thread=False)
        conn.execute("PRAGMA journal_mode=WAL;") # To activate write mode
        conn.execute("PRAGMA synchronous=NORMAL;") # Better performance
        return conn
    except Exception as e:
        raise RuntimeError(f"Error connecting to database: {e}")

# ============================================================
# 2. List all tables in the database 
# ============================================================

def list_tables(conn) -> list:

    """
    Returns a list of all tables in the SQLite database.

    Args:
        conn (sqlite3.Connection): Active database connection.

    Returns:
        list: List of table names.

    Example:
        tables = list_tables(conn)
    """
    
    try:
        cursor = conn.cursor() 
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' and name != 'sqlite_sequence' ORDER BY name;")
        return [row[0] for row in cursor.fetchall()] 
    except Exception as e: 
        return f"Error retrieving tables: {e}"


# -----------------------------
# 3. Get columns of a table
# -----------------------------

def get_columns(conn, table: str) -> pd.DataFrame:
    """
    Returns a DataFrame with the columns of a given table.

    Args:
        conn (sqlite3.Connection): Active database connection.
        table (str): Table name.

    Returns:
        pd.DataFrame: Columns with name, type, PK, and NULL info.

    Example:
        cols = get_columns(conn, "Customers")
    """
    
    try: 
        cursor = conn.cursor() 
        cursor.execute(f"PRAGMA table_info('{table}');") 
        rows = cursor.fetchall() 
        
        return pd.DataFrame(rows, columns=[ 
            "cid", "name", "type", "notnull", "dflt_value", "pk"
        ])
        
    except Exception as e: 
        raise RuntimeError(f"Error retrieving columns for table '{table}': {e}")

# ============================================================ 
# 4. Get foreign keys of a table 
# ============================================================

def get_foreign_keys(conn, table: str) -> pd.DataFrame:
    """ 
    Returns a DataFrame with the foreign keys of a given table.
    
    Args: 
        conn (sqlite3.Connection): Active database connection.
        table (str): Table name. 
    
    Returns: 
        pd.DataFrame: Foreign key relationships. 
    
    Example: 
        fks = get_foreign_keys(conn, "Orders")
        
    """
    try: 
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA foreign_key_list('{table}');") 
        rows = cursor.fetchall() 
        
        return pd.DataFrame(rows, columns=[ 
            "id", "seq", "table", "from", "to", "on_update", "on_delete", "match" 
        
        ])
    except Exception as e:
        raise RuntimeError(f"Error retrieving foreign keys for table '{table}': {e}")


# -----------------------------
# 5. Execute a SQL query
# -----------------------------

def execute_query(conn, sql: str) -> tuple: 
    """ 
    Executes a SQL query and returns the rows and column names. 
    
    Args: 
        conn (sqlite3.Connection): 
        Active database connection. sql (str): SQL query to execute.
    
    Returns: 
        tuple: (rows, columns) 
    
    Example: 
        rows, cols = execute_query(conn, "SELECT * FROM Customers;") 
    """ 
    try: 
        cursor = conn.cursor() 
        cursor.execute(sql) 
        rows = cursor.fetchall() 
        
        columns = [desc[0] for desc in cursor.description] if cursor.description else [] 
        return rows, columns 
    
    except Exception as e: 
        raise RuntimeError(f"Error executing SQL query: {e}")

# ============================================================ 
# 6. Validate SQL (syntax and execution) 
# ============================================================

def validate_sql(conn, sql: str) -> tuple:
    """
    Validates a SQL query by attempting to execute it.

    Args:
        conn (sqlite3.Connection): Active database connection.
        sql (str): SQL query to validate.

    Returns:
        tuple: (True, None) if valid, (False, error_message) if invalid.

    Example:
        valid, error = validate_sql(conn, "SELECT * FROM Orders;")
    """

    try: 
        cursor = conn.cursor()
        cursor.execute(sql)
        return True, None
    
    except Exception as e: 
        return False, str(e)
    

# ============================================================
# 7. Generate a full database summary
# ============================================================

def get_unique_columns(conn, table: str) -> list:
    """
    Returns a list of columns that have UNIQUE constraints.
    """
    try:
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA index_list('{table}')")
        indexes = cursor.fetchall()

        unique_cols = []

        for idx in indexes:
            # idx[2] == 1 means UNIQUE index
            if idx[2] == 1:
                cursor.execute(f"PRAGMA index_info('{idx[1]}')")
                info = cursor.fetchall()
                for col in info:
                    unique_cols.append(col[2])

        return unique_cols

    except Exception:
        return []



def summarize_database(conn) -> str:
    """
    Generates a full summary of the database including:
    - Tables
    - Columns
    - Foreign keys

    Args:
        conn (sqlite3.Connection): Active database connection.

    Returns:
        str: Human-readable summary of the database.

    Example:
        summary = summarize_database(conn)
    """
    tables = list_tables(conn)
    summary_lines = []

    for table in tables:
        summary_lines.append(f"TABLE: {table}")

        # Columns
        columns = get_columns(conn, table)
        summary_lines.append("  COLUMNS:")
        for _, col in columns.iterrows():
            summary_lines.append(
                f"    - {col['name']} | Type: {col['type']} | PK: {col['pk']} | NULL: {col['notnull']}"
            )

        # Foreign keys
        fks = get_foreign_keys(conn, table)
        if not fks.empty:
            summary_lines.append("  FOREIGN KEYS:")
            for _, fk in fks.iterrows():
                summary_lines.append(
                    f"    - {fk['from']} -> {fk['table']}.{fk['to']}"
                )

        summary_lines.append("")

    return "\n".join(summary_lines)