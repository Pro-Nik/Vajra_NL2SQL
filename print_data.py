import mysql.connector
from mysql.connector import Error

def print_table_data():
    try:
        # ✅ Connect to MySQL
        connection = mysql.connector.connect(
            host='localhost',
            user='root',         
            password='Diat2024',     
            database='Vajra_NL2SQL'      
        )

        if connection.is_connected():
            print("Connected to MySQL")

            # Choose the table you want to read
            table_name = 'login_events'  

            cursor = connection.cursor()
            query = f"SELECT * FROM {table_name};"
            cursor.execute(query)

            # Fetch all rows
            rows = cursor.fetchall()

            # Print rows with column names
            column_names = [desc[0] for desc in cursor.description]
            print("\n Table:", table_name)
            print(" | ".join(column_names))
            print("-" * 50)

            for row in rows:
                print(" | ".join(str(col) for col in row))

    except Error as e:
        print(" Error reading from MySQL:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("\n🔌 MySQL connection closed.")

if __name__ == "__main__":
    print_table_data()
