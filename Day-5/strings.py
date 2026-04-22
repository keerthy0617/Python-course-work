Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a="keerthy"
a
'keerthy'
type(a)
<class 'str'>
name= 'abc'
lname = 'xyz'
name+lname
'abcxyz'
name*7
'abcabcabcabcabcabcabc'
'*'*30
'******************************'
a='python'
a[4]
'o'
a[5]
'n'
a[1]
'y'
a[0]
'p'
a[-1]
'n'
a[-2]
'o'
a[-3]
'h'
a[-4]
't'
names = 'keerthy mahitha bhavana priya'
names
'keerthy mahitha bhavana priya'
names[1]
'e'
name[-1]
'c'
names[-1]
'a'
names[0:7]
'keerthy'
names[0:8:2]
'kety'
names[:15]
'keerthy mahitha'
names
'keerthy mahitha bhavana priya'
names[::2]
'ketymhtabaaapia'
names[-1]
'a'
names[-1:-5:-1]
'ayir'
names[-5:]
'priya'
names[::-1]
'ayirp anavahb ahtiham yhtreek'
'keerthy' in names
True
'mehaboob' in names
False
len(names)
29
sorted(names)
[' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'e', 'e', 'h', 'h', 'h', 'h', 'i', 'i', 'k', 'm', 'n', 'p', 'r', 'r', 't', 't', 'v', 'y', 'y']
max(names)
'y'
min(names)
' '
ord('a')
97
ord('A')
65
ord('')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    ord('')
TypeError: ord() expected a character, but string of length 0 found
ord(' ' )
32
chr(100)
'd'
chr(90)
'Z'
names
'keerthy mahitha bhavana priya'
names.upper()
'KEERTHY MAHITHA BHAVANA PRIYA'
names.lower()
'keerthy mahitha bhavana priya'
names.capitalize()
'Keerthy mahitha bhavana priya'
names.title()
'Keerthy Mahitha Bhavana Priya'
names
'keerthy mahitha bhavana priya'
names.swapcase()
'KEERTHY MAHITHA BHAVANA PRIYA'
"fkjzshdfhzlriugxzhfjehr323".casefold()
'fkjzshdfhzlriugxzhfjehr323'
names
'keerthy mahitha bhavana priya'
names.center(50,'*')
'**********keerthy mahitha bhavana priya***********'
names.center(50,' ')
'          keerthy mahitha bhavana priya           '
names.rjust(50,'*')
'*********************keerthy mahitha bhavana priya'
names.ljust(50,'*')
'keerthy mahitha bhavana priya*********************'
names.zfill(50,'*')
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    names.zfill(50,'*')
TypeError: str.zfill() takes exactly one argument (2 given)
num='245364'
num
'245364'
num.zfill(10)
'0000245364'
names
'keerthy mahitha bhavana priya'
names.fine('keerthy')
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    names.fine('keerthy')
AttributeError: 'str' object has no attribute 'fine'. Did you mean: 'find'?
names.find('keerthy')
0
names.find('z')
-1
names.find('a')
9
names.rfind('a)
            
SyntaxError: unterminated string literal (detected at line 1)
names.rfind('a')
            
28
names.index('a')
            
9
names.rindex('a')
            
28
names.count('b')
            
1
names.count('k')
            
1
names
            
'keerthy mahitha bhavana priya'
names.replace('a','*')
            
'keerthy m*hith* bh*v*n* priy*'
names.maketrans('aeiou','12345')
            
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
names.translate(names.maketrans('aeiou','12345'))
            
'k22rthy m1h3th1 bh1v1n1 pr3y1'
names
            
'keerthy mahitha bhavana priya'
names.split()
            
['keerthy', 'mahitha', 'bhavana', 'priya']
names.rsplit(' ' ,2)
            
['keerthy mahitha', 'bhavana', 'priya']
names.lsplit(' ' ,2)
            
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    names.lsplit(' ' ,2)
AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?
s='python\programming\with\dsa'
            
s
            
'python\\programming\\with\\dsa'
s.splitlines()
            
['python\\programming\\with\\dsa']
l=['keerthy', 'mahitha', 'bhavana', 'priya']
            
','.join(1)
            
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    ','.join(1)
TypeError: can only join an iterable
','.join(l)
            
'keerthy,mahitha,bhavana,priya'
'@'.join(l)
            
'keerthy@mahitha@bhavana@priya'
>>> names
...             
'keerthy mahitha bhavana priya'
>>> names.paryition(' ')
...             
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    names.paryition(' ')
AttributeError: 'str' object has no attribute 'paryition'. Did you mean: 'partition'?
>>> names.partition(' ')
... 
('keerthy', ' ', 'mahitha bhavana priya')
>>> names.partition('p')
...             
('keerthy mahitha bhavana ', 'p', 'riya')
>>> names.partition('a')
...             
('keerthy m', 'a', 'hitha bhavana priya')
>>> s='     helllo    world     ''
...             
SyntaxError: unterminated string literal (detected at line 1)
>>> KeyboardInterrupt
>>> s='     helllo    world     '
...             
>>> s.strip()
...             
'helllo    world'
>>> s.rstrip()
...             
'     helllo    world'
>>> s.lstrip()
...             
'helllo    world     '
>>> s.replace(' ','')
...             
'hellloworld'
s='python programming lang'
s.startswith('p')
True
s.endswitch('p')
false

