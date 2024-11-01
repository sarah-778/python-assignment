 # comparison operators
 # example:
 # allow you to compare two values and return a bloolean value (true or false)
 # examples:
a = 80
b = 70
c = 80
result_one = a==b
print(result_one)
result_two = a!=b
print(result_two)
result_three = a==c
print(result_three)
#2 longin syestem
username = "sarah"
password = "sarah256"
inputed_username = input("enter your name")
inputed_password = input("enter your password")

# validate login credentials
if inputed_username == username and inputed_password ==password:
    print('login was successfull')
else:
    print("login failed")