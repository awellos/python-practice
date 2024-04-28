#string concatenation
print ("Enter your first name:")
fname = input()
print ("Enter your second nmae:")
sname = input()
print (fname +  " " + sname)

#age calculator
print("Enter your year of birth:")
birth_year = int(input())
age = 2024 - birth_year
print("You are ",age ,"years old")

#number comparison
print("Enter a number:")
num = input()
print("Enter another nunber:")
num3 = input()
if num == num3:
  print("True")
else:
 print("False")
  
#Length of String
print("Enter a sentence:")
sentence = input()
print(len(sentence))

#Simple Interest Calculator
print("Enter the principal amount:")
principal = int(input())
print("Enter rate:")
rate = float(input())
print("Enter time:")
time = int(input())
interest = (principal*rate*time)/100
print("The simple interest is",interest)

#Temprature converter
print("Enter the temprature in fahrenheit:")
temp = float(input())
celsius = (temp - 32)*5/9
print("The temperature in celsius is", celsius) 

#Multiplication table
print("Enter a number:")
num = int(input())
for i in range(1,11):
  print(num, "x", i, "=", num*i)