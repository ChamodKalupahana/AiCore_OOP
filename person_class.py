# Import modules

import datetime

# Create a person class

class Person():
    def __init__(self, name, date_of_birth, friends=None):
        self.name = name
        self.date_of_birth = date_of_birth
        self.friends = friends if friends else []

    def __str__(self):
        return 'Name: ' + self.name + ', Date of Birth: ' +  str(self.date_of_birth) + ', Num. of friends: ' + str(len(self.friends))
    
    def __gt__(self, other_person):
        date_self = datetime.datetime.strptime(self.date_of_birth, '%Y-%m-%d')
        date_other_person = datetime.datetime.strptime(other_person.date_of_birth, '%Y-%m-%d')

        # for datetime objects, being > means coming later
        return date_other_person > date_self


# Test if > is correct
Cham = Person('Cham', '2001-05-30', friends=['Jas', 'Caitlin', 'Dylan'])
Jas = Person('Jas', '2003-01-21', friends=['Cham', 'Caitlin'])

print(Cham > Jas)