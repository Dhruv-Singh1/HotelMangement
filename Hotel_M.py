import random
import time
import datetime
import  csv
#csvf= open('gdata.csv','r')
#read = csv.reader(csvf)
class  guest :

    @staticmethod
    def roomlist ():
        rooms = [range(1, 100)]
        r= random.sample(range(1,100),k=1)
        return r

    def __init__(self,name ,mail,num):
        self.name = name
        self.mail = mail
        self.num = num
        self.mem = " NONE"
        self.intime = 0
        self.outime =0
        self.visit = 0
        self.L_bill = 0
        self.bill = 0
    @classmethod
    def fullD(cls,name,mail,num,mem,intt,out,visit,bill):
        cls.name = name
        cls.mail = mail
        cls.num = num
        cls.mem = mem
        cls.intime = intt
        cls.outime = out
        cls.visit = visit
        cls.L_bill = bill

    def checkin(self):
        self.r = self.roomlist()
        self.C_in = True
        self.intime= time.time()
        print("Hello "+self.name+"!! your Room No. is : "+str(self.r)+"  have a nice stay ")
        a.add(g1)

    def checkout(self):
        print("1. Use current check out time \n 2. Enter Check out time Manually ")
        z=int(input("Enter Choice : "))
        if z == 1 :
            self.outime = time.time()
            print('success')

        elif z == 2  :
            t=input("Enter complete date time in format yyyy-mm-dd-hh-mm-ss :" )
            t= t.split('-')
            self.outime= datetime.datetime(int(t[0]),int(t[1]),int(t[2]),int(t[3]),int(t[4]),0,0).timestamp()
        t=round((self.outime - self.intime)/3600)
        charges = t*150
        self.bill=charges
        self.visit =self.visit+1
        print(self.name+" your Bill is "+str(charges)+" Rs for a stay of "+ str(t) +"hours" )
        write.writerow([self.name,self.mail,self.num,self.mem,self.intime,self.outime,self.visit,self.bill])

        a.L.remove(self)
        input("Press key to continue ")
    def disp(self):
        print('Name: ' +self.name+'\tEmail : '+ self.mail+ '\tMobile No. : '  + str(self.num) + '\tRoom No. : ' + str(self.r))
        if(self.mem==1) :print("Membership : Platinium")
        elif (self.mem == 2): print("Membership : Gold")
        elif (self.mem == 3) :print("Membership : Silver")
        else : print("Membership : NONE")
        
class Glist(object) :
    def __init__(self):
        self.L = []
       # for l in read :
        #    n=int(l[2])
            #s =guest.__init__(l[0],l[1],n)
         #   self.L.append(s)
          #  print(l)

    def add(self,g):
        self.L.append(g)
    def show(self):
        for i in range(len(self.L)) :
            self.L[i].disp()

    def searchN(self,room):
        i=0
        for i in range(len(self.L)):
            if str(self.L[i].r) == str('['+str(room)+']'):
                self.L[i].disp()
                return self.L[i]
                break
        return 'NULL'
    def search(self,namee):
        i=0
        for i in range(len(self.L)):
            if self.L[i].name == namee:
                self.L[i].disp()
                return self.L[i]
                break
        return 'NULL'
a = Glist()
csvf= open('gdata.csv','w')
write = csv.writer(csvf)


ch=1
print("\t\t\tWelcome to the Hotel Royal INN ")
while ch != 7 :
 print('\n\nHow may I Help You\n1.Check IN\n2.Check OUT\n3. See Guest List\n4. Modify Guest Data'
       '\n5. Rates\n6.Perks of Membership\n7. Exit ')
 ch = int(input("Enter Choice : "))

 if ch == 1 :
    print("Please Enter Your Details : ")
    namee =input("Enter Name :")
    mail = input("Enter E-Mail address:")
    num =int(input("Enter Mobile Number : "))
    g1 = guest(namee, mail,num)
    g1.checkin()

 elif ch == 2:
     c = int(input("Press 1. To enter Name of guest whose is checking out\n2.To enter room No of guest : "))

     if c==1 :
        namee=input("\n\n\nEnter Name :")
        o = a.search(namee)
        if o == 'NULL':
             print("Entry not found in list ")
        else:
            o.checkout()
     else :
         num = int(input("\n\n\nEnter Room No. :"))
         o = a.searchN(num)
         if o == 'NULL':
             print("Entry not found in list ")
         else:
             o.checkout()

 elif ch == 3:
    a.show()

 elif ch== 4:
    namee= input("Enter Name of Guest whose data is to be update : ")
    o= a.search(namee)
    if o == 'NULL' :
        print("Entry not found in list ")
    else :
        i=int(input("Choose among the following criteria to update :\n1.Name\n2.Email address\n3.Mobile Number\n4.Membership Status"))
        if i== 1:
            o.name=input(" Enter new Name ")
            print("The Updated data is :\n")
            o.disp()
        elif i== 2:
            o.mail=input(" Enter Email Address ")
            print("The Updated data is :\n")
            o.disp()
        elif i== 3:
            o.num=input(" Enter new Mobile Number ")
            print("The Updated data is :\n")
            o.disp()
        elif i== 4:
            o.mem=int(input(" Choose among the following Membership :\n1.Platinium\n2.Gold\n3.Silver"))
            print("The Updated data is :\n")
            o.disp()
 elif ch==5 :
     print("\n\nWe Charge :\n150Rs per Hour for Normal Days\n200Rs per hour for weekend days")

 elif ch==6 :
    print("\n\n\n\n\nPerks of our membership :\n\n\n1. Platinium :\n You get complementry Breakfast and Dinner acess "
     "to  Gym , Saloon ,swimming pool \n Shopping Vouchers,laundry service, high speed internet\n\n\n2.Gold :\nYou get"
    " complementry Breakfast,Gym,laundry service ,Shopping vouchers and high speed internet\n\n\n3.Silver :\nYou get"
    " access to gym ,laundry service and internet ")
 input("\n\n\nPress to continue ...")
