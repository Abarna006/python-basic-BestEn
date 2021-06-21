# merging two dictionary
from typing import Dict, List, Any, Counter

a = {1: "ab", 2: "bc", 3: "cd"}
b = {4: "de", 5: "ef"}
c = {**a, **b}
print(c)
# sorting the list in ascending order
lis = [8, 2, 5, 7, 1, 9]
lis.sort()
print(lis)
# after sorting converting it into set
lis = set(lis)
print(lis)
#with and without function
dict1 = {"bvi": [4, 7, 6], "avi": [1, 3, 2], "cvi": [23, 41, 20]}
result = {k: sorted(dict1[k]) for k in sorted(dict1)}
print(result)
#Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.
user=input("Enter the string :")
word="String given by user! "
print(user+word[6:])
print(word.replace('String',user))
#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter.
user = input("Enter the string :")
print(user.capitalize())
#Write a Python program to find the repeated items of a list
L1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
d = L1
print(d)
new_list = list([item for item in d if d[item] > 1])
print(new_list)
#Write a Python program to check the sum of three elements and divided by a value which is given as an input by the user
a=int(input("Enter number :"))
b=int(input("Enter number :"))
c=int(input("Enter number :"))
sum=a+b+c
print("Sum is: ",sum)
user=int(input("Enter the number to divide sum!"))
if sum% user==0:
    print("The given input divide")
else :
    print("The given input does not divide sum1")
#Write a Python program to find the Mean,median,mode among three given numbers
given_numbers = [1,2,2]
addition = 0
for i in given_numbers:
    addition = addition +i
print("addition",addition)
length = len(given_numbers)
mean = addition/length
print("mean :",mean)

given_numbers.sort()
if length%2==0:
    median1 = given_numbers[length//2]
    median2=given_numbers[length//2-1]
    median = (median1+median2)/2
else:
    median = given_numbers[length//2]
print("median is:",median)
import statistics
mode1=statistics.mode(given_numbers)
print("mode is :",mode1)
#Write a Python program to swap cases of a given string
a="Abi"
b="Hello"
tep=a
a=b
b=tep
print(a,b)
#Write a program to convert an integer to binary & octa decimal
x = 2
oct(x)
print(x)
y = 4
bin(y)
print(y)