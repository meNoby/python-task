class Person:

    def __init__(self, name=None, surname=None, father_name=None, age=None, gender=None, height=None, weight=None):
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def __str__(self):
        f"{self.name} is a person"

    def print_info(self):
        attr = vars(self)
        print('\n'.join("%s: %s" % item for item in attr.items()), "\n")


class Employee(Person):

    experience_baseline = 5

    def __init__(self, organization=None, specialty=None, position=None, salary=None, experience=experience_baseline, *args):
        super().__init__(*args)
        self.organization = organization
        self.specialty = specialty
        self.position = position
        self.salary = salary
        self.experience = experience

    def __str__(self):
        return f"Official -> Name: {self.name}, Organization: {self.organization}"


class Organization:

    employees = list()

    @staticmethod
    def print_info(employees):
        print(f"\nHere's a list of employees:")
        for item in employees:
            print(item)
    
    @staticmethod
    def print_info_detailed(employees):
        print(f"\nHere's a detailed list of employees:")
        for item in employees:
            item.print_info()