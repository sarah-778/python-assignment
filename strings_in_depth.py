#1 array is also like alist
# examples
# marks=[90, 60,70]
# name = sarah
# [we use angle brackets whe dealing with array]
name = "sarah"
print(name[0])
print(name[4])


# type: ignore #looping through string
# we loopthrough strings using a keyword "for"
#example
for charactr in  name:
   print(charactr)

address="kamokya"
for item in address:
   print(item)


   #3.slicing in string
   #this is the accessing of a range of character 
   #example
   name="sarah"
print(name[1:3])#aa
print(name[1:4])#ah
print(name[  :3])#ra (when you dont have the start index, 

message="hello"
print(message[0:3])
print(message[-1])
print(message[-1:-5])
print(message[-1:-4])
print(message[-5:-3])
print(message[-4: ])#keep all the items after the start index
print(message[4: ])



#4. f strings
#they always work with the 
name= "ishameli"
age= "16"
weight=58.4356
print(f" my name is {name} and am {age} years old and weigh {weight:.2f}")
total_cost=300000
print(f"a new dress is sold at  {total_cost:,}")


#string method
#1. length #len
name = 'robert'
print(len(name))

adress='from kamokya'
print(len(adress))
# we also count spaces  left between the words
name= 'sarah\norishaba'
print(name)
print(name.upper)
#\n new line 
#\t   tab it leaves four spaces between the text.
name = 'pineapple'
print(name[4:9])








