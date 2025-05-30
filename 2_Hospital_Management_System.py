import json
from datetime import datetime

patients = []
doctors = [{"id": 1, "name": "Dr. Smith"}, {"id": 2, "name": "Dr. Adams"}]
appointments = []

def register_patient():
    name = input("Enter patient name: ")
    age = input("Enter age: ")
    pid = len(patients) + 1
    patients.append({"id": pid, "name": name, "age": age})
    print(f"Patient {name} registered with ID {pid}")

def assign_doctor():
    if not patients:
        print("No patients found.")
        return
    pid = int(input("Enter patient ID: "))
    for doc in doctors:
        print(f"{doc['id']}: {doc['name']}")
    did = int(input("Choose doctor ID: "))
    date = input("Enter appointment date (YYYY-MM-DD): ")
    appointments.append({"patient_id": pid, "doctor_id": did, "date": date})
    print("Appointment scheduled.")

def daily_report():
    today = datetime.now().date().isoformat()
    print(f"Appointments for {today}:")
    for a in appointments:
        if a["date"] == today:
            pname = next(p["name"] for p in patients if p["id"] == a["patient_id"])
            dname = next(d["name"] for d in doctors if d["id"] == a["doctor_id"])
            print(f"{pname} with {dname}")

def main():
    while True:
        print("\n--- Hospital Management System ---")
        print("1. Register Patient")
        print("2. Assign Doctor")
        print("3. Daily Report")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            register_patient()
        elif choice == '2':
            assign_doctor()
        elif choice == '3':
            daily_report()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()