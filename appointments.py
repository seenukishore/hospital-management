from db_config import get_connection

def book_appointment(patient_id, doctor_id, appointment_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO appointments (patient_id, doctor_id, appointment_date, status) VALUES (%s, %s, %s, %s)",
                   (patient_id, doctor_id, appointment_date, "Booked"))
    conn.commit()
    print(f"Appointment booked successfully! ✅")
    conn.close()

def view_appointments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.id, p.name, d.name, a.appointment_date, a.status 
        FROM appointments a
        JOIN patients p ON a.patient_id = p.id
        JOIN doctors d ON a.doctor_id = d.id
    """)
    appointments = cursor.fetchall()
    print("\n--- All Appointments ---")
    for a in appointments:
        print(f"ID: {a[0]} | Patient: {a[1]} | Doctor: {a[2]} | Date: {a[3]} | Status: {a[4]}")
    conn.close()