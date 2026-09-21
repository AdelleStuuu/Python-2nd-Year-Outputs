class runner:
    def __init__(self,name = "",experience = 0,speed = 0,medal = 0): 
        self.name = name
        self.experience = experience
        self.speed = speed
        self.medal = medal

    def run(self,kilometer = 0):
        previousMedal = self.medal
        if kilometer < 10 or kilometer > 30:
            print("Invalid input, pick a number between 10 to 30.")
        else:
            print(f"{self.name} ran {kilometer} kilometers!")
            self.experience += kilometer
            self.medal = int(self.experience/100)
            if self.medal > previousMedal:
                self.speed *= 1.2
                print(f"+ 20% speed for {self.name}!")
                print(f"+ {self.medal - previousMedal} medal/s! for {self.name}!")

    def displayStat(self):
        print(f"Name: {self.name}")
        print(f"Experience: {self.experience}")
        print(f"Speed: {round(self.speed,2)}")
        print(f"Medal: {self.medal}")
        print()

run1 = runner("Adam", 0, 1, 0)
run2 = runner("Bob", 0, 1, 0)

run1.displayStat()
run2.displayStat()
run1.run(25)
run2.run(30)
run1.run(20)
run2.run(35)
run1.run(25)
run2.run(15)
run1.run(20)
run2.run(10)
run1.run(15)
run2.run(30)
run1.run(20)
run2.run(25)
print()
run1.displayStat()
run2.displayStat()
print("Created by Adelle")