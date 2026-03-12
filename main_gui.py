import tkinter as tk
from tkinter import messagebox, ttk
from patients import register_patient, view_patients
from appointments import book_appointment, view_appointments
from billing import add_bill, view_bills

# Main Window
root = tk.Tk()
root.title("Hospital Management System 🏥")
root.geometry("600x500")
root.config(bg="#f0f4f8")

# Title
title = tk.Label(root, text="🏥 Hospital Management System",
                 font=("Arial", 20, "bold"), bg="#f0f4f8", fg="#2c3e50")
title.pack(pady=20)

# Buttons Frame
frame = tk.Frame(root, bg="#f0f4f8")
frame.pack(pady=10)

def open_register_patient():
    win = tk.Toplevel(root)
    win.title("Register Patient")
    win.geometry("400x350")
    win.config(bg="#f0f4f8")

    tk.Label(win, text="Register Patient", font=("Arial", 15, "bold"), bg="#f0f4f8").pack(pady=10)

    tk.Label(win, text="Name:", bg="#f0f4f8").pack()
    name = tk.Entry(win, width=30)
    name.pack()

    tk.Label(win, text="Age:", bg="#f0f4f8").pack()
    age = tk.Entry(win, width=30)
    age.pack()

    tk.Label(win, text="Gender:", bg="#f0f4f8").pack()
    gender = tk.Entry(win, width=30)
    gender.pack()

    tk.Label(win, text="Phone:", bg="#f0f4f8").pack()
    phone = tk.Entry(win, width=30)
    phone.pack()

    tk.Label(win, text="Address:", bg="#f0f4f8").pack()
    address = tk.Entry(win, width=30)
    address.pack()

    def submit():
        register_patient(name.get(), int(age.get()), gender.get(), phone.get(), address.get())
        messagebox.showinfo("Success", f"Patient '{name.get()}' registered! ✅")
        win.destroy()

    tk.Button(win, text="Register", command=submit, bg="#27ae60", fg="white", width=20).pack(pady=10)

def open_view_patients():
    win = tk.Toplevel(root)
    win.title("All Patients")
    win.geometry("600x400")
    win.config(bg="#f0f4f8")

    tk.Label(win, text="All Patients", font=("Arial", 15, "bold"), bg="#f0f4f8").pack(pady=10)

    tree = ttk.Treeview(win, columns=("ID", "Name", "Age", "Gender", "Phone"), show="headings")
    for col in ("ID", "Name", "Age", "Gender", "Phone"):
        tree.heading(col, text=col)
        tree.column(col, width=100)
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    from db_config import get_connection
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age, gender, phone FROM patients")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    conn.close()

def open_book_appointment():
    win = tk.Toplevel(root)
    win.title("Book Appointment")
    win.geometry("400x300")
    win.config(bg="#f0f4f8")

    tk.Label(win, text="Book Appointment", font=("Arial", 15, "bold"), bg="#f0f4f8").pack(pady=10)

    tk.Label(win, text="Patient ID:", bg="#f0f4f8").pack()
    patient_id = tk.Entry(win, width=30)
    patient_id.pack()

    tk.Label(win, text="Doctor ID:", bg="#f0f4f8").pack()
    doctor_id = tk.Entry(win, width=30)
    doctor_id.pack()

    tk.Label(win, text="Date (YYYY-MM-DD):", bg="#f0f4f8").pack()
    date = tk.Entry(win, width=30)
    date.pack()

    def submit():
        book_appointment(int(patient_id.get()), int(doctor_id.get()), date.get())
        messagebox.showinfo("Success", "Appointment Booked! ✅")
        win.destroy()

    tk.Button(win, text="Book", command=submit, bg="#2980b9", fg="white", width=20).pack(pady=10)

def open_add_bill():
    win = tk.Toplevel(root)
    win.title("Add Bill")
    win.geometry("400x280")
    win.config(bg="#f0f4f8")

    tk.Label(win, text="Add Bill", font=("Arial", 15, "bold"), bg="#f0f4f8").pack(pady=10)

    tk.Label(win, text="Patient ID:", bg="#f0f4f8").pack()
    patient_id = tk.Entry(win, width=30)
    patient_id.pack()

    tk.Label(win, text="Amount:", bg="#f0f4f8").pack()
    amount = tk.Entry(win, width=30)
    amount.pack()

    tk.Label(win, text="Date (YYYY-MM-DD):", bg="#f0f4f8").pack()
    date = tk.Entry(win, width=30)
    date.pack()

    def submit():
        add_bill(int(patient_id.get()), float(amount.get()), date.get())
        messagebox.showinfo("Success", "Bill Added! ✅")
        win.destroy()

    tk.Button(win, text="Add Bill", command=submit, bg="#8e44ad", fg="white", width=20).pack(pady=10)

# Main Buttons
buttons = [
    ("👤 Register Patient", open_register_patient, "#27ae60"),
    ("📋 View Patients", open_view_patients, "#2980b9"),
    ("📅 Book Appointment", open_book_appointment, "#e67e22"),
    ("💰 Add Bill", open_add_bill, "#8e44ad"),
]

for text, command, color in buttons:
    tk.Button(frame, text=text, command=command, bg=color, fg="white",
              width=25, height=2, font=("Arial", 11)).pack(pady=5)

root.mainloop()