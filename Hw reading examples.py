Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========== RESTART: C:/Users/user/Downloads/Hw reading examples.py ==========
Traceback (most recent call last):
  File "C:/Users/user/Downloads/Hw reading examples.py", line 1, in <module>
    from cs115 import*
ModuleNotFoundError: No module named 'cs115'
>>> 3 + 5
8
>>> (3 + 5) * 2 - 1
15
>>> 3 + 5 * 2 - 1
12
>>> 6 / 2
3.0
>>> 2 ** 5
32
>>> 10 ** 3
1000
>>> 52 % 10
2
>>> 11/ 2
5.5
>>> 11.0 / 2
5.5
>>> 11 / 2.0
5.5
>>> 11.0 / 2.0
5.5
>>> pi = 3.1415926
>>> pi * (10 ** 2)
314.15926
>>> name1 = "Ben"
>>> name2= 'Jerry'
>>> name1
'Ben'
>>> name2
'Jerry'
>>> len(name1)
3
>>> len(name2)
5
>>> len('I love spam!')
12
>>> name1[0]
'B'
>>> name1[1]
'e'
>>> name1[2]
'n'
>>> name1[3]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    name1[3]
IndexError: string index out of range
>>> bestFood = 'spam burrito'
>>> bestFood[0:3]
'spa'
>>> bestFood[0:4]
'spam'
>>> bestFood[2:6]
'am b'
>>> bestFood[1:]
'pam burrito'
>>> bestFood[:4]
'spam'
>>> 'yum' + 'my'
'yummy'
>>> 'yum' * 3
'yumyumyum'
>>> oddNumbers = [1 , 3 , 5 ,7 , 9, 11]
>>> friends = ['rachel' , 'monica' , ' phoebe' , 'joey' , 'ross']
>>> stuff = [2, 'hello' , 2.718]
>>> stuff = [2, 'hello' , 2.718 , {1 , 2 , 3]]
SyntaxError: invalid syntax
>>> len(stuff)
3
>>> stuff [0]
2
>>> stuff [1]
'hello'
>>> stuff [2]
2.718
>>> stuff [2:4]
[2.718]
>>> mylist = [1, 2, 3]
>>> mylist + [4, 5, 6]
[1, 2, 3, 4, 5, 6]
>>> mylist * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> mylist
[1, 2, 3]
>>> 
