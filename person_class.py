# Create a person class

class Person():
    def __init__(self, name, date_of_birth, input_list=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.list = input_list if input_list else []

# Test if init is correct

test_person = Person('Cham', 4)

print(test_person.name)
print(test_person.date_of_birth)
print(test_person.list)

# Test if input_list is correct


test_person = Person('Cham', 4, input_list=[1, 2, 3])

print(test_person.list)