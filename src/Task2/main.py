from customclass import Person, Employee, Organization
import random

# * TESTING CLASS METHODS

test = Person("alpha", "beta", "gamma", 10, "male", 180, 70)

test2 = Employee("test.org", "tester", "manager", 0, 0, "alpha", "beta", "gamma", 10, "male", 180, 70)

print("\n`print_info` method from class Person:\n")
test.print_info()

print("\n`print_info` method from class Employee:\n")
test2.print_info()

# * TESTING ORGANIZATION

print("\nTesting Organization:\n")

org_list = ["test org 1", "test org 2", "test org 3"]
specialty_list = ["engineer", "manager", "marketing", "tester"]
position_list = ["junior", "middle", "senior"]

def sort_employees(org):
    answer_arr = list()
    for off in org:
        if(off.experience >= Employee.experience_baseline):
            answer_arr.append(off)
    return answer_arr     

# Fill with random employees
for i in range(10):
    random_employee = Employee(random.choice(org_list), random.choice(specialty_list), random.choice(position_list), random.randint(5000, 80000),random.randint(0, 8), "generic name", "generic surname", "generic father's name", random.randint(20, 40), "male" if random.randint(1,2) == 1 else "female", random.randint(150, 190), random.randint(45, 75))
    Organization.employees.append(random_employee)
Organization.print_info(Organization.employees)

print("All the employees that have 5 or more years of experience")

Organization.employees = sort_employees(Organization.employees)
Organization.print_info_detailed(Organization.employees)