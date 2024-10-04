class Cat:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("meow")

class Dog:
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Woof")

cat1 = Cat("Kitty", 4)
dog1 = Dog("Clifford", 12)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()