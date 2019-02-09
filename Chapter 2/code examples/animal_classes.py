'''
    An example of object modelling is the creation of animals.
    First we create a general template on which we base our other animals.

        class Animal:
            def __init(self):

    We can add attributes to our animal in the __init__ section.

        class Animal:
            def __init__(self, name, color, pattern):

    In order to retrieve the information we put in these attributes, we need to add the following below the __init__ section.

        class Animal:
            def __init__(self, name, color, pattern):
                self.name = name
                self.color = color
                self.pattern = pattern

    Now that we have created an Animal object we can begin to create our individual animals.
    We could create many animal objects to represent our menagerie, but a possible intermediate step would be to create a sub-class of the Animal.
    For instance, we could creat a cat based on our general animal by doing this:

        class Cat(Animal):

    This cat has all of the same attributes that our general animal does. We can also write funcitons to be only included for a specific sub-class:

        class Cat(Animal):
        def speak(self):
            print("Purr...")

    Likewise, we can create other animals in the same fashion:

        class Dog(Animal):
            def speak(self):
                print("Woof!")

        class Giraffe(Animal):
            def speak(self):
                print("...giraffe sounds?")

    Now that we have created the model of our animal objects, we can create specific animals with names, colors, and coat patterns.

        huckle = Cat('huckle', 'ginger', 'tabby')
        ginger = Dog('ginger', 'white and brown', 'spotted')
        spooks = Cat('spooks', 'grey', 'tabby')
        geoffrey = Giraffe('geoffrey', 'brown and yellow', 'spotted')

    And we can query these animals for certain information:

        print("Huckle is " + huckle.color)
        print("Spooks is a " + spooks.pattern)
        print("The dog's name is " + ginger.name)
        print("Geoffrey is " + geoffrey.color)
        huckle.speak()
        spooks.speak()
        ginger.speak()
        geoffrey.speak()
'''

class Animal:
    def __init__(self, name, color, pattern):
        self.name = name
        self.color = color
        self.pattern = pattern

class Cat(Animal):
    def speak(self):
        print("Purr...")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Giraffe(Animal):
    def speak(self):
        print("...giraffe sounds?")

huckle = Cat('huckle', 'ginger', 'tabby')
ginger = Dog('ginger', 'white and brown', 'spotted')
spooks = Cat('spooks', 'grey', 'tabby')
geoffrey = Giraffe('geoffrey', 'brown and yellow', 'spotted')

print("Huckle is " + huckle.color)
print("Spooks is a " + spooks.pattern)
print("The dog's name is " + ginger.name)
print("Geoffrey is " + geoffrey.color)
huckle.speak()
spooks.speak()
ginger.speak()
geoffrey.speak()
