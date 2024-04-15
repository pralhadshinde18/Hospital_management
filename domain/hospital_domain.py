from schema.hospital_schema import HospitalCreate


class HospitalDomain:
    def __init__(self, hospital_data: HospitalCreate):
        self.validate(hospital_data)
        self.hospital_data = hospital_data

    def validate(self, hospital_data: HospitalCreate):
        if hospital_data.rating > 5:
            raise ValueError("Rating must 5 or below")