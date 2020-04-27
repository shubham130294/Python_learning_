# Data type declaration is not required ,On the value assignment the data type is decided dynamically #

print("SHUBHAM sharma`s Book")
print('SHUBHAM sharma\'s Book')  # \ is used as an escape character
print(r'C:\Users\SHUBHAM Sharma') # r is used to print raw string considering even back slashes
print("")

print("================VARIABLES===================")
num1,num2 = 7,4
result = num1+num2
print(result)

var1 = "SHUBHAM"   #ALL CAPITAL LETTERS
print(var1)
print("")           #Gives a Single new line

var1 += " sharma"   #ALL SMALL LETTERS
print(var1)
print("\n")         #Gives two new line ,one due to special character "\n"

print("***********  OPERATIONS ON VARIABLES  *************")
name = var1
print(name[0]) # This proves that string is a character array with lower bound as 0  -------->
print(len(name)) # len is a function to determine the length of the string
print(name[1:10]) # this will escape the 0th character i.e S and will print upto the length 10
print(name[-1])  #-1 reperesents the last character of the string <-------
print(name[-6:])  #print will always happen from ---->> till length


