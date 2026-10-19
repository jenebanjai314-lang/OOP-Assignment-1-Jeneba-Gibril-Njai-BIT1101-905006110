# Patient Record Management System
class Patient:
    # Class attribute
    total_patients = 0

    def __init__(self, patient_id, name, age, gender, condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition

        Patient.total_patients += 1

    # Instance method
    def display_info(self):
        print("\n--- Patient Information ---")
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Reason for Visit:", self.condition)

    # Instance method
    def update_record(self, name, age, gender, condition):
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition
        print("Patient record updated successfully!")


class PatientManagementSystem:

    def __init__(self):
        # List data structure
        self.patients = []

    # Add a patient
    def add_patient(self):
        patient_id = input("Enter Patient ID: ")

        if self.search_patient(patient_id, show_message=False):
            print("This Patient ID already exists.")
            return

        name = input("Enter Patient Name: ")

        try:
            age = int(input("Enter Patient Age: "))
            if age < 0 or age > 130:
                print("Please enter a valid age.")
                return
        except ValueError:
            print("Age must be a number.")
            return

        gender = input("Enter Patient Gender: ")
        condition = input("Enter Reason for Visit: ")

        patient = Patient(
            patient_id, name, age, gender, condition
        )

        self.patients.append(patient)
        print("Patient registered successfully!")

    # Display all patients
    def display_all_patients(self):
        if not self.patients:
            print("No patient records available.")
            return

        print("\n=== ALL PATIENT RECORDS ===")

        for patient in self.patients:
            patient.display_info()

    # Search for a patient
    def search_patient(self, patient_id, show_message=True):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                if show_message:
                    patient.display_info()
                return patient

        if show_message:
            print("Patient not found.")

        return None

    # Update patient details
    def update_patient(self):
        patient_id = input("Enter Patient ID to update: ")
        patient = self.search_patient(
            patient_id, show_message=False
        )

        if patient is None:
            print("Patient not found.")
            return

        print("Enter the updated information.")

        name = input("Enter New Name: ")

        try:
            age = int(input("Enter New Age: "))
            if age < 0 or age > 130:
                print("Please enter a valid age.")
                return
        except ValueError:
            print("Age must be a number.")
            return

        gender = input("Enter New Gender: ")
        condition = input("Enter New Reason for Visit: ")

        patient.update_record(name, age, gender, condition)

    # Class method
    @classmethod
    def show_total_patients(cls):
        print("Total patients registered:", Patient.total_patients)


# Main program
def main():
    system = PatientManagementSystem()

    while True:
        print("\n================================")
        print(" PATIENT RECORD MANAGEMENT SYSTEM")
        print("================================")
        print("1. Register a Patient")
        print("2. Display All Patients")
        print("3. Search for a Patient")
        print("4. Update Patient Record")
        print("5. Show Total Patients")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            system.add_patient()

        elif choice == "2":
            system.display_all_patients()

        elif choice == "3":
            patient_id = input("Enter Patient ID: ")
            system.search_patient(patient_id)

        elif choice == "4":
            system.update_patient()

        elif choice == "5":
            PatientManagementSystem.show_total_patients()

        elif choice == "6":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()


