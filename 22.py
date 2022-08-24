"""
Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
"""

# def cift():
#     str = input("string gir :")
#     e = tuple(str)
#     z = []
#     i = 0
#     while i < len(e):
#         z.append(e[i])
#         i += 2
#     print(z)
# cift()

"""
Exercise 4: Remove first n characters from a string
Write a program to remove characters from a string starting 
from zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. 
Here we need to remove first four characters from a string.
remove_chars("pynative", 2) so output must be native. 
Here we need to remove first two characters from a string.
Note: n must be less than the length of the string.


"""

# def remove_chars():
#     a = input("string gir:")
#     x = list(a)
#     b = int(input("kaç harfi silinecek ?:"))
#
#     del x[0:b]
#
#     print("".join(x))
#
# remove_chars()

"""

Exercise 5: Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

Given:

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
Expected Output:

Given list: [10, 20, 30, 40, 10]
result is True

numbers_y = [75, 65, 35, 75, 30]
result is False

"""

# def isSame():
#     z = []
#     i = input("\n" + "sayı dizisini girin, girişi biritmek için q girin :")
#
#     while i != "q":
#         z.append(i)
#         print(z)
#         i = input("sayı dizisini girin :" + "\n")
#
#     if z[0] == z[-1]:
#         return print("ilk eleman :" + z[0] + "\n" + " son eleman : " + z[-1] + "   EŞİT" + "\n")
#     else:
#         return print("ilk eleman :" + z[0] + "\n" + " son eleman : " + z[-1] + " EŞİT DEĞİL!!!" + "\n")
#
#
# isSame()

"""

Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5

Expected Output:

Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55

"""

# def divisible():
#     given = [10, 20, 33, 46, 55]
#     z = []
#
#     for i in given:
#
#         if i % 5 == 0:
#             z.append(i)
#     print("\n Divisible by 5 : ")
#     print(z)
#
#
# divisible()

"""

Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.

Given:

str_x = "Emma is good developer. Emma is a writer"
Expected Output:

Emma appeared 2 times

"""
# çözülmedi

# x = input('Enter your sentence :')
# y = x.split()
# z = len(y)
# p = []
#
# i = 0
# while i <= z:
#     for j in y:
#         if j == y[j + 1]: p.append(j)
#     i += 1
#
# print(p)

"""

Exercise 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
Hint: Print Pattern using for loop

"""

# çözülmedi

# def ucgen():
#     j = int(input("Bir sayı gir :"))
#     i = 1
#     for i in range(1,j) :
#         print(i)
#         print("\n")
#         i+=1
#
#
# ucgen()

"""

Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

Expected Output:

original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number

"""
# tam çözülmedi

# def pandolin():
#     i = str(input("\nBir sayı gir:"))
#     z = list(i)
#     x=[]
#     x=z.sort()
#
#     print(x)
#     if z == x:
#         print(i + " bir pandolin sayıdır ")
#     else:
#         print(i + " bir pandolin sayı değildir! ")
#
#
# pandolin()

"""

Exercise 10: Create a new list from a two list using the following condition
Create a new list from a two list using the following condition

Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers 
from the first list and even numbers from the second list.

Given:

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
Expected Output:

result list: [25, 35, 40, 60, 90]

"""
# çözüldü
# def oddy():
#     list1 = [10, 20, 25, 30, 35]
#     list2 = [40, 45, 60, 75, 90]
#     z = []
#     i = 0
#     while i <= 4:
#         if list1[i] % 2 != 0 :
#             z.append(list1[i])
#         if list2[i] % 2 == 0 :
#             z.append(list2[i])
#
#         i += 1
#
#     print(z)
#
# oddy()

"""

Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

"""
# def reverse():
#     x=str(input("Bir sayı gir :"))
#     y=list(x)
#     print(y)
#     print(sorted(y,reverse=True))
#
# reverse()


"""

Exercise 12: Calculate income tax for the given income by adhering to the below rules
Taxable Income	Rate (in %)
First $10,000	    0
Next $10,000	    10
The remaining	    20
Expected Output:

For example, suppose the taxable income is 45000 the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000.

"""

# def income():
#     t = int(input('Whats your income $ :'))
#     x = int(t / 10000)
#     y = str(x)
#     print("Aşama Sayısı:" + y)
#
#     if t < 10000:
#         print("borcunuz :$0")
#     if 10000 <= t < 20000:
#         print("borcunuz :$1000")
#     if t > 20000:
#         z = str((x - 2) * 2000)
#         w = ((x - 2) * 2000) + 3000
#         q = str(w)
#         print("borcunuz :$1000 +$2000" + " +$" + z + "=" + "$" + q)
#
#
# income()

# if x==1 :
#     i=0
# elif x==2 :
#     tax2 = t*0.1
# elif x==3 :
#     tax3 =t*0.2+tax2+tax1

"""

Exercise 13: Print multiplication table form 1 to 10
Expected Output:

1  2 3 4 5 6 7 8 9 10 		
2  4 6 8 10 12 14 16 18 20 		
3  6 9 12 15 18 21 24 27 30 		
4  8 12 16 20 24 28 32 36 40 		
5  10 15 20 25 30 35 40 45 50 		
6  12 18 24 30 36 42 48 54 60 		
7  14 21 28 35 42 49 56 63 70 		
8  16 24 32 40 48 56 64 72 80 		
9  18 27 36 45 54 63 72 81 90 		
10 20 30 40 50 60 70 80 90 100 
See: How two use nested loops in Python


"""

# def carpimTablosu():
#     z = []
#     i = 1
#     j = 0
#     while i <= 10:
#         while j <= 9:
#             z.append(i * (j + 1))
#             j += 1
#         print(z)
#         z = []
#         j = 0
#         i += 1
#
#
# carpimTablosu()

"""

Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
* * * * *  
* * * *  
* * *  
* *  
*
Hint: Print Pattern using for loop

"""

# def yildiz():
#     i = 1
#     j = 9
#     while i <= 10:
#         while 0 < j <= 9:
#             print('*' * (j - 1))
#             j -= 1
#     i += 1
#
#
# yildiz()

"""

Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
Note here exp is a non-negative integer, and the base is an integer.

Case 1:

base = 2
exponent = 5

2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

Case 2:

base = 5
exponent = 4

5 raises to the power of 4 is: 625 
i.e. (5 *5 * 5 *5 = 625)


"""
# taban=int(input("taban gir:"))
# us = int(input("us gir :"))
#
# def usAlma(taban,us):
#     x=taban**us
#     print(x)
#
# usAlma(taban,us)

# ****************************INTERMEDIATE**********************

"""
Exercise 1: Reverse each word of a string
Given:

str = 'My Name is Jessa'
Expected Output

yM emaN si asseJ

"""

# Exercise to reverse each word  of a string

# çözemedim

# def reverse_words(Sentence):
#     # Split string on whitespace
#     words = Sentence.split(" ")
#     print(words)
#
#     # iterate list and reverse each word using ::-1
#     new_word_list = [word[::-1] for word in words]
#
#     print(new_word_list)
#
#     # Joining the new list of words
#     res_str = " ".join(new_word_list)
#     return res_str


# # Given String
# str1 = "My Name is Jessa"
# print(reverse_words(str1))


"""
Exercise 2: Read text file into a variable and replace all newlines with space
Given: Assume you have a following text file (sample.txt).

Line1
line2
line3
line4
line5
Expected Output:

Line1 line2 line3 line4 line5
"""
#
# f = open("1.txt","r")
#
# x= f.read()
# print(x)
# y=x.replace("\n","  ")
#
# print(y)

"""
Exercise 3: Remove items from a list while iterating
Description:

In this question, You need to remove items from a list while iterating but without creating a different copy of a list.

Remove numbers greater than 50

Given:

number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Expected Output: -

[10, 20, 30, 40, 50]

"""
""" Benim çözümüm"""
# number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# print(number_list)
# number_list.pop(5)
# number_list.pop(5)
# number_list.pop(5)
# number_list.pop(5)
# number_list.pop(5)
# print(number_list)

""" Pynative çözümü"""

# number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# i = 0
# # get list's size
# n = len(number_list)
# # iterate list till i is smaller than n
# while i < n:
#     # check if number is greater than 50
#     if number_list[i] > 50:
#         # delete current index from list
#         del number_list[i]
#         # reduce the list size
#         n = n - 1
#     else:
#         # move to next item
#         i = i + 1
# print(number_list)


"""
Exercise 4: Reverse Dictionary mapping
Given:

ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
Expected Output:

{65: 'A', 66: 'B', 67: 'C', 68: 'D'}
"""
# çözemedim

# ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
# # Reverse mapping
# new_dict = {value: key for key, value in ascii_dict.items()}
# print(new_dict)
"""
Exercise 5: Display all duplicate items from a list
Given:

sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
Expected Output: -

[20, 60, 30]
"""

# while i <= 8:
#     if sample_list[j] == sample_list[i + 1]:
#         z.append(sample_list[i])
#     else :
#         del sample_list[i]
#     i += 1
#
# i = 0


# /*****/ PYnative çöcümü

# import collections
#
# sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
#
# duplicates = []
# for item, count in collections.Counter(sample_list).items():
#     if count > 1:
#         duplicates.append(item)
# print(duplicates)

"""
Exercise 6: Filter dictionary to contain keys present in the given list
Given:

# Dictionary
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}

# Filter dict using following keys
l1 = ['A', 'C', 'F']
Expected Output: -

new dict {'A': 65, 'C': 67, 'F': 70}
"""

"""
Exercise 7: Print the following number pattern
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5

"""

# print("1"*5,end='  ')
# print("\n")
# print("2"*4,end=' ')
# print("\n")
#
# print("3"*3,end=' ')
# print("\n")
#
# print("4"*2,end=' ')
# print("\n")
#
# print("5"*1,end=' ')


"""
Exercise 8: Create an inner function
Question description: -

Create an outer function that will accept two strings, x and y. (x= 'Emma' and y = 'Kelly'.
Create an inner function inside an outer function that will concatenate x and y.
At last, an outer function will join the word 'developer' to it.
Expected Output: -

EmmaKellyDevelopers
"""

"""
Exercise 9: Modify the element of a nested list inside the following list
Change the element 35 to 3500

Given:

list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
Expected Output: -

[5, [10, 15, [20, 25, [30, 3500], 40], 45], 50]
"""
# list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
#
# x= list1[1]
# y=x[2]
# z=y[2]
#
# z[1] = 3500
#
# print(list1)


"""
Exercise 10: Access the nested key increment from the following dictionary
Given:

emp_dict = {
    "company": {
        "employee": {
            "name": "Jess",
            "payable": {
                "salary": 9000,
                "increment": 12
            }
        }
    }
}

"""
# emp_dict = {
#     "company": {
#         "employee": {
#             "name": "Jess",
#             "payable": {
#                 "salary": 9000,
#                 "increment": 12
#             }
#         }
#     }
# }
#
#
# # print(emp_dict['company']['employee']['payable']['increment'])
# emp_dict['company']['employee']['payable']['increment'] = 16
#
# print(emp_dict)

# /**************************************             LOOPS              *************************************************/


"""
Exercise 1: Print First 10 natural numbers using while loop
Help: while loop in Python

Expected output:

1
2
3
4
5
6
7
8
9
10
Show Solution

"""
# i=1
# while i<11 :
#     print(i)
#     i+=1


"""
Exercise 2: Print the following pattern
Write a program to print the following number pattern using a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
Refer:

Print Patterns In Python
Nested loops in Python
Show Hint
Show Solution

"""
# i = 1
# j = 1
# for j in range(j):
#     while j <= 5:
#         print(j)
#     j += 1

# print("Number Pattern ")
#
# # Decide the row count. (above pattern contains 5 rows)
# row = 5
# start: 1
# stop: row+1 (range never include stop number in result)
# step: 1
# run loop 5 times
# for i in range(1, row + 1, 1):
#     # Run inner loop i+1 times
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     # empty line after each row
#     print("")

"""
Exercise 3: Calculate the sum of all numbers from 1 to a given number
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

Expected Output:

Enter number 10
Sum is:  55
Refer:

Accept input from user in Python
Calculate sum and average in Python
Show Hint
Show Solution

"""

# x=int(input("Bir sayı gir:"))
# print()
#
# y = sum(range(1, x+1, 1))
#
# print(y)

"""

Exercise 4: Write a program to print multiplication table of a given number
For example, num = 2 so the output should be

2
4
6
8
10
12
14
16
18
20
Show Hint
Show Solution


"""
# x = int(input("Bir sayı gir:"))
#
#
# def katla(x):
#     return x + 2
# # print(2)
# # i = 1
# # while i <= 20:
# #     print(x*i)
# #     i+=2
# for i in range(2,22,2) :
#
#     print(i)

"""
Exercise 5: Display numbers from a list using loop
Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop
Given:

numbers = [12, 75, 150, 180, 145, 525, 50]
Expected output:

75
150
145
Refer: break and continue in Python

Show Hint
Show Solution
"""
# numbers = [12, 75, 150, 180, 145, 525, 50]
#
# z = []
# for i in numbers:
#     if i >= 150:
#         pass
#     elif i > 500:
#         break
#     else:
#         if i % 5 == 0:
#             z.append(i)
#
# print(*z)

"""
Exercise 6: Count the total number of digits in a number
Write a program to count the total number of digits in a number using a while loop.

For example, the number is 75869, so the output should be 5.

Show Hint
Show Solution

"""
# x = list(input("Bir sayı giriniz :"))
#
# # y= list(x)
#
# print("Girdiğiniz sayının basamak adedi : "+str(len(x)))

"""
Exercise 7: Print the following pattern
Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
Refer: Print patterns in Python

Show Hint
Show Solution

"""
# j = 6
# while j != 0:
#     for i in range(j-1, 0, -1):
#         print(i, end=' ')
#     print("\n")
#     j -= 1

"""
Exercise 8: Print list in reverse order using a loop
Given:

list1 = [10, 20, 30, 40, 50]
Expected output:

50
40
30
20
10
Show Hint
Show Solution

"""
# list1 = [10, 20, 30, 40, 50]
# z=[]
# i=4
# while i>=0 :
#     z.append(list1[i])
#     i-=1
#
# for i in z :
#     print
"""
Exercise 9: Display numbers from -10 to -1 using for loop
Expected output:

-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
See: Reverse range

Show Solution

"""
# i = -10
# while i <= -1:
#     print(i)
#     i += 1


"""

Exercise 10: Use else block to display a message “Done” after successful execution of for loop
For example, the following loop will execute without any error.

Given:

for i in range(5):
    print(i)
Expected output:

0
1
2
3
4
Done!
Show Hint
Show Solution


"""

# for i in range(5):
#     print(i)
# print("done!")

"""

Exercise 11: Write a program to display all prime numbers within a range
Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. 
A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers

Examples:

6 is not a prime mumber because it can be made by 2×3 = 6
37 is a prime number because no other whole numbers multiply together to make it.
Given:

# range
start = 25
end = 50
Expected output:

Prime numbers between 25 and 50 are:
29
31
37
41
43
47
Show Solution

"""
# start = 25
# end = 50
# z = list(range(25, 51))
# x=[]
# i = 0
#
# while i < len(z):
#     if z[i] % 2 == 0:
#         x.append(z[i])
#     elif z[i] % 3 == 0:
#         x.append(z[i])
#     elif z[i] % 4 == 0:
#         x.append(z[i])
#     elif z[i] % 5 == 0:
#         x.append(z[i])
#     elif z[i] % 7 == 0:
#         x.append(z[i])
#     else:
#         pass
#     i += 1
#
# difference = list(set(z) - set(x))
#
# print(*difference)

"""


Exercise 12: Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.

For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.

Expected output:

Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34
Show Hint
Show Solution

"""
# z=[]
# z.append(0)
# z.append(1)
# i=0
#
# while i<8 :
#     z.append(z[i]+z[i+1])
#     i+=1
#
# print(*z)

"""

Exercise 13: Find the factorial of a given number
Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5

5! = 5 × 4 × 3 × 2 × 1 = 120
Expected output:

120
Show Hint
Show Solution


"""
# import math
# x = int(input("Bir sayı gir :"))
#
# print("verilen sayının faktöryeli = "+ str(math.factorial(x)))


"""

Exercise 14: Reverse a given integer number
Given:

76542

Expected output:

24567

Show Solution
"""
# x= list(input("bir sayı gir : "))
#
# x.reverse()
#
# a_string = "".join(x)
#
# res = int(a_string)
#
#
# print(x)
# print(a_string)

"""


Exercise 15: Use a loop to display elements from a given list present at odd index positions
Given:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Note: list index always starts at 0

Expected output:

20 40 60 80 100
Show Hint
Show Solution

"""
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# z=[]
#
# i=1
# while i<=9 :
#     z.append(my_list[i])
#     i+=2
#
# print(*z)

"""
Exercise 18: Print the following pattern
Write a program to print the following start pattern using the for loop

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
Refer: Print Patterns In Python

Show Hint
Show Solution

"""
# i=1
# while i <=5 :
#     if i !=6 :
#         print("*" * i)
#     i += 1
#
# if i==6 :
#     j=4
#     while j > 0 :
#         print("*" * j)
#         j = j-1

"""

//////////////**** FUNCTION EXCERCISES *****//////////////



Exercise 2: Create a function with variable length of arguments
Write a program to create function func1() to accept a variable length of arguments and print their value.

Note: Create a function in such a way that we can pass any number of arguments to this function, and the function should process them and display each argument’s value.

Read: variable length of arguments in functions

Function call:

# call function with 3 arguments
func1(20, 40, 60)

# call function with 2 arguments
func1(80, 100)
Expected Output:

Printing values
20
40
60


Printing values
80
100

"""

# def func1(x, y, z):
#     return print(x, y, z)
#
#
# func1(20, 40, 60)
# func1(80, 100, 0)

"""




Exercise 4: Create a function with a default argument
Write a program to create a function show_employee() using the following conditions.

It should accept the employee’s name and salary and display both.
If the salary is missing in the function call then assign default value 9000 to salary
See: Default arguments in function

Given:

showEmployee("Ben", 12000)
showEmployee("Jessa")
Expected output:

Name: Ben salary: 12000
Name: Jessa salary: 9000
Show Hint
Show Solution


"""

# def showEmployee(name, salary=9000):
#
#         print("Name :" + name + " Salary :" + str(salary))
#
# showEmployee("Ben")
# showEmployee("Jessa", 12000)


"""

Exercise 5: Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it
Show Solution
"""

# def outer(a,b) :
#
#     def inner() :
#         return a+b
#
#     return print(inner()+5)
#
# outer(3,4)


"""

Exercise 6: Create a recursive function
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

A recursive function is a function that calls itself again and again.

Expected Output:

55

Show Solution

"""

# def addition(num):
#     if num:
#         # call same function by reducing number by 1
#         return num + addition(num - 1)
#     else:
#         return 0
#
# res = addition(10)
# print(res)

"""

Exercise 7: Assign a different name to function and call it through the new name
Below is the function display_student(name, age). Assign a new name show_tudent(name, age) to it and call it using the new name.

Given:

def display_student(name, age):
    print(name, age)

display_student("Emma", 26)
You should be able to call the same function using

show_student(name, age)
Show Hint
Show Solution

"""
# def display_student(name, age):
#     print(name, age)
#
# # call using original name
# display_student("Emma", 26)
#
# # assign new name
# showStudent = display_student
# # call using new name
# showStudent("Emma", 26)


"""

Exercise 8: Generate a Python list of all the even numbers between 4 to 30
Expected Output:

[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
Show Hint
Show Solution

"""
# print(list(range(4, 30, 2)))

"""

Exercise 9: Find the largest item from a given list
Expected Output:


"""

# x = [4, 6, 8, 24, 12, 2,89]
# print(max(x))

"""
//////////////////////////////////////**** Python Input and Output Exercise *****//////////////////////////////

Exercise 1: Accept numbers from a user
Write a program to accept two numbers from the user and calculate multiplication

Help: Take user input in Python


"""
# sayi1 = int(input("sayi1 gir :"))
# sayi2 = int(input("sayi2 gir :"))
#
# def mul(sayi1, sayi2):
#     print("\n")
#     print( sayi1 * sayi2)
#
# mul(sayi1, sayi2)

"""
Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.

Expected Output:

For example: print('Name', 'Is', 'James') will display Name**Is**James
"""

# print('Name'+"**" 'Is'+"**" 'James')

"""
Exercise 3: Convert Decimal number to octal using print() output formatting
Given:

num = 8
Expected Output:

The octal number of decimal number 8 is 10

"""
# ne diyor anlamadım
"""
Exercise 4: Display float number with 2 decimal places using print()
Given:

num = 458.541315
Expected Output:

458.54
"""
# num = 458.541315
# print('%.2f' % num)
"""
Exercise 5: Accept a list of 5 float numbers as an input from the user
Refer:

Take list as a input in Python.
Python list
Expected Output:

[78.6, 78.6, 85.3, 1.2, 3.5]

"""
# z=[]
#
# x=input("sayı giriniz: çıkmak için q ... ")
#
# while x !='q' :
#         z.append(x)
#         x=input("sayı giriniz: çıkmak için q ... ")
# print(*z)

"""

Exercise 6: Write all content of a given file into a new file by skipping line number 5
See:

Python file handling
Python Read file
Python write file
Create a test.txt file and add the below content to it.

Given test.txt file:

line1
line2
line3
line4
line5
line6
line7
Expected Output: new_file.txt

line1
line2
line3
line4
line6
line7
"""

# Ben yapmadım


# with open("test.txt", "r") as fp:
#     # read all lines from a file
#     lines = fp.readlines()
#
# # open new file in write mode
# with open("new_file.txt", "w") as fp:
#     count = 0
#     # iterate each lines from a test.txt
#     for line in lines:
#         # skip 5th lines
#         if count == 4:
#             count += 1
#             continue
#         else:
#             # write current line
#             fp.write(line)
#         # in each iteration reduce the count
#         count += 1


"""
Exercise 7: Accept any three string from one input() call
Write a program to take three names as input from a user in the single input() function call.

See: Get multiple inputs from a user in one line

Show Hint
Expected Output

Enter three string Emma Jessa Kelly
Name1: Emma
Name2: Jessa
Name3: Kelly
# """
# x= input("isimleri giriniz :")
#
# y=x.split()
# print(*y[0])
# print(*y[1])
# print(*y[2])

"""
Exercise 8: Format variables using a string.format() method.
Write a program to use string.format() method to format the following 
three variables as per the expected output

Given:

totalMoney = 1000
quantity = 3
price = 450
Expected Output:

I have 1000 dollars so I can buy 3 football for 450.00 dollars.
"""
# totalMoney = 1000
# quantity = 3
# price = 450
#
# x= "I have {} dollars so I can buy {} football for {:.2f} dollars."
# print(x.format(totalMoney,quantity,price))


"""
Exercise 9: Check file is empty or not
Write a program to check if the given file is empty or not

"""
# with open("new_file.txt", "r") as fp:
#     lines = fp.readlines()
#     z = list(lines)
#     if len(z) ==0 :
#         print("dosya boş")
#     else:
#         print("dosya dolu")
"""
Exercise 10: Read line number 4 from the following file
See:

Read Specific Lines From a File in Python
Python read file
Create a test.txt file and add the below content to it.

test.txt file:

line1
line2
line3
line4
line5
line6
line7

"""

# with open("test2.txt", "w") as fp:
#
#     i=1
#     while i<=7 :
#
#         fp.write("line"+str(i))
#         fp.write("\n")
#
#         i+=1

#
# //////////////////////////////////////**** String Excercises *****//////////////////////////////
"""
Exercise 1A: Create a string made of the first, middle and last character
Write a program to create a new string made of an input string’s first, middle, and last character.

Given:

str1 = "James"
Expected Output:

Jms
"""
# str1 = "James"
# z=list(str1)
# print(*z[0],z[2],z[4])

"""
Exercise 1B: Create a string made of the middle three characters
Write a program to create a new string made of the middle three characters of an input string.

Given:

Case 1

str1 = "JhonDipPeta"
Output

Dip
Case 2

str2 = "JaSonAy"
Output

Son

"""
# def get_middle_three_chars(str1):
#     print("Original String is", str1)
#
#     # first get middle index number
#     mi = int(len(str1) / 2)
#
#     # use string slicing to get result characters
#     res = str1[mi - 1:mi + 2]
#     print("Middle three chars are:", res)
#
# get_middle_three_chars("JhonDipPeta")
# get_middle_three_chars("JaSonAy")


"""


Exercise 2: Append new string in the middle of a given string
Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

Given:

s1 = "Ault"
s2 = "Kelly"
Expected Output:

AuKellylt

"""
# s1 = "Ault"
# s2 = "Kelly"
#
# mi = int(len(s1) / 2)
# print(mi)
#
# res = s1[mi:mi + 2]
#
#

"""
Exercise 3: Create a new string made of the first, middle, and last characters of each input string
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.

Given:

s1 = "America"
s2 = "Japan"
Expected Output:

AJrpan

"""

"""
Exercise 4: Arrange string characters such that lowercase letters should come first
Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

Given:

str1 = PyNaTive
Expected Output:

yaivePNT

"""
# str1 = "PyNaTive"
# z = list(str1)
# zup = []
# zlow = []
#
# i = 0
# while i < 8:
#     if z[i].isupper():
#         zup.append(z[i])
#     else:
#         zlow.append(z[i])
#     i += 1
#
# print(*zlow,*zup)

"""
Exercise 5: Count all letters, digits, and special symbols from a given string
Given:

str1 = "P@#yn26at^&i5ve"
Expected Outcome:

Total counts of chars, digits, and symbols 

Chars = 8 
Digits = 3 
Symbol = 4

"""
# str1 = "P@#yn26at^&i5ve"
# x = "<class 'str'>"
# y = "<class 'int'>"
# z=list(str1)
#
# char = 0
# digit = 0
# sym = 0
# i = 0
# while i < len(z):
#     if z[i].isalpha():
#         char += 1
#     elif z[i].isdigit():
#         digit += 1
#     else:
#         sym += 1
#
#     i += 1
#
# print(f"char : {char} , digit : {digit} Symbol : {sym}")

"""
Exercise 6: Create a mixed String using the following rules
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

Given:

s1 = "Abc"
s2 = "Xyz"
Expected Output:

AzbycX
"""
# s1 = "Abc"
# s2 = "Xyz"
# x = list(s1)
# y = list(s2)
# z = []
# i = 0
# while i <= 2:
#     z.append(x[i])
#     z.append(y[2-i])
#     i += 1
# print(*z)

"""
Exercise 7: String characters balance Test
Write a program to check if two strings are balanced.
 For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
 The character’s position doesn’t matter.

Given:

Case 1:

s1 = "Yn"
s2 = "PYnative"
Expected Output:

True
Case 2:

s1 = "Ynf"
s2 = "PYnative"
Expected Output:

False

"""
# s1 = "Yn"
# s2 = "PYnative"
# j = 0
#
# source = list(s1)
# target = list(s2)
#
# for i in source:
#     if i in target:
#         j += 1
#     else:
#         pass
#
# if j == len(s1):
#     print("True")
# else:
#     print("False")

"""
Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
Write a program to find all occurrences of “USA” in a given string ignoring the case.

Given:

str1 = "Welcome to USA. usa awesome, isn't it?"
Expected Outcome:

The USA count is: 2

"""
# str1 = "Welcome to USA. usa awesome, isn't it?"
# str2 = str1.upper()
#
# x=int(str2.count("USA"))
# print(x)

"""
Exercise 9: Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average of the digits that appear in the string,
 ignoring all other characters.

Given:

str1 = "PYnative29@#8496"
Expected Outcome:

Sum is: 38 Average is  6.333333333333333

"""
# str1 = "PYnative29@#8496"
# x=tuple(str1)
# z=0
# i=0
#
#
# while i < len(x):
#     if x[i].isdigit():
#         z+=int(x[i])
#
#     else:
#         pass
#
#     i += 1
#
#
# average=z/len(x)
#
# print(f"Sum is: {z} Average is  {average}")


"""
Exercise 10: Write a program to count occurrences of all characters within a string
Given:

str1 = "Apple"
Expected Outcome:

{'A': 1, 'p': 2, 'l': 1, 'e': 1}

"""
# str1 = "Apple"
# z = list(str1)
# y = {}
#
# for i in z:
#     x = int(str1.count(i))
#     y[i] = x
#
# print(y)

"""
Exercise 11: Reverse a given string
Given:

str1 = "PYnative"
Expected Output:

evitanYP

"""
# str1 = "PYnative"
# z=list(str1)
# print(*z[::-1])

"""
Exercise 12: Find the last position of a given substring
Write a program to find the last position of a substring “Emma” in a given string.

Given:

str1 = "Emma is a data scientist who knows Python. Emma works at google."
Expected Output:

Last occurrence of Emma starts at index 43

"""
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# print("Last occurrence of Emma starts at index",str1.rfind("Emma"))

"""
Exercise 13: Split a string on hyphens
Write a program to split a given string on hyphens and display each substring.

Given:

str1 = Emma-is-a-data-scientist
Expected Output:

Displaying each substring

Emma
is
a
data
scientist

"""
# str1 = "Emma-is-a-data-scientist"
# z=list(str1.split("-"))
# for i in z:
#     print(i)

"""
Exercise 14: Remove empty strings from a list of strings
Given:

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
Expected Output:

Original list of sting
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']

"""
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
#
# result = filter(lambda x: x != '' and x is not None, str_list)
# print(list(result))

"""
Exercise 15: Remove special symbols / punctuation from a string
Given:

str1 = "/*Jon is @developer & musician"
Expected Output:

"Jon is developer musician"

"""
# str1 = "/*Jon is @developer & musician"
# str2 = str1.split()
#
# new_string = ''.join(char for char in str2 if char.isalnum())
# print(new_string)


"""
Exercise 16: Removal all characters from a string except integers
Given:

str1 = 'I am 25 years and 10 months old'
Expected Output:

2510

"""
# str1 = 'I am 25 years and 10 months old'
# z=list(str1)
# x=[]
# for i in z :
#     if i.isdigit() :
#         x.append(i)
#
# print(*x)


"""
Exercise 17: Find words with both alphabets and numbers
Write a program to find words with both alphabets and numbers from an input string.

Given:

str1 = "Emma25 is Data scientist50 and AI Expert"
Expected Output:

Emma25
scientist50

"""
# str1 = "Emma25 is Data scientist50 and AI Expert"
# z=list(str1.split())
# y=[]
# for i in z :
#
#     if  i.isalpha() :
#         pass
#     else :
#         y.append(i)
# print(*y)


"""
Exercise 18: Replace each special symbol with # in the following string
Given:

str1 = '/*Jon is @developer & musician!!'
Expected Output:

##Jon is #developer # musician##

 
 """

# str1 = '/*Jon is @developer & musician!!'
# x = list(str1)
# i = 0
# while i < len(x):
#     if x[i].isalpha():
#         pass
#     elif x[i] == ' ':
#         pass
#     else:
#         x[i] = '#'
#     i += 1
#
# print(*x)

"""/**************Python Data Structure Exercise for Beginners***************************/"""

"""
Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list 
l1 and even index elements from the list l2.

Given:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
Expected Output:

Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]

Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
"""
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# z1=[]
# z2=[]
# z3=[]
#
# i=0
#
# while i<len(l1) :
#     if i%2!=0: #tekse
#         z1.append(l1[i])
#     else :
#         z2.append((l2[i]))
#     i+=1
#
# z3=z1+z2
# print("Element at odd-index positions from list one")
# print(z1)
# print(("Element at even-index positions from list two"))
# print(z2)
# print("Printing Final third list")
# print(z3)



"""
Exercise 2: Remove and add item in a list
Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

Given:

list1 = [54, 44, 27, 79, 91, 41]
Expected Output:

List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
"""




"""
Exercise 3: Slice list into 3 equal chunks and reverse each chunk
Given:

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
Expected Outcome:

Chunk  1 [11, 45, 8]
After reversing it  [8, 45, 11]
Chunk  2 [23, 14, 12]
After reversing it  [12, 14, 23]
Chunk  3 [78, 45, 89]
After reversing it  [89, 45, 78]
"""
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]


start = 0
end = 12
step = 3
for i in range(start, end, step):
    x = i
    print(sample_list[x:x+step])





"""
Exercise 4: Count the occurrence of each element from a list
Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.

Given:

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
Expected Output:

Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
"""




"""Exercise 5: Create a Python set such that it shows the element from both lists in a pair
Given:

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
Expected Output:

Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}
"""




"""
Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
See: Python Set

Given:

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
Expected Output:

Intersection is  {57, 83, 29}
First Set after removing common element  {65, 42, 78, 23}
"""




"""
Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
Given:

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
Expected Output:

First set is subset of second set - True
Second set is subset of First set -  False

First set is Super set of second set -  False
Second set is Super set of First set -  True

First Set  set()
Second Set  {67, 73, 43, 48, 83, 57, 29}
"""




"""
Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
Given:

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
Expected Outcome:

After removing unwanted elements from list [47, 69, 76, 97]
"""




"""
Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
Given:

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
Expected Outcome:

[47, 52, 44, 53, 54]
"""




"""
Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
Given:

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
Expected Outcome:

unique items [87, 45, 41, 65, 99]
tuple (87, 45, 41, 65, 99)
min: 41
max: 99

"""

"""//////////////**** LIST EXCERCISES *****//////////////"""

"""
Exercise 1: Reverse a list in Python
Given:

list1 = [100, 200, 300, 400, 500]
Expected output:

[500, 400, 300, 200, 100]
"""




"""
Exercise 2: Concatenate two lists index-wise
Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

Given:

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
Expected output:

['My', 'name', 'is', 'Kelly']
"""




"""
Exercise 3: Turn every item of a list into its square
Given a list of numbers. write a program to turn every item of a list into its square.

Given:

numbers = [1, 2, 3, 4, 5, 6, 7]
Expected output:

[1, 4, 9, 16, 25, 36, 49]
"""




"""
Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Expected output:

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""




"""
Exercise 5: Iterate both lists simultaneously
Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
Expected output:

10 400
20 300
30 200
40 100
"""




"""
Exercise 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
Expected output:

["Mike", "Emma", "Kelly", "Brad"]
"""




"""
Exercise 7: Add new item to list after a specified item
Write a program to add item 7000 after 6000 in the following Python List

Given:

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Expected output:

[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
"""




"""
Exercise 8: Extend nested list by adding the sublist
You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.

Given List:

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]
Expected Output:

['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
"""




"""
Exercise 9: Replace list’s item with new value if found
You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

Given:

list1 = [5, 10, 15, 20, 25, 50, 20]
Expected output:

[5, 10, 15, 200, 25, 50, 20]
"""




"""
Exercise 10: Remove all occurrences of a specific item from a list.
Given a Python list, write a program to remove all occurrences of item 20.

Given:

list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output:

[5, 15, 25, 50]
Show Solution


"""


"""/**************Python Dictionary Exercise for Beginners***************************/"""

"""
Exercise 1: Convert two lists into a dictionary
Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
"""




"""
Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
"""





"""

Exercise 3: Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
Expected output:

80

"""




"""
Exercise 4: Initialize dictionary with default values
In Python, we can initialize the keys with the same values.

Given:

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
Expected output:

{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
"""




"""
Exercise 5: Create a dictionary by extracting the keys from a given dictionary
Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
Expected output:

{'name': 'Kelly', 'salary': 8000}
"""




"""
Exercise 6: Delete a list of keys from a dictionary
Given:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
Expected output:

{'city': 'New york', 'age': 25}
"""




"""
Exercise 7: Check if a value exists in a dictionary
We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

Write a Python program to check if value 200 exists in the following dictionary.

Given:

sample_dict = {'a': 100, 'b': 200, 'c': 300}
Expected output:

200 present in a dict
"""




"""
Exercise 8: Rename key of a dictionary
Write a program to rename a key city to a location in the following dictionary.

Given:

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
Expected output:

{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
"""




"""
Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
Expected output:

Math
"""




"""
Exercise 10: Change value of a key in a nested dictionary
Write a Python program to change Brad’s salary to 8500 in the following dictionary.

Given:

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
Expected output:

{
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 8500}
}

"""
"""/**************Python SET Exercise for Beginners***************************/"""


"""
Exercise 1: Add a list of elements to a set
Given a Python list, Write a program to add all its elements into a given set.

Given:

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
Expected output:

Note: Set is unordered.

{'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
"""





"""
Exercise 2: Return a new set of identical items from two sets
Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{40, 50, 30}
"""





"""
Exercise 3: Get Only unique items from two sets
Write a Python program to return a new set with unique items from both sets by removing duplicates.

Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{70, 40, 10, 50, 20, 60, 30}
Note: set is unordered so not necessary this will be the order of the item.
"""





"""
Exercise 4: Update the first set with items that don’t exist in the second set
Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set.

Given:

set1 = {10, 20, 30}
set2 = {20, 40, 50}
Expected output:

set1 {10, 30}
"""





"""
Exercise 5: Remove items from the set at once
Write a Python program to remove items 10, 20, 30 from the following set at once.

Given:

set1 = {10, 20, 30, 40, 50}
Expected output:

{40, 50}
"""





"""
Exercise 6: Return a set of elements present in Set A or B, but not both
Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{20, 70, 10, 60}
"""





"""
Exercise 7: Check if two sets have any elements in common. If yes, display the common elements
Given:

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
Expected output:

Two sets have items in common
{10}
"""





"""
Exercise 8: Update set1 by adding items from set2, except common items
Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{70, 10, 20, 60}
"""





"""
Exercise 9: Remove items from set1 that are not common to both set1 and set2
Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{40, 50, 30}
Show Hint
Show Solution

"""

"""/**************Python TUPLE Exercise for Beginners***************************/"""

"""
Exercise 1: Reverse the tuple
Given:

tuple1 = (10, 20, 30, 40, 50)
Expected output:

(50, 40, 30, 20, 10)
"""





"""
Exercise 2: Access value 20 from the tuple
The given tuple is a nested tuple. write a Python program to print the value 20.

Given:

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
Expected output:

20
"""





"""
Exercise 3: Create a tuple with single item 50
"""





"""Exercise 4: Unpack the tuple into 4 variables
Write a program to unpack the following tuple into four variables and display each variable.

Given:

tuple1 = (10, 20, 30, 40)
Expected output:

tuple1 = (10, 20, 30, 40)
# Your code
print(a) # should print 10
print(b) # should print 20
print(c) # should print 30
print(d) # should print 40
"""





"""Exercise 5: Swap two tuples in Python
Given:

tuple1 = (11, 22)
tuple2 = (99, 88)
Expected output:

tuple1: (99, 88)
tuple2: (11, 22)
"""





"""Exercise 6: Copy specific elements from one tuple to a new tuple
Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

Given:

tuple1 = (11, 22, 33, 44, 55, 66)
Expected output:

tuple2: (44, 55)
"""





"""
Exercise 7: Modify the tuple
Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222

Given:

tuple1 = (11, [22, 33], 44, 55)
Expected output:

tuple1: (11, [222, 33], 44, 55)
"""





"""
Exercise 8: Sort a tuple of tuples by 2nd item
Given:

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
Expected output:

(('c', 11), ('a', 23), ('d', 29), ('b', 37))
"""





"""
Exercise 9: Counts the number of occurrences of item 50 from a tuple
Given:

tuple1 = (50, 10, 60, 70, 50)
Expected output:

2

"""





"""
Exercise 10: Check if all items in the tuple are the same
tuple1 = (45, 45, 45, 45)
Expected output:

True

"""

"""/**************Python DATE&TIME Exercise for Beginners***************************/"""
"""

Exercise 1: Print current date and time in Python
See: Get Current Date and Time in Python

"""






"""
Exercise 2: Convert string into a datetime object
For example, You received the following date in string format. Please convert it into Python’s DateTime object.

Refer: Python String to DateTime

Given:

date_string = "Feb 25 2020 4:20PM"
Expected output:

2020-02-25 16:20:00
"""






"""Exercise 3: Subtract a week (7 days)  from a given date in Python
Refer: TimeDelta in Python

Given:

given_date = datetime(2020, 2, 25)
Expected output:

2020-02-18
"""






"""Exercise 4: Print a date in a the following format
Day_name  Day_number  Month_name  Year
Refer: Python DateTime Format Using Strftime()

Given:

given_date = datetime(2020, 2, 25)
Expected output:

Tuesday 25 February 2020
Refer Date format codes for help

"""






"""Exercise 5: Find the day of the week of a given date
Given:

given_date = datetime(2020, 7, 26)
Expected output:

Sunday
"""






"""
Exercise 6: Add a week (7 days) and 12 hours to a given date
Given:

# 2020-03-22 10:00:00
given_date = datetime(2020, 3, 22, 10, 0, 0)
Expected output:

2020-03-29 22:00:00
"""






"""

Exercise 7: Print current time in milliseconds
"""






"""

Exercise 8: Convert the following datetime into a string
Given:

given_date = datetime(2020, 2, 25)
Expected output:

"2020-02-25 00:00:00"
"""






"""Exercise 9: Calculate the date 4 months from the current date
Given:

# 2020-02-25
given_date = datetime(2020, 2, 25).date()
Expected output:

2020-06-25
"""






"""Exercise 10: Calculate number of days between two given dates
Given:

# 2020-02-25
date_1 = datetime(2020, 2, 25)

# 2020-09-17
date_2 = datetime(2020, 9, 17)
Expected output:

205 days



"""

"""/*******************************Python OOP Exercise for Beginners***************************/"""


"""
OOP Exercise 1: Create a Class with instance attributes
Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

Refer:

Classes and Objects in Python
Instance variables in Python
"""






"""
OOP Exercise 2: Create a Vehicle class without any variables and methods
"""






"""
""""""OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
Given:

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.

Expected Output:

Vehicle Name: School Volvo Speed: 180 Mileage: 12
Refer: Inheritance in Python

"""






"""OOP Exercise 4: Class Inheritance
Given:

Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
Expected Output:

The seating capacity of a bus is 50 passengers
Refer:

Inheritance in Python
Polymorphism in Python
"""






"""
OOP Exercise 5: Define a property that must have the same value for every class instance (object)
Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

Use the following code for this exercise.

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
Expected Output:

Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18
Refer: Class Variable in Python

"""






"""
OOP Exercise 6: Class Inheritance
Given:

Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.

Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a child class.

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())
Expected Output:

Total Bus fare is: 5500.0
"""






"""
OOP Exercise 7: Check type of an object
Write a program to determine which class a given Bus object belongs to.

Given:

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
"""






"""
OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
Given:

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)






"""

"""/*******************************Python JSON Exercise for Beginners***************************/"""

"""
Exercise 1: Convert the following dictionary into JSON format
data = {"key1" : "value1", "key2" : "value2"}
Expected Output:

data = {"key1" : "value1", "key2" : "value2"}

"""



"""

Exercise 2: https://pynative.com/python-json-exercise/

"""



"""
Exercise 3: PrettyPrint following JSON data
PrettyPrint following JSON data with indent level 2 and key-value separators should be (",", " = ").

sampleJson = {"key1": "value1", "key2": "value2"}
Expected Output:

{
  "key1" = "value2",
  "key2" = "value2",
  "key3" = "value3"
}

"""



"""
Exercise 4: Sort JSON keys in and write them into a file
Sort following JSON data alphabetical order of keys

sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
Expected Output:

{
    "age": 29,
    "id": 1,
    "name": "value2"
}

"""



"""

Exercise 5: Access the nested key ‘salary’ from the following JSON
import json

https://pynative.com/python-json-exercise/

# write code to print the value of salary
Expected Output:

7000
"""



"""
Exercise 6: Convert the following Vehicle Object into JSON
import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

# Convert it into JSON format
Expected Output:

{
    "name": "Toyota Rav4",
    "engine": "2.5L",
    "price": 32000
}
"""



"""
Exercise 7: Convert the following JSON into Vehicle Object
{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }
For example, we should be able to access Vehicle Object using the dot operator like this.

vehicleObj.name, vehicleObj.engine, vehicleObj.price
Show Solution
Exercise 8: Check whether following json is valid or invalid. If Invalid correct it
{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000
            "bonus":800
         }
      }
   }
}
"""



"""
Exercise 9: Parse the following JSON to get all the values of a key ‘name’ within an array
[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]
Expected Output:

["name1", "name2"]

Show Solution


"""

"""/*******************************Python Data generation Exercise for Beginners***************************/"""


"""
Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5
Reference article for help: Python get a random number within a range


"""




"""
Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
Note you must adhere to the following conditions:

The lottery number must be 10 digits long.
All 100 ticket number must be unique.
Hint: Generate a random list of 1000 numbers using randrange() and then use the sample() method to pick lucky 2 tickets.


"""




"""
Exercise 3: Generate 6 digit random secure OTP
Reference article for help:

Python secrets module to generate secure numbers
Python get a random number within a range

"""




"""
Exercise 4: Pick a random character from a given String
Reference article for help: random.choice()


"""




"""
Exercise 5: Generate random String of length 5
Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.

Reference article for help: Generate random String in Python.


"""




"""
Exercise 6: Generate a random Password which meets the following conditions
Password length must be 10 characters long.
It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
Reference article for help: Generate random String and Password in Python


"""




"""
Exercise 7: Calculate multiplication of two random float numbers
Note:

First random float number must be between 0.1 and 1
Second random float number must be between 9.5 and 99.5
Reference article for help: Generate a random float number between a float range


"""




"""
Exercise 8: Generate random secure token of 64 bytes and random URL
Reference article for help: Python secrets module to generate a secure token and URL


"""




"""
Exercise 9: Roll dice in such a way that every time you get the same number
Dice has 6 numbers (from 1 to 6). Roll dice in such a way that every time you must get the same output number. do this 5 times.

Reference article for help:

How to seed random number generator
random.choice()

"""




"""
Exercise 10: Generate a random date between given start and end dates

"""

"""/*******************************Python Pandas generation Exercise for Beginners***************************/"""
"""
Mutlaka yerinden bak!!!!!!!!!!!!
"""

"""/*******************************Python Database Programming Exercise ***************************/"""

"""
Mutlaka yerinden bak!!!!!!!!!!!!

"""
""