from patients import register_patient, view_patients
from appointments import book_appointment, view_appointments
from billing import add_bill, view_bills

def main():
    while True:
        print("\n--- Hospital Management System 🏥 ---")
        print("1. Register Patient")
        print("2. View Patients")
        print("3. Book Appointment")
        print("4. View Appointments")
        print("5. Add Bill")
        print("6. View Bills")
        print("7. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            phone = input("Phone: ")
            address = input("Address: ")
            register_patient(name, age, gender, phone, address)

        elif choice == "2":
            view_patients()

        elif choice == "3":
            patient_id = int(input("Patient ID: "))
            doctor_id = int(input("Doctor ID: "))
            date = input("Appointment Date (YYYY-MM-DD): ")
            book_appointment(patient_id, doctor_id, date)

        elif choice == "4":
            view_appointments()

        elif choice == "5":
            patient_id = int(input("Patient ID: "))
            amount = float(input("Amount: "))
            date = input("Payment Date (YYYY-MM-DD): ")
            add_bill(patient_id, amount, date)

        elif choice == "6":
            view_bills()

        elif choice == "7":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()