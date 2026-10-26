
# Parent class
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


# Child class for Senior Citizens (20% discount)
class SeniorPatient(Patient):
    def calculate_bill(self):
        # Applying a 20% discount
        return self.get_bill_amount() * 0.8


# Child class for PhilHealth Members (15% discount)
class PhilHealthPatient(Patient):
    def calculate_bill(self):
        # Applying a 15% discount
        return self.get_bill_amount() * 0.85


# example
if __name__ == "_main_":
    reg_patient = Patient("Juan Dela Cruz", 15000.0)
    senior_patient = SeniorPatient("Maria Santos", 5000.0)
    philhealth_patient = PhilHealthPatient("Pedro Reyes", 5000.0)

    print(f"Regular Patient ({reg_patient.get_name()}): ₱{reg_patient.calculate_bill():.2f}")
    print(f"Senior Citizen ({senior_patient.get_name()}): ₱{senior_patient.calculate_bill():.2f}")
    print(f"PhilHealth Member ({philhealth_patient.get_name()}): ₱{philhealth_patient.calculate_bill():.2f}")