import mysql.connector

try:
    # 1. MySQL Database se connect kar rahe hain
    conn = mysql.connector.connect(
        host="localhost",
        user="root",          # Agar aapka username alag hai toh wo dalo
        password="root1234",      # Yahan apna MySQL workbench ka password dalo
        database="Bhopal_NDT_Employees" # Jo database humne banaya tha
    )

    if conn.is_connected():
        print("--- MySQL Connected Successfully! ---")
        cursor = conn.cursor()
        
        # 2. Query run kar rahe hain Python ke through
        cursor.execute("SELECT emp_id, first_name, salary FROM employees;")
        
        # 3. Saara data fetch kar rahe hain
        records = cursor.fetchall()
        
        print("\nFetching Employee Data via Python:")
        print("-" * 40)
        for row in records:
            print(f"ID: {row[0]} | Name: {row[1]} | Salary: ₹{row[2]}")
        print("-" * 40)

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # 4. Connection band kar rahe hain
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("\nDatabase connection closed.")