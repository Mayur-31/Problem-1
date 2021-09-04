marks=[]
present=[]
absent=[]
n=0
def marksobtain():
    global n
    n=int(input("Enter number of students:\n"))
    print("consider absent student's score as 0")
    
    for i in range(1,n+1):
        print("Enter marks of students",i,":")
        s=int(input())
        marks.append(s)
        if(s>0):
            present.append(s)
        else:
            absent.append(s)
            print("marks of students:",marks)    
    
    # Function for average
def average():
    p=0
    for i in present:
        p=p+i
    average=p/(len(present))
    print("average marks of class is:",average)

# Function for highest and lowest marks
def high_low():
    print("Highest marks in class:",max(present))
    print("Lowest marks in class:",min(present))
   
# Function for absent students 
def absent_length():
    print("count of students who are absent for the test:",len(absent))
    
# Function for number with highest frequency
def frequency():
    print("marks with highest frequency count:",max(set(present),key=present.count))
 
marksobtain()
average()
high_low()
absent_length()
frequency()            
    
    
                    
        
