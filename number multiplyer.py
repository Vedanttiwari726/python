j=int(input('enter the number:'))
for i in range(1,13):
    print(j,"X",i,"=",i*j)

#print a table based on number given by the user but less than 10.

j=int(input('enter the number:'))
for i in range(1,13):
    if(j<=10):
            print(j,"X",i,"=",i*j)
    else:
         print("you entered invaild number")

