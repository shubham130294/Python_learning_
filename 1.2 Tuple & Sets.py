#Tuple ()
#Tuple is the same as List , with only difference of () & that it is immutable .
# Since we dont change values in Tuple ,so iteration in Tuples is faster than in List .Enhance the speed of execution
Tuple =(1,2,3,4,45,'SHUBHAM',45,54,45,54,6,76,78)

# print(max(Tuple))   # Comparision is not supported between instances of 'str' and 'int'

print(Tuple.count(45))


#========================================================================================#
#Sets {}
#Set uses the concept of Hash to fetch the elements faster .
#So its not guranteed that you ll get the same sequence as you entered in Sets .
#Sets is mutually Exclusive
#Set does not support indexing

set1 ={23,4,55,67,89,97,90,89}
print(set1)
set1.remove(89)
print(set1)
set1.pop()
print(set1)
set1.pop()
print(set1)
