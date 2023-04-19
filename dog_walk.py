class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        print(f"{self.name} is barking!")
    
    def fetch(self, item):
        print(f"{self.name} is fetching the {item}!")
    
    def walk(self):
        print(f"{self.name} is walking with you!")
        self.bark()
    
    def stop(self):
        print(f"{self.name} has stopped walking!")
    
    def run(self):
        print(f"{self.name} is running with you!")
        self.bark()


dog_name = input("What is your dog's name? ")
dog_breed = input("What is your dog's breed? ")
dog_age = int(input("What is your dog's age? "))

my_dog = Dog(dog_name, dog_breed, dog_age
