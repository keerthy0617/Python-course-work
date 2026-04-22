Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={}
d
{}
type(d)
<class 'dict'>
d = {'name':'keerthy','batch':52}
d
{'name': 'keerthy', 'batch': 52}
d['name'] ='mehaboob'
d
{'name': 'mehaboob', 'batch': 52}
d['course']='python'
d
{'name': 'mehaboob', 'batch': 52, 'course': 'python'}
s={}
s[1]='int'
s
{1: 'int'}
s[1.2]='float'
s['demo']='string'
s
{1: 'int', 1.2: 'float', 'demo': 'string'}
s[(1,2,3)]='tuple'
s
{1: 'int', 1.2: 'float', 'demo': 'string', (1, 2, 3): 'tuple'}
s[False]=1
s
{1: 'int', 1.2: 'float', 'demo': 'string', (1, 2, 3): 'tuple', False: 1}
S
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    S
NameError: name 'S' is not defined. Did you mean: 's'?
s
{1: 'int', 1.2: 'float', 'demo': 'string', (1, 2, 3): 'tuple', False: 1}
'name in d
SyntaxError: unterminated string literal (detected at line 1)
'name' in d
True
d['name']
'mehaboob'
d.get('course')
'python'
d.get('age','age is not present')
'age is not present'
d.get('name is not present')
d
{'name': 'mehaboob', 'batch': 52, 'course': 'python'}
d.get('name','is not present')

'mehaboob'
d
{'name': 'mehaboob', 'batch': 52, 'course': 'python'}
d['course']='PFS'
d
{'name': 'mehaboob', 'batch': 52, 'course': 'PFS'}
d['age']=21
d
{'name': 'mehaboob', 'batch': 52, 'course': 'PFS', 'age': 21}
d['k1']='v1'
d
{'name': 'mehaboob', 'batch': 52, 'course': 'PFS', 'age': 21, 'k1': 'v1'}
d.update({'k2':'v2','k3':'v3'})
d
{'name': 'mehaboob', 'batch': 52, 'course': 'PFS', 'age': 21, 'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
d.popitem()
('k3', 'v3')
d.popitem()
('k2', 'v2')
d
{'name': 'mehaboob', 'batch': 52, 'course': 'PFS', 'age': 21, 'k1': 'v1'}
d.pop('name')
'mehaboob'
d
{'batch': 52, 'course': 'PFS', 'age': 21, 'k1': 'v1'}
del d['batch']
d
{'course': 'PFS', 'age': 21, 'k1': 'v1'}
>>> d.clear()
>>> d
{}
>>> d = {'name':'keerthy','batch':52}
... \
...   
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> d = {'name':'keerthy','batch':52}
>>> d
{'name': 'keerthy', 'batch': 52}
>>> d.key()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    d.key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
>>> d.keys()
dict_keys(['name', 'batch'])
>>> d.values()
dict_values(['keerthy', 52])
>>> d.items()
dict_items([('name', 'keerthy'), ('batch', 52)])
>>> sorted(d)
['batch', 'name']
>>> len(d)
2
>>> max(d)
'name'
>>> min(d)
'batch'
>>> d
{'name': 'keerthy', 'batch': 52}
>>> d.get('course')
>>> d.setdefault('course','')
''
>>> d
{'name': 'keerthy', 'batch': 52, 'course': ''}
