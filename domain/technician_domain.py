from schema.technician_schema import TechnicianCreate


class TechnicianDomain:
    def __init__(self, technician_data: TechnicianCreate):
        self.validate(technician_data)
        self.technician_data = technician_data

    def validate(self, technician_data: TechnicianCreate):
        if technician_data.contact_number < 1:
            raise ValueError("contact number must be greater than 1")




