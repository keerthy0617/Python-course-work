Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Arthemtic Operator
a=20
b=10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
10/3
3.3333333333333335
10//3
3
10%3
1
10%5
0
a**b
10240000000000
2**4
16
#Comparision Operator
a>b
True
a<b
False
a>=b
True
a<=b
False
a==b
False
a!=b
True
#Assignment Operator
c=10
c
10
c=c+10
C+=10
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    C+=10
NameError: name 'C' is not defined. Did you mean: 'c'?
c
20
c-=20
c
0
c*=1000
c
0
c=10
c//=20
c
0
c=10
c
10
c*1000
10000
c//=20
c
0
c**=2
c
0
c=10
c
10
c*=1000
c
10000
c//=20
c
500
c**=2
c
250000
c%=30
c
10
c/=10
c
1.0
#logical Operatoe
T AND T=T
SyntaxError: invalid syntax
'''
T AND T = T
F AND F=F
T AND F=F
F AND T =F
T AND T AND T AND.....=T
T AND F AND T AND T....T=F'''
'\nT AND T = T\nF AND F=F\nT AND F=F\nF AND T =F\nT AND T AND T AND.....=T\nT AND F AND T AND T....T=F'
'''
T OR T = T
F OR F=F
T OR F=T
F OR T =T
T AND T AND T AND.....=T
T AND F AND T AND T....T=F'''
'\nT OR T = T\nF OR F=F\nT OR F=T\nF OR T =T\nT AND T AND T AND.....=T\nT AND F AND T AND T....T=F'
#All false are there then if one true is there then it will true
a
20
b
10
a%3==0
False
b%3==0
False
a%5==0 and b%5==0
True
a%5==0 and b%5==0

True
KeyboardInterrupt
a%20==0 and b%20==0
False
a%20==0 or b%20==0
True
not b%20==0
True
#Membership Operator
#str,list,tuple,set,dict
s='python'
'o' in s
True
'z' in s
False
'i' not in s
True
'o' not in s
False
#list
l=['keerthy','nagaraju','mehaboob','bhavana']
l
['keerthy', 'nagaraju', 'mehaboob', 'bhavana']
'keerthy' in l
True
'ramana' in l
False
#tuple
t=(1,2,3,4)
1 in t
True
5 in t
False
3 not in t
False
2 not in t
False
#set
s=[1,2,3,4,5]
3 in s
True
6 in s
False
#dictionary
d={1:2,2:3,3:4}
9 in s
False
1 in s
True
#identity Opeartoe
l=[1,2,3,4,5]
l
[1, 2, 3, 4, 5]
m=[1,2,3,4,5]
>>> m
[1, 2, 3, 4, 5]
>>> n=m
>>> n
[1, 2, 3, 4, 5]
>>> n==1
False
>>> n==l
True
>>> n==m
True
>>> n is m
True
>>> n is l
False
>>> n not is l
SyntaxError: invalid syntax
>>> n is not l
True
>>> id(l)
1853824963648
>>> id(n)
1853824906880
>>> id(m)
1853824906880
>>> #bitwise operator
>>> 12 & 13
12
>>> 7 & 12
4
>>> 7 |12
15
>>> 7 ^ 12
11
>>> ~-14
13
>>> 8<<2
32
>>> 8>>2
2
