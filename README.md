# This is my python task #1 and #2 for Uni

## >>> Task #1 review <<<

### Requirements:
1. Make a `Weather` class

```python
class Weather:
```

2. Add weather data like:
    * Date
    * Average temperature
    * Atmospheric pressure
    * Precipitation

```python
def __init__(self=None, date=None, temp=None, pressure=None, precipitation=None):
    self.date = date
    self.tempavg = temp
    self.pressure = pressure
    self.precipitation = precipitation
```
    
3. Define constructors, methods, a way to read data

```python
# constructor, technically counts as changing data since it overrides default atributes
def __init__() 

# override of a special method, allows to read data
def __str__(self):
    return f"date: {self.date}\ntempavg: {self.tempavg} degree C\npressure: {self.pressure} mmHg\nprecipitation: {self.precipitation}" 
```

4. Find days with the highest pressure change (pressure delta)

```python
def max_pressure_delta(arr):
    lo = Weather(0, 0, 1000, 0)
    hi = Weather(0, 0, 0, 0)
    for i in arr:
        lo = i if lo.pressure > i.pressure else lo
        hi = i if hi.pressure < i.pressure else hi
    return hi, lo

highest, lowest = max_pressure_delta(weather_list)
```

## >>> Task #2 review <<<

### Requirements:

1. Create a `Person` class with attributes:
    * Surname
    * Name
    * Father's name
    * Birth date (age for simplicity)
    * Gender
    * Height
    * Weight

```python
class Person:

# technically counts as changing data since it overrides default atributes
def __init__(self, name=None, surname=None, father_name=None, age=None, gender=None, height=None, weight=None):
    self.name = name
    self.surname = surname
    self.father_name = father_name
    self.age = age
    self.gender = gender
    self.height = height
    self.weight = weight
```

2. Define methods to read data

```python
def print_info(self):
    attr = vars(self)
    print('\n'.join("%s: %s" % item for item in attr.items()), "\n")
```

3. Overload an operator

```python
def __str__(self):
        f"{self.name} is a person"
```

4. Create an `Employee` class that derives from `Person` and adds attributes:
    * Organization
    * Specialty
    * Position
    * Salary
    * Experience

```python
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
```

5.  Create `Organization` class which holds a sequence of `Employee` class objects. Find number of people whose experience is above baseline value

```python
class Organization:

    employees = list()
``` 

```python
# Fill with random employees
for i in range(10):
    random_employee = Employee(random.choice(org_list), 
                               random.choice(specialty_list), 
                               random.choice(position_list), 
                               random.randint(5000, 80000),
                               random.randint(0, 8), 
                               "generic name", 
                               "generic surname", 
                               "generic father's name", 
                               random.randint(20, 40), 
                               "male" if random.randint(1,2) == 1 else "female", 
                               random.randint(150, 190), 
                               random.randint(45, 75))
    Organization.employees.append(random_employee)
```

```python
def sort_employees(org):
    answer_arr = list()
    for off in org:
        if(off.experience >= Employee.experience_baseline):
            answer_arr.append(off)
    return answer_arr 
```

6. Use an iterator when working with an object sequence

```python
    @staticmethod
    def print_info_detailed(employees):
        print(f"\nHere's a detailed list of employees:")
        for item in employees: # for loop uses iterator logic under the hood
            item.print_info()
```
