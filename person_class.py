# Create a person class

class Person():
    def __init__(self, name, date_of_birth, friends=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.friends = friends if friends else []

    def __str__(self):
        return 'Name: ' + self.name + ', Date of Birth: ' +  str(self.date_of_birth) + ', Num. of friends: ' + str(len(self.friends))


# Test if input_list is correct
test_person = Person('Cham', '2001-05-30', friends=['Jas', 'Caitlin', 'Dylan'])

print(test_person)