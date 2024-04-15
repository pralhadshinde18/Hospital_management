from schema.reporting_doctor_schema import ReportingDoctorCreate


class ReportingDoctorDomain:
    def __init__(self, reporting_doctor_data: ReportingDoctorCreate):
        self.validate(reporting_doctor_data)
        self.reporting_doctor_data = reporting_doctor_data

    def validate(self, reporting_doctor_data: ReportingDoctorCreate):
        if reporting_doctor_data.contact_number < 1:
            raise ValueError("contact number must be greater than 1")
