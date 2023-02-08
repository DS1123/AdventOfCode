import numpy as np
# Read directions $R , R, U , D , L .. e.t.c ,$ in a list assume both HT start at origin
import csv

list1 = []

with open('Day9.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=" ")
    line_count = 0
    for row in csv_reader:
        list1.append(row)

directions = ["L","L"]
for i in range(1,len(list1)):
    for ii in range( int((list1[i])[1]) ):
        directions.append(list1[i][0])

size = len(directions)
HeadPos = np.array([0,0])
TailPos = np.array([0,0])
UniqueListTailPos = [TailPos.tolist()]
def DrawGrid(TailPos, HeadPos): 
    for j in range(-size , size +1 ,1  ):
        for jj in range(-size , size +1 , 1):
            CurPos = np.array([jj, - j ])
            if(np.array_equiv(CurPos, TailPos)):
                if(np.array_equiv(TailPos,HeadPos)):
                    print("B", end= "" )
                else:
                    print("T", end = "")
            elif(np.array_equiv(CurPos, HeadPos)):
                print("H", end = "")
            elif (jj == size  ):
                print(" \n")
            else:
                print("*", end = "")
    print("\n\n")            
#DrawGrid(TailPos,HeadPos)
for i in range(size): 
    if directions[i] == "R" :
        change = np.array([1,0])
    if directions[i] == "D" :
        change = np.array([0,-1])
    if directions[i] == "U":
        change = np.array([0,1])
    if directions[i] == "L":
        change = np.array([-1,0]) 
    
    HeadPos += change 
    dist2 = (HeadPos[0] - TailPos[0])**2 + (HeadPos[1] - TailPos[1])**2
    if (dist2 >= 4):
        # dist^2 \geq 4 means tails must move 
        TailPos = HeadPos - change
        if(not(TailPos.tolist() in UniqueListTailPos)):  
            UniqueListTailPos.append(TailPos.tolist()) 
 #   DrawGrid(TailPos,HeadPos)
print("Number of unique tiles visited by Tails is ", len(UniqueListTailPos)) 

