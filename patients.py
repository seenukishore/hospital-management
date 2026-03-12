from db_config import get_connection

def register_patient(name, age, gender, phone, address):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO patients (name, age, gender, phone, address) VALUES (%s, %s, %s, %s, %s)",
                   (name, age, gender, phone, address))
    conn.commit()
    print(f"Patient '{name}' registered successfully! ✅")
    conn.close()

def view_patients():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    print("\n--- All Patients ---")
    for p in patients:
        print(f"ID: {p[0]} | Name: {p[1]} | Age: {p[2]} | Gender: {p[3]} | Phone: {p[4]}")
    conn.close()