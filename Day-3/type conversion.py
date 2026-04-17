Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
type(a)
<class 'int'>
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
#float can convert into ,int,str,complex,bool.
a=1.0
int(a)
1
str(a)
'1.0'
complex(a)
(1+0j)
list(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(a)
TypeError: 'float' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(a)
TypeError: 'float' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(a)
TypeError: 'float' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(a)
TypeError: 'float' object is not iterable
bool(a)
True
#Complex can convert into str,bool
a=10+0j
int(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
str(a)
'(10+0j)'
list(a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(a)
TypeError: 'complex' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tuple(a)
TypeError: 'complex' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    set(a)
TypeError: 'complex' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    dict(a)
TypeError: 'complex' object is not iterable
bool(a)
True
#str can convert into int(numeric),float(numeric),complex(numeric),set,list,tuple,bool
a='python'
int(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'python'
float(a)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    float(a)
ValueError: could not convert string to float: 'python'
complex(a)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    complex(a)
ValueError: complex() arg is a malformed string
str(a)
'python'
list(a)
['p', 'y', 't', 'h', 'o', 'n']
tuple(a)
('p', 'y', 't', 'h', 'o', 'n')
set(a)
{'n', 'p', 't', 'y', 'o', 'h'}
bool(a)
True
a=10
int(a)
10
a='10'
int(a)
10
float(a)
10.0
complex(a)
(10+0j)
#list can convert intostr,tuple,set,bool
l=[1,2,3,4,5]
int(a)
10
int(l)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
str(l)
'[1, 2, 3, 4, 5]'
tuple(l)
(1, 2, 3, 4, 5)
set(l)
{1, 2, 3, 4, 5}
dict(l)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
#tuple can convert into str,list,set,bool
T=(1,2,3,4,5)
int(T)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    int(T)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(T)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    float(T)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(T)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    complex(T)
TypeError: complex() first argument must be a string or a number, not 'tuple'
str(T)]
SyntaxError: unmatched ']'
str(T)
'(1, 2, 3, 4, 5)'
list(T)
[1, 2, 3, 4, 5]
set(T)
{1, 2, 3, 4, 5}
dict(T)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    dict(T)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(T)
True
set can convert it into str,list,tuple,bool
s={1,2,3,4,,4,5,5,6,6,7}
SyntaxError: invalid syntax
s={1,2,3,4,4,5,5,6,6,7}
s
{1, 2, 3, 4, 5, 6, 7}
int(s)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
complex(a)
(10+0j)
complex(s)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
str(s)
'{1, 2, 3, 4, 5, 6, 7}'
list(s)
[1, 2, 3, 4, 5, 6, 7]
tuple(s)
(1, 2, 3, 4, 5, 6, 7)
dict(s)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(s)
True
dict can convert into str,list,set,tuple,bool
d={'Name':'Keerthy','age':'20','course':'PFS'}
d
{'Name': 'Keerthy', 'age': '20', 'course': 'PFS'}
int(d)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(d)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
str(d)
"{'Name': 'Keerthy', 'age': '20', 'course': 'PFS'}"
list(d)
['Name', 'age', 'course']
set(d)
{'age', 'Name', 'course'}
>>> tuple(d)
('Name', 'age', 'course')
>>> bool(d)
True
>>> a=true
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>>#bool can covert into int,float,str,complex
a=True
>>> int(a)
1
>>> float(a)
1.0
>>> complex(a)
(1+0j)
>>> str(a)
'True'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    list(a)
TypeError: 'bool' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    set(a)
TypeError: 'bool' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    tuple(a)
TypeError: 'bool' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    dict(a)
TypeError: 'bool' object is not iterable
>>> bool(a)
True
