from argparse import ArgumentParser
import sys
import re

class Patient:

    def __init__(self, patient_id, fname, lname, gender, race, birthdate, address, phone_num, email, insurance):
        self.patient_id = patient_id
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.race = race
        self.birthdate = birthdate
        self.address = address
        self.phone_num = phone_num
        self.email = email
        self.insurance = insurance
    
class HealthcareDB:
 
    def __init__(self):
        self.patients = {}

    def create_patient(self, patient):
        self.patients[patient.patient_id] = patient

    def remove_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
    
    def find_patient(self, patient_id):
        return self.patients.get(patient_id)
    
    def save_patients_to_file(self, filename):
        with open(filename, 'w') as file:
            for patient_id, patient in self.patients.items():
                file.write(f"{patient_id}; {patient.fname}; {patient.lname}; {patient.gender}; {patient.race}; {patient.birthdate}; {patient.address}; {patient.phone_num}; {patient.email}; {patient.insurance}\n")

def parse_patient_info(filename):
    patients = {}
    with open(filename, 'r') as file:
        for line in file:
            pattern = r'^(\d+); ([\w\s]+); ([\w\s]+); ([\w\s]+); ([\w\s]+); (\d{2}/\d{2}/\d{4}); ([\w\s,]+); (\d{3}-\d{3}-\d{4}); (\w+@\w+\.\w+); ([\w\s]+)$'
            match = re.match(pattern, line)
            if match:
                patient_id = match.group(1)
                fname = match.group(2)
                lname = match.group(3)
                gender = match.group(4)
                race = match.group(5)
                birthdate = match.group(6)
                address = match.group(7)
                phone_num = match.group(8)
                email = match.group(9)
                insurance = match.group(10)
                patient = Patient(int(patient_id), fname, lname, gender, race, birthdate, address, phone_num, email, insurance)
                patients[int(patient_id)] = patient
    return patients

def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file", help="path to patient file")
    return parser.parse_args(arglist)


def main(filename):
    healthdb = HealthcareDB()

    existing_patients = parse_patient_info(filename)
    for patient_id, patient in existing_patients.items():
        healthdb.create_patient(patient)

    result = None
    while result != "leave":
        result = input("What would you like to do today? [find, remove, create, leave] ")
        if result == "find":
            patient_id = input("What is your patient_id? ")
            patient = healthdb.find_patient(int(patient_id))
            if patient:
                print("Patient information:")
                print(f"Patient ID: {patient.patient_id}")
                print(f"First Name: {patient.fname}")
                print(f"Last Name: {patient.lname}")
                print(f"Gender: {patient.gender}")
                print(f"Race: {patient.race}")
                print(f"Birthdate: {patient.birthdate}")
                print(f"Address: {patient.address}")
                print(f"Phone Number: {patient.phone_num}")
                print(f"Email: {patient.email}")
                print(f"Insurance: {patient.insurance}")
        
            else:
                print("Patient not found in the database.")

        elif result == "remove":
            patient_id = input("What is your patient_id? ")
            patient = healthdb.remove_patient(int(patient_id))
            print("Patient information has been deleted.")

        elif result == "create":
            while True:
                patient_id = input("Create a Patient ID, must consist of 5 integers (Ex. 12345)\nPatient ID: ")
                if int(patient_id) in healthdb.patients:
                    print("Patient ID already exists, please try again.")
                else: 
                    break
                
            fname = input("First Name: ")
            lname = input("Last Name: ")
            gender = input("Gender: ")
            race = input("Race: ")
            birthdate = input("(Ex. MM/DD/YYYY)\nBirthdate: ")
            address = input("(Ex. 14325 House Road, Alexandria VA 98766)\nAddress: ")
            phone_num = input("(Ex. 123-456-7890)\nPhone Number: ")
            email = input("(Ex. youremail@gmail.com)\nEmail: ")
            insurance = input("Insurance: ")
            patient = Patient(int(patient_id), fname, lname, gender, race, birthdate, address, phone_num, email, insurance)
            healthdb.create_patient(patient)
            healthdb.save_patients_to_file(filename)
            print("Your Patient Information has been successfully created.")
            
        elif result == "leave":
            print("Thank you for using my Health Portal!")

        else:
            print("That is not a valid choice, please try again.")
    
    healthdb.save_patients_to_file(filename)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)





