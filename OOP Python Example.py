# This is a Class, A class is a blueprint for creating objects. You can think of a class as a cookie cutter for creating objects.
class Person:

    # Class variable, shared by all instances of the class.
    species = "H. Sapiens" 

    # The __init__ method is called every time a new object is created. We use it to set some initial values for our object.
    # The self parameter is a reference to the new object being created.
    # We are then telling it we are going to pass in an argument of name and age.
    def __init__(self, name, age, clothes:list):
        # We then set the values of the instance variables with the arguments from __init__.
        self.name = name
        self.age = age
        self.clothes = clothes
    
    # This is a method. A method is a function that is part of a class.
    # Methods always receive self as the first argument.
    def sayHello(self):
        print("Hello my name is " + self.name)

    def outputClothes(self):
        # This will output the clothes the person has.
        if len(self.clothes) > 0:
            print("I have the following clothes:")
            for i in self.clothes:
                print(i)
        else:
            print("I have no clothes.")


# Define a subclass of Person, named Student.
class Student(Person):

    # The __init__ method is called every time a new object is created. We use it to set some initial values for our object.
    # The self parameter is a reference to the new object being created.
    # We are then telling it we are going to pass in an argument of name, age, school.
    def __init__(self, name, age, clothes, school):
        # We can the super() function to call the __init__ method of the parent class.
        # This allows us to pass in the arguments that are needed for the parent class.
        super().__init__(name, age, clothes)
        # Then we set the values of the other instance variables with the arguments from __init__.
        self.school = school
    
    # This methord overrides the one in the parent class.
    # This means if we call the sayHello method in the Student class, it will call this method instead of the one in the parent class (Person).
    def sayHello(self):
        print("Hello my name is " + self.name + " and I am a student at " + self.school)

    def saySimpleHello(self):
        # This calls the parent class method.
        super().sayHello()
    
    # We can also add new methord for just the child/subclass.
    def getYearGroup(self):
        # Returns the year group as a integer.
        return self.age - 5

# This Class is for Salaries
class Salary():

    def __init__(self, pay:int):
        self.salary = pay

    def getSalary(self):
        return self.salary
    
    def raiseSalary(self):
        self.salary = self.salary * 1.1

    # This is a static method. A static method is a method that does not require an instance of the class to be created. It is often used to create utility functions. They do not have self as the first argument.
    # In python we use the @staticmethod decorator to define a static method. This tells python not to pass self as the first argument to the method.
    @staticmethod
    def calculate_tax(salary:int):
        # This will calculate the tax on the salary.
        tax = salary * 0.2
        return tax




class Employee(Person):

    # A class variable, shared by all instances of the class.
    employed = True

    # The __init__ method is called every time a new object is created. We use it to set some initial values for our object.
    # The self parameter is a reference to the new object being created.
    # We are then telling it we are going to pass in an argument of name, age, salary.
    def __init__(self, name, age, clothes, initialSalary:int, job_title):
        # We can the super() function to call the __init__ method of the parent class.
        # This allows us to pass in the arguments that are needed for the parent class.
        super().__init__(name, age, clothes)
        # Then we set the values of the other instance variables with the arguments from __init__.
        self.position = job_title
        # Here we are setting the instance variable salary to and instance of the Salary class.
        # This is composition as the Salary instance will only exist as a part of the Employee Instance.
        self.salary = Salary(initialSalary)
    
    # This methord overrides the one in the parent class.
    # This means if we call the sayHello method in the Employee class, it will call this method instead of the one in the parent class (Person).
    def sayHello(self):
        print("Hello my name is " + self.name + " and I am an employee with a salary of " + str(self.salary.getSalary()) + " and a position of " + self.position)

    def saySimpleHello(self):
        # This calls the parent class method.
        super().sayHello()
    
    # We can also add new methord for just the child/subclass.
    def giveRaise(self):
        # This calls the Salary instance method raiseSalary.
        self.salary.raiseSalary()
        print("Raise given.")


class Clothes():

    def __init__(self, type_, size:str, colour:str):
        self.type_ = type_
        self.size = size
        self.colour = colour

    # By default every class has a method called __repr__ that returns a string representation of the object for when you print it out.
    # By overriding this we can change what happens when we try printing it.
    def __repr__(self) -> str:
        # This returns a string representation of the object.
        return "A " + self.type_ + " of size " + self.size + " and colour " + self.colour
            



# Here we initialize a new Person on object with the arguments of "John", 36 and [] for name and age, clothes.
person1 = Person("John", 36, [])
# This calls the sayHello method on the person1 object.
person1.sayHello()

# Here we initialize some clothes.
tie1 = Clothes("Tie", "M", "Red")
shirt1 = Clothes("Shirt", "L", "Blue")
trousers1 = Clothes("Trousers", "XL", "Black")
shoes1 = Clothes("Shoes", "7", "Brown")
# If we try to print a piece of clothing it will output the __repr__ method we defined.
print(tie1)

# Here we initialize a new Person on object and pass in a list of the clothes we have just created.
# This is a type of association between the Person and the Clothes class as the clothes exist separate from the Person and we are passing in a list of the clothes as a argument rather than deffining the clothes within the Pesron class.
person2 = Person("John", 36, [tie1, shirt1, trousers1, shoes1])
# This calls the sayHello method on the person2 object.
person2.sayHello()
# This calls the outputClothes method on the person2 object.
person2.outputClothes()


# Here we initialize a new Student on object with the arguments of "Jane", 25, [], and "Oxford" for name, age, clothes and school.
student1 = Student("Jane", 12, [], "Oxford")
# This calls the sayHello method on the student1 object.
student1.sayHello()
# This calls the saySimpleHello method on the student1 object.
student1.saySimpleHello()
# We print the result of the getYearGroup method.
print(student1.getYearGroup())


# Here we initialize a new Employee on object with the arguments of "Bob", 36, [], 10000 and "Manager" for name, age, clothes, salary and job_title.
employee1 = Employee("Bob", 36, [], 10000, "Manager")
# This calls the sayHello method on the employee1 object.
employee1.sayHello()
# This calls saySimpleHello method on the employee1 object.
employee1.saySimpleHello()
# This calls giveRaise method on the employee1 object. We should see their salary increase when we sayHello.
employee1.giveRaise()
# This calls the sayHello method on the employee1 object.
employee1.sayHello()

# We could call the static methord calculate_tax in two ways.
# The first way is to call the method directly on the class.
print(Salary.calculate_tax(employee1.salary.getSalary()))
# The second way is to call the method on the Salary instance.
print(employee1.salary.calculate_tax(employee1.salary.getSalary()))


