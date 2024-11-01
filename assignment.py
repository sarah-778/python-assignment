# 1. write a programe that checks if a given number is between 10 and 20 (20 iclusive) use logical operators.
number= int(input("enter the number: "))
if 10 <number <= 20:
    print(f" {number} is between 10 and 20 (20 inclusive)")
else: 
    print(f" {number} is not between 10 and 20 (20 inclusive)")    

    # 2. write aprogram that prints the square of all integers from one to ten using the for loop
integers = [1,2,3,4,5,6,7,8,9,10]
for x in integers:
        x= x*x
        print(x)
    # 3. write a simple program that asks a user for their age
    # if the user greater or equal to 18 print "adult,you are not qualified your qualified" else print your not qualified
age = int(input('enter your age'))
if age >= 18:
     print("adult, you are qualified")
else:
     print("you are not qualified")
     
     #. 4 we have the following student detail and marks, enter these details from the key board
     # student name= ritah liz
     # student number = SEP23/BCS/14
     # programming = 78
     # data science = 89
     # computer application = 55
      # culculate the average mark and print the answerin three dps
student_name = 'ritah liz'
student_number = 'SEP23/BCS/14'
programming = 78
data_science = 89
computer_application = 55
total_sum = programming + data_science +computer_application
number =3
average = total_sum /number
print(f" the total_sum is {total_sum}")
print(f" the average is {average}")
# 5 write thea programe thatconverts degrees celicious to franhigt, the programe 
# should ask the user to enter the temperature in gegrees celicoius and display the temperature to gerees frahanght
temperature_celicious = float(input("Enter the temperature in °C"))
temperature_faranhight =(9/5*temperature_celicious) 
print(f"the temperature in faranhight °F is :{temperature_faranhight:.3f}")



# 6. A car miles per gallatons can be calculated with the following  formula .
#  Write the programe that asks the user for the number of miles driven and gallons used
#  it should culculate the car's miles and display the results 
#  MPG = miles Driven/Gallons of car used.
miles_driven = float(input("Enter the miles_driven"))
gallons = float(input("gallons"))
mpg = miles_driven/gallons
print(f"the miles per gallons used are:{mpg:.2f}")









     
     
     

