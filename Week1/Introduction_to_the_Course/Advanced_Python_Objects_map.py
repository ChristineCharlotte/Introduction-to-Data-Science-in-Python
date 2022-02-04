class Person:
    department = 'School of Information'

    # def __init__(self):
    #     self.location = None
    #     self.name = None

    def set_name(self, new_name):
        self.name = new_name

    def set_location(self, new_location):
        self.location = new_location


person = Person()
person.set_name('Jun Bingo')
person.set_location('Shanghai, China')
# print('{} live in {} and works in the department {}'.format(person.name, person.location, person.department))

store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
# print(cheapest)

# Data Cleaning
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']


def split_title_and_name(person):
    title = person.split()[0]
    last_name = person.split()[-1]
    return '{} {}'.format(title, last_name)


print(list(map(split_title_and_name, people)))
