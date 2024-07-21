class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        super().breathe()
        print("doing underwater")


neme = Animal()
neme.breathe()
my_fish = Fish()
my_fish.swim()
my_fish.breathe()