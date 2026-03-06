```python
import sqlite3

def create_table(db_name, table_name, columns):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    columns_str = ', '.join([f'{col[0]} {col[1]}' for col in columns])
    create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})'
    
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

def insert_data(db_name, table_name, data):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    columns = ', '.join(data.keys())
    values = ', '.join([f':{k}' for k in data.keys()])
    insert_query = f'INSERT INTO {table_name} ({columns}) VALUES ({values})'
    
    cursor.execute(insert_query, data)
    conn.commit()
    conn.close()

def query_data(db_name, query, params=None):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    
    rows = cursor.fetchall()
    conn.close()
    return rows
```