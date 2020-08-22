class Person(object):
    def __init__(self,name,age,gendre):
        self.name = name
        self.age = age
        self.gendre = gendre
    def setName(self,name):
        self.name = name
    def setAge(self,age):
        self.age = int(age)
    def setGendre(self,gendre):
        self.gendre = gendre
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGendre(self):
        return self.gendre
    def sayHi(self,namePerson):
        return print('Hi',namePerson,'nice to meet you.')
    def start(self):
        print("""
                Hellow there, I'm """,self.name,',',"""an instance from a class called 'Person'.
                you can modify my properties with the following commands:

                name:   set a name to the 'person', my actual name is""",self.name,""".
                age:    set an age to the 'person', my actual age is""",self.age,""".
                gendre: set a gendre to the 'person, my actual gendre is""",self.gendre,""".
                help: pritns the list of commands.
                
                Also, I have a few interesting methods like: 

                birthday : add 1 to the actual age of "person".
                say hi : says hi to a name person.



                """)

createPerson = input('Wanna create a new person? (it will be an instance of a class.) Y/N : ')
if createPerson == 'Y' or createPerson == 'yes' or createPerson == 'Yes' or createPerson == 'y':
    print('person created')
    
    name = input('How want to call to this new person?: ')
    if name == '' or name == None:
        print ('the name only can be letters.')
    age = int(input('Enter the age of the new person: '))
    if age == '' or age == None:
        print('The age only can be integer numbers')
    gendre = input('Enter the gendre of the new person: ')
    if gendre == '' or gendre == None:
        print('the gendre only can contein letters.')
    person = Person(name,age,gendre)
    person.start()
    while True:
        command = input('write a command: ')
        if command == 'name':
            setName = input('Enter the new name for "person": ')
            person.setName(setName)
            print('Nice choise, now my name is',person.getName())
            pass
        elif command == 'age':
            setAge = input('Enter the new age fot "person": ')
            person.setAge(setAge)
            print('Wow! now my new age is',person.getAge())
            pass
        elif command == 'gendre':
            setGendre = input('Enter the new gendre for "person": ')
            person.setGendre(setGendre)
            print('Oh... now my new gendre is',person.getGendre())
            pass
        elif command == 'help':
            person.start()
            pass
        elif command == 'birthday':
            print('Wow... has pass a year? my age now is',person.age + 1)
            person.setAge(person.age + 1)
        elif command == 'say hi':
            namePerson = input('Enter the name of the person you want to say hi: ')
            person.sayHi(namePerson)
elif createPerson == 'N' or createPerson == 'No' or createPerson == 'No' or createPerson == 'n':
    print('Well see you when you want to try it.')
elif createPerson == '':
    print('No such command like that.')
else:
    print('no such command like',createPerson)





