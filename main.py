import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.mood = 20
        self.cleanness = 20
        self.hunger = 10
        self.love = 0
        self.alive = True

    def to_play(self):
        print("Time to play!")
        self.mood += 5
        self.love += 0.5
        self.hunger -= 5
        self.cleanness -= 5

    def to_wash(self):
        print("Time to wash!")
        self.mood -= 1
        self.love += 0.5
        self.cleanness += 20

    def to_sleep(self):
        print("Time to sleep!")
        self.mood += 20
    def to_eat(self):
        print("Time to eat!")
        self.mood += 20
        self.love += 0.5
        self.hunger += 10
        self.cleanness -= 5

    def is_alive(self):
        if self.mood < 0:
                print(":(")
                self.alive = False
        elif self.love > 0:
                print(":)")
                self.alive = False
    def end_of_day(self):
        print(f"Mood: {self.mood}")
        print(f"Cleanness: {self.cleanness}")
        print(f"Hunger: {self.hunger}")
        print(f"Love: {self.love}")
    def live(self, day):
        d = f"Day {day} of {self.name}'s life"
        print(f"{d:=^50}")
        live_cube = random.randint(1,4)
        if live_cube == 1:
            self.to_wash()
        elif live_cube == 2:
            self.to_eat()
        elif live_cube == 3:
            self.to_play()
        elif live_cube == 4:
            self.to_sleep()
        self.end_of_day()
        self.is_alive()

nick = Cat("Kitty")
for day in range(1, 366):
    nick.live(day)