from db_config import get_connection

def add_bill(patient_id, amount, payment_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO billing (patient_id, amount, payment_date, status) VALUES (%s, %s, %s, %s)",
                   (patient_id, amount, payment_date, "Paid"))
    conn.commit()
    print(f"Bill added successfully! ✅")
    conn.close()

def view_bills():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT b.id, p.name, b.amount, b.payment_date, b.status
        FROM billing b
        JOIN patients p ON b.patient_id = p.id
    """)
    bills = cursor.fetchall()
    print("\n--- All Bills ---")
    for b in bills:
        print(f"ID: {b[0]} | Patient: {b[1]} | Amount: ₹{b[2]} | Date: {b[3]} | Status: {b[4]}")
    conn.close()