#Project 4: RANDOM PASSWORD GENERATOR

#Create a program that takes the length of the password as input and generates a random password of the same length.
#  The strength of the password depends equally on the 4 properties mentioned below. 
# If the password generated randomly following the rules or constraints given below,
#  then that password is treated as good in terms of strength and accepted otherwise ignore that password.
#The properties to be followed for a strong password are:
#•	At least 12 characters.
#•	A mixture of both uppercase and lowercase letters.
#•	A mixture of letters and numbers. 
#•	Inclusion of at least one special character, e.g., @ #?]
#Note: do not use < or > in your password, as both can cause problems in Web browsers.
#(Student is free to decide the input and output layout for this mini project)



import random

name=input("Enter a name that you want to give to the password: ")
length=int(input("Enter the length of the password you want: "))
log1=input("Do you want to generate a file which store the password(y/n): ")

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."

mix_str = lower + upper + numbers + symbols

password = "".join(random.sample(mix_str,length))

def password_gen():
    print("Generating random password for you ...")
    print("The random password for",name, "is",password)

def log():
    f=open('logs.txt','a')
    f.write("\n")
    f.write("PASSWORD LIST")
    f.write("\n")
    f.write("Password for: ")
    f.write(name)
    f.write("\n")
    f.write("Password Length: ")
    f.write(str(length))
    f.write("\n")
    f.write("Password is: ")
    f.write(password)
    f.close


if log1=="y":
    log()
    password_gen()
elif log1=="n":
    print("The random password has been generated without the without the log file")
    password_gen()
else:
    print("Please Enter a valid response")  