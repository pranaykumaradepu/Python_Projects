# Animal sound simulator

class Animal:
    def make_sound(self):
        print("Generic animal sound")


class Dog(Animal):
    def make_sound(self):
        print('The dog barks')

class Cat(Animal):
    def make_sound(self):
        print('The cat Meow!')

class Duck(Animal):
    def make_sound(self):
        print('The duck Quack!')


# simulator class
class AnimalSimulator:
    def __init__(self):
        self.animals = []

    def add_animal(self,animal):
        if isinstance(animal,Animal):
            self.animals.append(animal)
            print(f'{animal.__class__.__name__} added to the simulator')
        else:
            print('Invalid animal type')
        
    def make_all_sound(self):
        if not self.animals:
            print('No animas in simulator')
        else:
            print('\n--- Animal Sound ---')
            for animal in self.animals:
                animal.make_sound()
# main program

simulator = AnimalSimulator()

while True:
    print('\n--- Animal Sounnd Simulator ---')
    print('1. Add Dog')
    print('2. Add Cat')
    print('3. Add Duck')
    print('4. Add make all sound')
    print('5. Exit')

    choice = int(input('eneter your choice : '))

    if choice == 1:
        simulator.add_animal(Dog())
    elif choice == 2:
        simulator.add_animal(Cat())
    elif choice == 3:
        simulator.add_animal(Duck())
    elif choice == 4:
        simulator.make_all_sound()
    elif choice == 5:
        break
    else:
        print('Wrong input')
