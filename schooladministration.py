import csv


def writeinfo(info_list):
    csvfile=open('student_info.csv', 'a',newline='')
    writer = csv.writer(csvfile)
    if csvfile.tell()==0:
        writer.writerow(["Name","Age","contact number","Email"])
    writer.writerow(info_list)
    


def put():
    stu=input("enter the details of the number {0}".format(num))
    return stu

    
num=1

while True:
    print("enter you choice\n1.Enter details\n2.To Print\n3.Exit")
    ch=int(input())
    if ch==1:
        stud=put()
        stud_list=stud.split(' ')
        print("\nThe entered information is -\nName: {}\nAge: {}\nContact_number: {}\nEmail ID: {}"
            .format(stud_list[0], stud_list[1], stud_list[2], stud_list[3] ))
        check=input("IS the entered details correct:Yes or No")
        if check=="Yes":
            writeinfo(stud_list)
            num+=1
        else:
            print("enter the correct info")
            stud=put()
            writeinfo(stuld_list)
            num+=1
    elif ch==2:
        print("The details are:")
        csvfile=open('student_info.csv', 'r')
        print(csvfile.read()) 
    else :
        break
            
