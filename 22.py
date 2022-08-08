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

