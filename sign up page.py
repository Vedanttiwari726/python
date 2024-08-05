def get_user_info():
    Fname=input("enter your first name:")
    Lname=input("enter your last name:")

#email id vaildation part
    Email_id=input("enter your email id:")
    if Email_id.endswith("@gmail.com"):
      print(Email_id)
    else:
      print("invalid email_id:")      
#pincode validation
    Pincode=(input("enter five digit pincode: "))
    if len(Pincode)== 5 and Pincode.isnumeric():
       print(Pincode)
    else:
       print("invalid pincode !please check for pin")  
#mobile number validation
    Mobile_number=(input("enter ten digit Mobile_number: "))
    if len(Mobile_number)== 10 and Mobile_number.isnumeric():
       print(Mobile_number)
    else:
       print("invalid Mobile_number !please check once...")  
      
get_user_info()   

def validation():
   # creating username and password
     username=input("create your username:") 
     Password=input("create your Password:")

     valid_username="vedant07"
     valid_password="1734"

     if valid_username==username and valid_password==Password:
      print(username)
      print(Password)
     else:
        print("Invalid user_ID and Password.Access denied!") 

validation()
       







      

