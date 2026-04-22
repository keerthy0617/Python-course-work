Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=set()
s={1,2,3,2,4,4,5,5,3}
s
{1, 2, 3, 4, 5}
s.add(100)
s
{1, 2, 3, 4, 5, 100}
s.add(0)
s
{0, 1, 2, 3, 4, 5, 100}
s.add(10.2)
s
{0, 1, 2, 3, 4, 5, 100, 10.2}
s.add("string")
s
{0, 1, 2, 3, 4, 5, 10.2, 100, 'string'}
s.add((1,2,3))
s
{0, 1, 2, 3, 4, 5, 10.2, 100, 'string', (1, 2, 3)}
1 in s
True
2 not in s
False
a={9,8,7,1,2,3}
b={5,3,4,1,2,7}
a
{1, 2, 3, 7, 8, 9}
b
{1, 2, 3, 4, 5, 7}
a.union(b)
{1, 2, 3, 4, 5, 7, 8, 9}
a | b
{1, 2, 3, 4, 5, 7, 8, 9}
a
{1, 2, 3, 7, 8, 9}
b
{1, 2, 3, 4, 5, 7}
a.intersection(b)
{1, 2, 3, 7}
a&b
{1, 2, 3, 7}
a-b
{8, 9}
a^b
{4, 5, 8, 9}
a
{1, 2, 3, 7, 8, 9}
{1}<a
True
{9,10}<a
False
a>{1}
True
a>{1,2,3,4,5}
False
a>{1,2,8,9}
True
a
{1, 2, 3, 7, 8, 9}
b
{1, 2, 3, 4, 5, 7}
a.isdisjoint(b)
False
c={10,11}
c
{10, 11}
a.isdisjoint(c)
True
a
{1, 2, 3, 7, 8, 9}
a.add(100)
a
{1, 2, 3, 100, 7, 8, 9}
a.update({20,40,60})
a
{1, 2, 3, 100, 7, 8, 9, 40, 20, 60}
a.remove(100)
a
{1, 2, 3, 7, 8, 9, 40, 20, 60}
a.pop()
1
a.clear()
a
set()
a.remove(7)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.remove(7)
KeyError: 7
a.discord(7)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.discord(7)
AttributeError: 'set' object has no attribute 'discord'. Did you mean: 'discard'?
a={9,8,7,1,2,3}
a
{1, 2, 3, 7, 8, 9}
a.remove(7)
a
{1, 2, 3, 8, 9}
a.remove(7)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.remove(7)
KeyError: 7
a.discord(7)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.discord(7)
AttributeError: 'set' object has no attribute 'discord'. Did you mean: 'discard'?
a.discard(7)
a
{1, 2, 3, 8, 9}
>>> a
{1, 2, 3, 8, 9}
>>> b
{1, 2, 3, 4, 5, 7}
>>> a.intersection(b)
{1, 2, 3}
>>> a.intersection_update(b)
>>> a
{1, 2, 3}
>>> a
{1, 2, 3}
>>> b
{1, 2, 3, 4, 5, 7}
>>> c=b
>>> c
{1, 2, 3, 4, 5, 7}
>>> c.add(10)
>>> c
{1, 2, 3, 4, 5, 7, 10}
>>> b
{1, 2, 3, 4, 5, 7, 10}
>>> e=c.copy()
>>> e
{1, 2, 3, 4, 5, 7, 10}
>>> c
{1, 2, 3, 4, 5, 7, 10}
>>> max(c)
10
>>> min(c)
1
>>> sorted(c)
[1, 2, 3, 4, 5, 7, 10]
>>> sum(c)
32
>>> frozen=frozenset([1,2,3])
>>> frozen.add(10)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    frozen.add(10)
AttributeError: 'frozenset' object has no attribute 'add'
