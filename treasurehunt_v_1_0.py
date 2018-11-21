import os
import time
import random
#############################################################################################################################################################################################################   
def userScreen2(*args):
        count = 0
        userEntry = list(args)
        list1 =[]
        entry1 = random.randint(1,7)
        list1.append(entry1)
        while len(list1) < 2:
           print('Entering loop1')    
           entry2 = random.randint(1,7)
           if entry2 not in list1:
               list1.append(entry2)          
           else:
               entry2 = random.randint(1,7)
           
        while len(list1) < 3:
           print('Entering loop2')
           entry3 = random.randint(1,7) 
           if entry3 not in list1:
              list1.append(entry3)
           else:
              entry3 = random.randint(1,7)            

        
	print('DEBUG userEntry {}'.format(userEntry))
        randGates = [entry1,entry2,entry3] 
        print("DEBUG randGates {}".format(randGates))

        userScreenPrint(entry1,entry2,entry3)  

        intList = list(set(randGates)& set(userEntry))
        print('intList {}'.format(intList))  
        print('length intList {}'.format(len(intList)))     
        if len(intList) >= 1:
           print('Better luck next time, you need to get all the gates right ')    
        else:
           print('Congratulations! you got the treasure')    
#############################################################################################################################################################################################################
def userScreenPrint(*args):
                   
        gate1 = "Gate1"
	gate2 = "Gate2"
	gate3 = "Gate3"
        gate4 = "Gate4"   
      	gate5 = "Gate5"   
        gate6 = "Gate6"   
        gate7 = "Gate7"   
	os.system("clear")
	gatesList = list(args)
        print('DEBUG::gatesList {}'.format(gatesList)) 
	print('\t\t\t\t\t\t\t\t\tTreasure\n') 
     
	for item in gatesList:
           if item == 1:
	   	   gate1 = 'Gate1-Guarded'
	 
	   elif item == 2:
	   	   gate2 = 'Gate2-Guarded'
	   	 
           elif item == 3:
	   	   gate3 = 'Gate3-Guarded'
      
           elif item == 4:
	   	   gate4 = 'Gate4-Guarded'
             
	   elif item == 5:
	   	   gate5 = 'Gate5-Guarded'
           elif item == 6:
	   	   gate6 = 'Gate6-Guarded'
           elif item == 7:
	   	   gate7 = 'Gate7-Guarded'
     	   else:
	 	  print('test') 
              
        gates = gate1+'\t\t'+gate2+'\t\t'+gate3+'\t\t'+gate4+'\t\t'+gate5+'\t\t'+gate6+'\t\t'+gate7
        print(gates)
        print('\n')         
        

#############################################################################################################################################################################################################
list1 =[]
entry1 = random.randint(1,7)
list1.append(entry1)
while len(list1) < 3:
     print('Entering loop1')    
     entry2 = random.randint(1,7)
     if entry2 not in list1:
           list1.append(entry2)          
     else:
           entry2 = random.randint(1,7)
           
while len(list1) < 4:
     print('Entering loop2')
     entry3 = random.randint(1,7) 
     if entry3 not in list1:
        
           list1.append(entry3)
     else:
           entry3 = random.randint(1,7)      

userScreenPrint(entry1,entry2,entry3)            
ele1 = int(input('Choice1 !\n'))
ele2 = int(input('Choice2 !\n'))
ele3 = int(input('Choice3 !\n'))  
userScreen2(ele1,ele2,ele3)     

