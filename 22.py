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

# /************************************************************************************************************************/
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



"""
Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.

Expected Output:

For example: print('Name', 'Is', 'James') will display Name**Is**James
"""



"""
Exercise 3: Convert Decimal number to octal using print() output formatting
Given:

num = 8
Expected Output:

The octal number of decimal number 8 is 10

Show Hint
Show Solution
Exercise 4: Display float number with 2 decimal places using print()
Given:

num = 458.541315
Expected Output:

458.54
Show Hint
Show Solution
Exercise 5: Accept a list of 5 float numbers as an input from the user
Refer:

Take list as a input in Python.
Python list
Expected Output:

[78.6, 78.6, 85.3, 1.2, 3.5]

Show Hint
Show Solution
numbers = []

# 5 is the list size
# run loop 5 times
for i in range(0, 5):
    print("Enter number at location", i, ":")
    # accept float number from user
    item = float(input())
    # add it to the list
    numbers.append(item)

print("User List:", numbers)
 Run
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
Show Hint
Show Solution
Exercise 7: Accept any three string from one input() call
Write a program to take three names as input from a user in the single input() function call.

See: Get multiple inputs from a user in one line

Show Hint
Expected Output

Enter three string Emma Jessa Kelly
Name1: Emma
Name2: Jessa
Name3: Kelly
Show Solution
Exercise 8: Format variables using a string.format() method.
Write a program to use string.format() method to format the following three variables as per the expected output

Given:

totalMoney = 1000
quantity = 3
price = 450
Expected Output:

I have 1000 dollars so I can buy 3 football for 450.00 dollars.
Show Solution
Exercise 9: Check file is empty or not
Write a program to check if the given file is empty or not

Show Hint
Show Solution
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
