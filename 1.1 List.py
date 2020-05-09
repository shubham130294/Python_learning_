# List  []

Numbers = [1,2,3,4,5,6]
Characters = ["MONU","SAURABH","TanishQ"]
print(max(Numbers))
print(min(Characters))

list1 = [3.14,'SHUBHAM',13]
list2 = ['Monu','Saurabh','Tanisq']

List = [list1,list2]
print(List)

print("===============Operations on LIST===========")
List.extend([29,84])
print(List)
List.pop() # LIFO
print(List)
del List[1]
print(List)
#List.remove(3.14) # its not going to work becoz remove function works only for one element & here the first element itself is a list i.e containg different elements.

List[0] = 314
print("LIST is Muttable i.e. element can be modified ")
print(List)