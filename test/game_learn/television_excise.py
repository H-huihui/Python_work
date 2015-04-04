#this is a television game

class Tele(object):
    def __init__(self,name,volumn=8,no=1):
        self.name=name
        self.no=no
        self.volumn=volumn

    def choose(self,no):
        self.no=no
        print "this is ",self.no," number television now\n"

    def volumnUp(self,num):
        self.volumn=self.volumn+num
        if self.volumn>40:
            self.volumn=40
        print "this is ",self.volumn,"now\n"

    def volumnDown(self,num):
        self.volumn=self.volumn-num
        if self.volumn<0:
            self.volumn=0
        print "this is ",self.volumn,"now\n"
        

def main():
    """ this is test"""
    tele_name=input("What do you want to name your tele?\n")
    tele=Tele(tele_name)

    choice=None
    while choice!=0:
        
        print \
        ("""
         Tele choose

         0-Quit
         1-Choose the Television
         2-volumn Up
         3-volumn Down

         """)
        
        choice=input("Choices:")
        print()
         

        if choice==0:    
            print ("good-bye")
         
        elif choice==1:
            
            no=input("please enter your tele no\n")
            tele.choose(no)
        elif choice==2:
            volumn=input("please enter your tele volumn\n")
            tele.volumnUp(volumn)

        elif choice==3:
            volumn=input("please enter your tele volumn\n")
            tele.volumnDown(volumn)

        else:
            print "\n Sorry ,but",choice,"isn't a valid choices."
            
main()
("\n\n Press the enter key to exit.")
