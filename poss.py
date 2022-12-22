import scipy
from scipy import *

class poss():
    def __init__(self,pos):
        self.pos =pos
    def __str__(self):
        # Fill this in
        return f"{self.pos}"

    def countPointsNCP(self,x):
        total =0
        for i in range(0, len(self.pos)):
            if(i == "1") :total==100
            if(i=="2"): total+=100*(1-x)-50*x
            if(i == "3"):  total+= 75
        return total    
            

    def countPointsCP(self):
        total =0
        for i in range(0, len(self.pos)):
            if(i=="2"): total+=100
            if(i == "3"):  total+= 100
            
        return total

         
            
    def countOccurance(self,num):
        ctr =0
        for i in range(0, len(self.pos)):
            if i ==num:
                ctr+=1
        return ctr  

    def risk(self,x):
        dup = self.countOccurance(2)
        return scipy.stats.binom.pmf(dup, dup, x)          

    def riskNCP(self):
        return self.risk(3)

    def riskCP(self):
        return self.risk(2)    
   
    def replaceLowestValue(self):
        lowestval = ""
        charArr = [char for char in self.pos]
        intArr = list(map(int,charArr))
        intArr.sort()
        intArr[len(intArr)-1] =1 
        charArr = list(map(str,intArr))
        str1 =""
        return str1.join(charArr)



    def weightedAvg(self):
        ctr0= self.countOccurance(0)
        ctr1 =self.countOccurance(1)
        ctr2=self.countOccurance(2)
        ctr3=self.countOccurance(3)
        ctr4=self.countOccurance(4)

        return (0.2^ctr0) * (0.2^ctr1)* (0.2^ctr2)* (0.2^ctr3)* (0.2^ctr4)


    def sum(self):
        #return self.countPointsCP()*self.weightedAvg()/
        pass
