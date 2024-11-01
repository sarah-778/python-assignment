# #OPERATOR PRECEDENCE, Control flow structures,conditional statement, loops
# #defn this describes the order in which operation are performed in an expression,
# #  operators with higher precidence are always executed first

results = 3*4+5
print(results)

result1 = 3*4+5-1
print(result1)

result2 = 3*(4+5)-1
print(result2)

result3 = 3*(4+5)/1
print(result3)

#what would be the out put of the following expresson 
result_five = 5*3**2
print(result_five)
result_six =(5+3)*2**2-10/2
print(result_six)
result_seven = (25/5)+2*1
print(result_seven)


# CONTROL FLOW STRUCTURES.


#these are programs tha bases on a particular condition eg if else


#create a progragram that asks the user to for the food type bought in the market
# the program should print you boughbt chicken if the user enters chicken, liver if the user enters liver or you bought fish  

food_type = input("Enter the food type bought" )
if food_type =="chicken":
  print("you bought chicken ") 
if food_type != "chicken" or food_type != 'fish'or food_type != "liver":
  print('please select from chicken ,liver; fish')

   