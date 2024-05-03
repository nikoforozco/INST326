from patientportal import parse_patient_info
from argparse import ArgumentParser
from healthcareDB import Patient
from healthcareDB import HealthcareDB 
filename = 'testpatientinfo.txt'


def test_parse_patient_info_function(filename):
    # Test logic for parse_patient_info
    # Use assert statements to check expected outputs
    expected = {
        54321: Patient(
        54321, 'Alyssa', 'Manio', 'Female', 'Asian', '02/25/1998', '9715 63rd Ave, Greenbelt MD 20770', '123-456-7890', 'ali@umd.edu', 'Medicare'    
        )
    }

    actual = parse_patient_info(filename)
    
    assert actual == expected

if __name__ == '__main__':
    test_parse_patient_info_function()

