import mysql.connector

#connect mysql with python
connection = mysql.connector.connect(
        host="localhost",
        user="khushi",
        password="Khushi2494",
        database="my_database"
    )


#create cursor
cursor = connection.cursor()


# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    age INT
)
""")

# Insert data
insert_query = """
INSERT IGNORE INTO users (id, name, email, age)
VALUES (%s, %s, %s, %s)

"""

values = [
    (101,"Khushi", "khushi@gmail.com", 22),
    (102,"palak", "palak@gmail.com", 25),
    (103,"Riya", "riya@gmail.com", 21)
]

cursor.executemany(insert_query, values)
connection.commit()

print("Table created and data inserted successfully")

#update data
update_data = """
UPDATE users
SET age = %s
WHERE id = %s
"""
val = [
    (21,101),
    (22,102),
    (25,103)
]

cursor.executemany(update_data , val)
connection.commit()

print("table updated successfully.")

cursor.close()
connection.close()


