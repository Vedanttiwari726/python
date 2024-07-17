F=input("Enter your first name:")
M=input("enter your middle name:")
L=input("enter your last name:")
Fullname=" ".join([F,M,L])
print(Fullname)
Email=input("enter your email id:")
if Email.endswith("org,com,in,edu"):
    print("valid email id:")
else:
    print("invalid email id:")
F=F.lower()
a=F[0:4]
DOB=input("DD MM YY:")
b=DOB[0:4]
password=a+b
print(password)


