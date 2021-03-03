# 1.
class Laptop:
    """
    Make the class with composition.
    """
    def __init__(self, battery_capacity, model):
        self.battery = Battery(battery_capacity)
        self.model = model


class Battery:
    """
    Make the class with composition.
    """
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity


# 2.
class Guitar:
    """
    Make the class with aggregation
    """
    def __init__(self, list_of_strings):
        self.list_of_strings = list_of_strings


class GuitarString:
    """
    Make the class with aggregation
    """
    pass


guitar_strings = [GuitarString() for _ in range(6)]
guitar = Guitar(guitar_strings)


# 3.
class Calc:
    """
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """
    @staticmethod
    def add_nums(par1, par2, par3):
        return par1 + par2 + par3


# 4*.
class Pasta:
    """
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """
    def __init__(self, list_of_ingredients):
        self.list_of_ingredients = list_of_ingredients

    @classmethod
    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])


# 5*.
class Concert:
    """
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, visitor_count):
        if visitor_count <= self.max_visitors_num:
            self._visitors_count = visitor_count
        else:
            self._visitors_count = self.max_visitors_num


# 6.
import dataclasses

@dataclasses.dataclass
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
    """
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


# 7. Create the same class (6) but using NamedTuple
import collections

AddressBookNamedTuple = collections.namedtuple('AddressBookNamedTuple',
                                               ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])


# 8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'AddressBook(key={self.key}, name={self.name}, phone_number={self.phone_number}, ' \
               f'address={self.address}, email={self.email}, birthday={self.birthday}, age={self.age})'


# 9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"

person_object = Person()
person_object.age = 25
setattr(person_object, 'age', 49)


# 10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(3, "John")
student.email = "john@cursor.edu"
student_email = getattr(student, 'email')
print(student_email)


# 11*.
class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature_Fahrenheit(self):
        return (self._temperature * 1.8) + 32


# create an object
T = Celsius(82)
print(T.temperature_Fahrenheit)
