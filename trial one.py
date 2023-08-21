Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from cs115 import *
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from cs115 import *
  File "C:\Users\user\Downloads\cs115.py", line 64
    >>> max (2, 4)
     ^
SyntaxError: invalid syntax
>>> max (2, 4)
4
>>> from math import pi
>>> pi
3.141592653589793
>>> from math import *
>>> factorial(4)
24
>>> '
SyntaxError: EOL while scanning string literal
>>> pi
3.141592653589793
>>> 2
2
>>> "hello"
'hello'
>>> ["hi, "there"]
 
SyntaxError: invalid syntax
>>> ["hi","there"]
['hi', 'there']
>>> L = ["hi", "there"]
>>> l
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> L
['hi', 'there']
>>> L[0]
'hi'
>>> L{2}
SyntaxError: invalid syntax
>>> l[2]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l[2]
NameError: name 'l' is not defined
>>> L[2]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    L[2]
IndexError: list index out of range
>>> L + L
['hi', 'there', 'hi', 'there']
>>> L
['hi', 'there']
>>> x = 2
>>> y = 3
>>> x+y
5
>>> range(3)
range(0, 3)
>>> max
<built-in function max>
>>> range
<class 'range'>
>>> range(3)
range(0, 3)
>>> from cs115 import *
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    from cs115 import *
  File "C:\Users\user\Downloads\cs115.py", line 64
    >>> max (2, 4)
     ^
SyntaxError: invalid syntax
>>> range(5)
range(0, 5)
>>> def dbl(n):
	return n*2
>>> 
