import sqlite3

connection = sqlite3.connect('user.db')
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS users(
    id integer primary key,
    first_name text,
    last_name text,
    phone text
);
"""

cursor.execute(create_table_query)
connection.commit()
connection.close()


sample_data_query = """
INSERT INTO users(id, first_name, last_name, phone)
VALUES (?, ?, ?, ?)
"""

sample_data = [
    (1234, 'beta', 'betaii', '0987'),
    (12345, 'gama', 'gamaii', '0987'),
    (123456, 'epsilon', 'epsilonii', '0987'),
    (1234567, 'zeta', 'zetaii', '0987'),
]

with sqlite3.connect('user.db') as connection:
    cursor = connection.cursor()
    cursor.executemany(sample_data_query, sample_data)
