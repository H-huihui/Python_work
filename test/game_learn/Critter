#Critter Caretaker

class Critter(object):
    """A virtual pet"""
    def __init__(self,name,hunger=0,boredom=0):
        self.name=name
        self.hunger=hunger
        self.boredom=boredom

    def _pass_time(self):
        self.hunger=self.hunger+1
        self.boredom=self.boredom+1

    @property
    def mood(self):
        unhappiness=self.hunger+self.boredom
        if unhappiness<5:
            m="happy"
        elif 5<=unhappiness<=10:
            m="okay"
        elif 11<=unhappiness<=15:
            m="frustrated"
        else:
            m="mad"
        return m

    def talk(self):
        print "I'm",self.name,"and I feel",self.mood,"now.\n"
        self._pass_time()

    def eat(self,food=4):
        print("Brruppp. Thank you.")
        self.hunger=self.hunger-food
        if self.hunger<0:
            self.hunger=0
        self._pass_time()

    def play(self,fun=4):
        print("Wheee!")
        self.boredom=self.boredom-fun
        if self.boredom<0:
            self.boredom=0
        self._pass_time()

def main():
    crit_name=input("What do you want to name your critter?")
    crit = Critter(crit_name)

    choice = None
    while choice!="0":
        print \
        ("""
        Critter Caretaker

        0-Quit
        1-Listen to your critter
        2-Feed your critter
        3-Play with your critter

        """)

        choice= input("Choice: ")
        print ()

        #Quit
        if choice == "0":
            print ("Good-bye.")

        #Listen to your critter
        elif choice=="1":
                crit.talk()
        #Feed your critter
        elif choice=="2":
                crit.eat()
        #Play with your critter
        elif choice=="3":
                crit.play()
        else:
            print "\n Sorry,but",choice,"isn't a valid choices."

main()
("\n \n Press the enter key to exit.")
