Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=()
t=tuple()
type(t)
<class 'tuple'>
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=(1,2.3,'string',[1,2,3],(1,2,3),(1,2,3){1:1,2:2},false)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
t=(1,2.3,'string',[1,2,3],(1,2,3),(1,2,3),{1:1,2:2},False)
t
(1, 2.3, 'string', [1, 2, 3], (1, 2, 3), (1, 2, 3), {1: 1, 2: 2}, False)
l=(1,1,1,1,1)
l
(1, 1, 1, 1, 1)
a=(1,2,3)
b=(4,5,6)
a+b
(1, 2, 3, 4, 5, 6)
a*3
(1, 2, 3, 1, 2, 3, 1, 2, 3)
a
(1, 2, 3)
l[2]
1
t
(1, 2.3, 'string', [1, 2, 3], (1, 2, 3), (1, 2, 3), {1: 1, 2: 2}, False)
t[1:4]
(2.3, 'string', [1, 2, 3])
t[-5:]
([1, 2, 3], (1, 2, 3), (1, 2, 3), {1: 1, 2: 2}, False)
t[2]
'string'
t[-1]
False
'srting' in t
False
(1,2,3) in t
True
(7,8) in t
False
t
(1, 2.3, 'string', [1, 2, 3], (1, 2, 3), (1, 2, 3), {1: 1, 2: 2}, False)
lent(t)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    lent(t)
NameError: name 'lent' is not defined. Did you mean: 'len'?
len(t)
8
max(t)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    max(t)
TypeError: '>' not supported between instances of 'str' and 'float'
t=(1,2,3,4,5,6,7,8,9)
max(t)
9
min(t)
1
sorted(t)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
t.count(1)
1
>>> a,b =[1,2]
>>> a
1
>>> b
2
>>> a=(1,2,3,4)
>>> w,x,y,z=a
>>> w
1
>>> t
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> y
3
>>> a.index($)
SyntaxError: invalid syntax
>>> a.index(4)
3
>>> a
(1, 2, 3, 4)
>>> sum(a)
10
>>> a
(1, 2, 3, 4)
>>> t
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> t(1,2,3[4,5])
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    t(1,2,3[4,5])
TypeError: 'int' object is not subscriptable
>>> t=(1,2,3[4,5])
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    t=(1,2,3[4,5])
TypeError: 'int' object is not subscriptable
>>> t[3].append(10)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    t[3].append(10)
AttributeError: 'int' object has no attribute 'append'
