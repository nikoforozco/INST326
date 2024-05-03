class Patient:

    '''
    Purpose:
        This class creates a Patient Object that stores specific patient information.
    Attributes:
        self
        patient_id (int): A five digit patient ID unique to each patient
        fname (str): A patient first name
        lname (str): A patient last name
        gender (str): The patient's gender
        race (str): The patient's race
        birthdate (str): The patient's birthdate in MM/DD/YYYY format
        address (str): The patient's address
        phone_num (str): The patient's phone number in 123-456-7890 format
        email (str): The patient's email address
        insurance (str): The patient's health insurance company

    Returns:
        A patient object with all the attributes listed above.

    '''

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

    '''
    Purpose:
        Creates a healthcare database that stores patient information in a dictionary wiht keys being the unique patient ID and the values being the Patient object

    Methods:
        __init__: creates a dictionary object that will store patient information
        create_patient: creates a new patient that gives a key value pair within the dictionary created in __init__
        remove_patient: removes a patient based on a unique patient ID given within the patients dictionary
        find_patient: finds a patient from a given patient ID 
        save_patient_info: when a patient is created it saves that new information in the Patient Class into the original .txt file given

    Returns:
        self.patients (dictionary): A dictionary of key/value pairs (patient_ID, Patient)

    '''
 
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

