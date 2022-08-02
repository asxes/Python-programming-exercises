"""
Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
"""


def cift():
    str = input("string gir :")
    e = tuple(str)
    z = []
    for i in e:
        z.append(i)
        i += 2
    print(z)


cift()
#     z = []
#     i = 0
#
#     for i in y:  # range(len(y)):
#
#         r = y.append[i]
#
#         i += 2
#
#     print(r)
#
#
# cift()
