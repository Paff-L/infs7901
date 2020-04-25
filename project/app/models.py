class Patient():
    def __init__(self, record):
        self.patient_id = record[0]
        self.first_name = record[1]
        self.last_name = record[2]
        self.gender = record[3]
        self.nationality = record[4]
        self.state = record[5]
        self.postcode = record[6]
        self.date_of_birth = record[7]
        self.phone_number = record[8]