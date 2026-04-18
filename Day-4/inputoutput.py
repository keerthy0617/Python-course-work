Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = input()
keerthy
>>> name
'keerthy'
>>> type(name)
<class 'str'>
>>> name = input("Enter your name: ")
Enter your name: keerthy
>>> name
'keerthy'
>>> age = int(input())
20
>>> age
20
>>> price = float(input())
12.3
>>> price
12.3
>>> 'java,python,html,css,js'.split(',')
['java', 'python', 'html', 'css', 'js']
>>> lang = input("Enter the languages:")
Enter the languages:java,python,html,css,js
>>> lang
'java,python,html,css,js'
>>> lang = input("Enter the languages:").slpit(',')
Enter the languages:java python html css js
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    lang = input("Enter the languages:").slpit(',')
AttributeError: 'str' object has no attribute 'slpit'. Did you mean: 'split'?
>>> lang = input("Enter the languages:").slpit()
Enter the languages:java python html css js
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    lang = input("Enter the languages:").slpit()
AttributeError: 'str' object has no attribute 'slpit'. Did you mean: 'split'?
lang = input("Enter the languages:").split()
Enter the languages:java python html css js
lang
['java', 'python', 'html', 'css', 'js']
names = input("Enter the name: ").split(',')
Enter the name: keerthy,bhavana,mahitha,ramana,dathri
names
['keerthy', 'bhavana', 'mahitha', 'ramana', 'dathri']
numbers = input("Enter the number: ").split()
Enter the number: 1 2 3 4
numbers
['1', '2', '3', '4']
['1', '2', '3', '4']
['1', '2', '3', '4']
map(int,['1', '2', '3', '4'])
<map object at 0x00000265BC182DD0>
list(map(int,['1', '2', '3', '4']))
[1, 2, 3, 4]
numbers = list(map(int,input("Enter the numbers:").split()))
Enter the numbers:1 23 5 6 743 234236 24
numbers
[1, 23, 5, 6, 743, 234236, 24]
numbers = list(map(float,input("Enter the numbers:").split()))
Enter the numbers:1.2 3.45 56.6 765.4
numbers
[1.2, 3.45, 56.6, 765.4]
numbers = tuple(map(int,input("Enter the numbers:").split()))
Enter the numbers:1 23 45 6 4 3
numbers
(1, 23, 45, 6, 4, 3)
numbers = tuple(map(float,input("Enter the numbers:").split()))
Enter the numbers:1.2 35.5 67.4
numbers
(1.2, 35.5, 67.4)
names = tuple(input().split())
keerthy ramana chandrika
names
('keerthy', 'ramana', 'chandrika')
names = set(input().split())

names = set(input().split())
keerthy mahitha bhavana
names
{'mahitha', 'bhavana', 'keerthy'}
numbers = set(map(float,input("Enter the numbers:").split()))
Enter the numbers:1.2 3.4 0.4
numbers
{0.4, 1.2, 3.4}
numbers = tuple(map(int,input("Enter the numbers:").split()))
Enter the numbers:1 2 34 556 
numbers
(1, 2, 34, 556)
numbers = set(map(int,input("Enter the numbers:").split()))
Enter the numbers:1 2 34 563
numbers
{1, 2, 563, 34}
a,b,c=[1,2,3]
a
1
b
2
c
3
a,b,c=list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
email,password = ['@gmail.com','pass@211']
email,password = input().split()
email
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    email,password = input().split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password = input().split()
keerthy@gmail.com
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    email,password = input().split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password = input().split()

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    email,password = input().split()
ValueError: not enough values to unpack (expected 2, got 0)
email,password = input().split()
keerthy@gmail.com keerthy@123
email
'keerthy@gmail.com'
password
'keerthy@123'
a=eval(input())
12
a
12
a=eval(input())

12.34 
a
12.34
a=eval(input("enter the input:" ))
enter the input:[1,2,34,45]
a
[1, 2, 34, 45]
a=eval(input("enter the input:" ))

enter the input:(1,2,3,4)
a
(1, 2, 3, 4)
a=eval(input("enter the input:" ))
enter the input:(1,2,4,56,8)
a
(1, 2, 4, 56, 8)
a=eval(input("enter the input:" ))
enter the input:{1:2,2:3,3:4}
a
{1: 2, 2: 3, 3: 4}
a=eval(input("enter the input:" ))

enter the input:true
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    a=eval(input("enter the input:" ))
  File "<string>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
a=eval(input("enter the input:" ))
enter the input:True
a
True
a,b,c = 10,20.7,'python'
a
10
b
20.7
c
'python'
print(a,b,c)
10 20.7 python
print("a =",a,'b =',b,'c =',c)
a = 10 b = 20.7 c = python
print("a =",a,'b =',b,'c =',c,sep='')
a =10b =20.7c =python
print("a =",a,'b =',b,'c =',c,sep='\n')
a =
10
b =
20.7
c =
python
print("a =",a,'b =',b,'c =',c,sep='@@@')
a =@@@10@@@b =@@@20.7@@@c =@@@python
print("a =",a,'b =',b,'c =',c,sep='@@@',end='.....')
a =@@@10@@@b =@@@20.7@@@c =@@@python.....
print(f'a={a} b={b} c={c}')
a=10 b=20.7 c=python
print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=20.700000 c=python
print('a=%d b=%2f c=%s'%(a,b,c))
a=10 b=20.700000 c=python
print('a=%d b=%.2f c=%s'%(a,b,c))
a=10 b=20.70 c=python
print('a={} b={} c={}'.format(a,b,c))
a=10 b=20.7 c=python
print('a={} b={} c={}'.format(c,a,b))
a=python b=10 c=20.7
