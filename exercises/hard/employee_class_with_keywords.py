''' Employee Class with Keywords
Create a class Employee that will take a full name as argument, as well as a set of none, one or more keywords. Each instance should have a name and a lastname attribute plus one more attribute for each of the keywords, if any.

Examples
john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

john.name ➞ "John"
mary.lastname ➞ "Major"
richard.height ➞ 178
giancarlo.nationality ➞ "Italian"
Notes
First and last names will be separated by whitespace. The test will not include any middle names or initials.
The value of the keywords can be an int, a str or a list.'''


class Employee:
    def __init__(self, full_name, **kwargs):
        name = full_name.split()
        self.name = name[0]
        self.lastname = name[1]
        
        for key, value in kwargs.items():
            setattr(self, key, value)

john = Employee("John Doe") 
mary = Employee("Mary Major", salary=120000) 
richard = Employee("Richard Roe", salary=110000, height=178) 
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian") 


print(john.name)
print(mary.lastname)
print(richard.height) 
print(giancarlo.nationality) 