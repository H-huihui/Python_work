from project3 import *
from project4 import *
from project2 import *

#YOUR CODE GOES HERE

class Number(object):
    def __init__(self,color,type,width,height):
        self.color=color
        self.type=type
        self.width=width
        self.height=height    
    def match(self,grid):
        result=[]
        color="x"
        i=0
        type="one"
        result=[]
        while(i<len(grid)):
            j=0
            while(j<len(grid[i])):
                if(grid[i][j]!="_"):
                    result.append((i)*len(grid[i])+j+1)
                j=j+1
            i=i+1
        result.sort()

        self.width=len(grid[0])
        self.height=len(grid)
        
        temp1=create(len(grid[0]),len(grid),"one")

        temp2=create(len(grid[0]),len(grid),"two")

        temp3=create(len(grid[0]),len(grid),"three")

        temp4=create(len(grid[0]),len(grid),"four")

        temp5=create(len(grid[0]),len(grid),"five")
        
        if(result==temp1):
            
            self.type="one"
        elif(result==temp2):
            self.type="two"
        elif(result==temp3):
            self.type="three"
        elif(result==temp4):
            self.type="four"
        elif(result==temp5):
            self.type="five"
        else:
            self.type="EXCEPTION"
        
    def draw(self):
        result=""
        result=draw(self.width,self.height,self.color,self.type)
        return result
    
    def getSoften(self):
        Soften=False
        return Soften
    
    def getColor(self):
        return self.color
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getType(self):
        return self.type
    
    def to_string(self):
        
        return str(self.color+" "+self.type)
