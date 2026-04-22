Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[]
l
[]
type(l)
<class 'list'>
l=[6,9.0,"ertes",[],[],{1:1},True]
l
[6, 9.0, 'ertes', [], [], {1: 1}, True]
a=[1,2,3,4]
b=[7,8,9]
a+b
[1, 2, 3, 4, 7, 8, 9]
a*8
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
2 in a
True
names = ['keerthy','mahesh','ravi','srivalli']
names
['keerthy', 'mahesh', 'ravi', 'srivalli']
names[0]
'keerthy'
names[-1]
'srivalli'
names
['keerthy', 'mahesh', 'ravi', 'srivalli']
names[1:3]
['mahesh', 'ravi']
names[::2]
['keerthy', 'ravi']
names[::-1]
['srivalli', 'ravi', 'mahesh', 'keerthy']
names[-3::]
['mahesh', 'ravi', 'srivalli']
names
['keerthy', 'mahesh', 'ravi', 'srivalli']
'keerthy'in names
True
'sai' in names
False
len(names)
4
sorted(names)
['keerthy', 'mahesh', 'ravi', 'srivalli']
max(names)
'srivalli'
min(names)
'keerthy'
names
['keerthy', 'mahesh', 'ravi', 'srivalli']
id(names)
2361789226496
name[2] ='sai'
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    name[2] ='sai'
NameError: name 'name' is not defined. Did you mean: 'names'?
names[2] ='sai'
names
['keerthy', 'mahesh', 'sai', 'srivalli']
id(names)
2361789226496
names.append('kranthi')
names
['keerthy', 'mahesh', 'sai', 'srivalli', 'kranthi']
['keerthy', 'mahesh', 'sai', 'srivalli', 'kranthi']
['keerthy', 'mahesh', 'sai', 'srivalli', 'kranthi']
id(names)
2361789226496
names
['keerthy', 'mahesh', 'sai', 'srivalli', 'kranthi']
names.insert(3,'ravi')
names
['keerthy', 'mahesh', 'sai', 'ravi', 'srivalli', 'kranthi']
names.extend(['vamsi','diya','srinish'])
names
['keerthy', 'mahesh', 'sai', 'ravi', 'srivalli', 'kranthi', 'vamsi', 'diya', 'srinish']
names.insert(0[46,'teja'])
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    names.insert(0[46,'teja'])
TypeError: 'int' object is not subscriptable
names.insert(0,[46,'teja'])
names
[[46, 'teja'], 'keerthy', 'mahesh', 'sai', 'ravi', 'srivalli', 'kranthi', 'vamsi', 'diya', 'srinish']
names.pop(0)
[46, 'teja']
names
['keerthy', 'mahesh', 'sai', 'ravi', 'srivalli', 'kranthi', 'vamsi', 'diya', 'srinish']
names.pop(3)
'ravi'
names.pop()
'srinish'
namespop()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    namespop()
NameError: name 'namespop' is not defined
names.remove('keerthy')
names
['mahesh', 'sai', 'srivalli', 'kranthi', 'vamsi', 'diya']
del names[0]
names
['sai', 'srivalli', 'kranthi', 'vamsi', 'diya']
names.clear()
names
[]
names
[]
names = ['keerthy','mahesh','ravi','srivalli']

names
['keerthy', 'mahesh', 'ravi', 'srivalli']
l=[1,1,1,2,3,4,3,4,5,2,1,2]
l.count(1)
4
l.count(1)
4
sorted(1)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    sorted(1)
TypeError: 'int' object is not iterable
sorted(l)
[1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5]
s
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    s
NameError: name 's' is not defined
set()
set()
1
1
l
[1, 1, 1, 2, 3, 4, 3, 4, 5, 2, 1, 2]
l.sort()
l
[1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 5]
l.sort(reverse=True)
l
[5, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
l.reverese()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    l.reverese()
AttributeError: 'list' object has no attribute 'reverese'. Did you mean: 'reverse'?
l.reverse()

l.reverse()

a=[1,2,3,4,4]
a
[1, 2, 3, 4, 4]
b=a
b
[1, 2, 3, 4, 4]
>>> a
[1, 2, 3, 4, 4]
>>> b.append(10)
>>> b
[1, 2, 3, 4, 4, 10]
>>> b.append(17)
>>> b
[1, 2, 3, 4, 4, 10, 17]
>>> a
[1, 2, 3, 4, 4, 10, 17]
>>> c=a.copy()
>>> id(a)
2361788754560
>>> id(b)
2361788754560
>>> id(c)
2361789161280
>>> c.append(6)
>>> c
[1, 2, 3, 4, 4, 10, 17, 6]
>>> a
[1, 2, 3, 4, 4, 10, 17]
>>> b
[1, 2, 3, 4, 4, 10, 17]
>>> sum(a)
41
>>> len(a)
7
>>> #[0,0.0,[],[],set(),()--false]
>>> #[1,-1,0.1,'wefsrt',[123],]
>>> any([0,0,0,'',[],[],set(),(),false])
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    any([0,0,0,'',[],[],set(),(),false])
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> any([0,0,0,'',[],[],set(),(),False])
False
>>> all([0,0,0,'',[],[],set(),(),False])
False
