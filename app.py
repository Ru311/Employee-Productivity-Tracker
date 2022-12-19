import pickle
import os
import pathlib
class Employee :
    
    name = ''
    expFrequency=0
    task = ''
    actFrequency=0
    productivity=0
    date=0
    
    def newEmployee(self):        
        self.name = input("Enter the employee name : ")
        self.task = input("Enter the type of task : ")
        self.expFrequency = int(input("Enter The frequncy of task expected :"))
        print("\nEmployee Registered\n")
    
    def taskUpdate(self):
        print("Employee Name : ",self.name)
        print("Task : ",self.task)
        self.actFrequency = int(input("Enter The Task Done : "))

    def empProd(self):
        self.productivity=self.actFrequency/self.expFrequency*100
   
    def modifyTask(self):
        print("Employee Name : ",self.name)
        self.task = input("Modify type of Task :")
        self.expFrequency = int(input("Modify expected frequency :"))
    
    def report(self):
        print(self.name, " ",self.productivity)
    
    def getexpFrequency(self):
        return self.expFrequency
    def getactFrequency(self):
        return self.actFrequency
    def getname(self):
        return self.name
    def gettask(self):
        return self.task
    def getproductivity(self):
        return self.productivity
    

def intro():
    
    print("\t\t\t\t\t\t\tEmployee Productivity Tracker")
    

    print("\n\n\t\t\t\t\t\t\tBrought To You By:")
    print("\t\t\t\t\t\t\tRucha Vaikar")
    print("\t\t\t\t\t\t\tBhargavee Nemade")
    input()


def newemp():
    employee = Employee()
    employee.newEmployee()
    newempsFile(employee)

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        for item in mylist :
            item.empProd()
            print("\nName: ",item.name,"\nTask: ", item.task, "\nProductivity: ",item.productivity)
        infile.close()
    else :
        print("\nNo records to display")
        

def displaySp(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.name == num :
                item.empProd()
                print("The productivity is = ",item.productivity)
                found = True
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this name")

def inputTask(num): 
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.name == num :
               item.taskUpdate()
               newempsFile(item)
               found = True
    else :
        print("No records to Search")
    if not found :
        print("No existing record with this name")
    


def newempsFile(account) : 
    
    file = pathlib.Path("accounts.data")
    if file.exists ():
        infile = open('accounts.data','rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else :
        oldlist = [account]
    outfile = open('newaccounts.data','wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')

# start of the program
ch=''
num=0
intro()
#system("cls");
print("\tMAIN MENU")
print("\t1. NEW EMPLOYEE")
print("\t2. TASK UPDATION")
print("\t3. PRODUCTIVITY EMPLOYEE")
print("\t4. PRODUCTIVITY OVERALL")
print("\t5. EXIT")
print("\n\tSelect Your Option (1-5) :")
ch = input()

while ch != 8:
    
    #system("cls");
    
    if ch == '1':
        newemp()
    elif ch =='2':
        num = input("Enter The Employee name. : ")
        inputTask(num)
    elif ch == '3':
        num = input("Enter The Employee name. : ")
        displaySp(num)
    elif ch == '4':
        displayAll();

    elif ch == '5':
        print("\tThanks for using our system")
        break
    else :
        print("Invalid choice")
    
    ch = input("\nEnter your choice : ")
    
 


    
    
    
    
    
    
    
    
    
    
