import mysql.connector

try:
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",          
        password="root1234",    
        database="Bhopal_NDT_Employees" 
    )

    if conn.is_connected():
        print("--- MySQL Connected Successfully! ---")
        cursor = conn.cursor()
        
      
        cursor.execute("SELECT emp_id, first_name, salary FROM employees;")
        
       
        records = cursor.fetchall()
        
        print("\nFetching Employee Data via Python:")
        print("-" * 40)
        for row in records:
            print(f"ID: {row[0]} | Name: {row[1]} | Salary: ₹{row[2]}")
        print("-" * 40)

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("\nDatabase connection closed.")
