class Friend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"Hey, I'm {self.name}!")

    def print_age(self):
        print(f"I am {self.age} years old.")


f = Friend("Myles", 20)

f.intro()
f.print_age()
