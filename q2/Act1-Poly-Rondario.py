class Patient:
    def __init__(self, name: str, bill_amount: float):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount: float):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount

    # New method
    def display_patient_type(self):
        print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


class PhilhealthPatient(Patient):
    def __init__(self, name: str, bill_amount: float):
        super().__init__(name, bill_amount)

    # Overridden method: 15% discount
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85

    # Overridden method
    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


if __name__ == "__main__":
    p1 = Patient("Juan Dela Cruz", 1000.0)
    p2 = SeniorPatient("Maria Clara", 1000.0)
    p3 = PhilhealthPatient("Crisostomo Ibarra", 1000.0)

    patients = [p1, p2, p3]

    for p in patients:
        print(f"Name: {p.get_name()}")
        p.display_patient_type()
        print(f"Total Bill: ₱{p.calculate_bill():.2f}")
        print("-" * 30)