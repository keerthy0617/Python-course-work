#str,list,tuple,set,dict,range()
s='python'
for i in s:
    print(i)
l=[1,2,3,4]
for i in l:
    print(i)

t=(1,2,3,4)
for i in t:
    print(i)

s={1,2,3,4,5}
for i in s:
    print(i)
d={1:2,2:3,3:4,4:5}
for i in  d:
    print(i,d[i])

for i in range(0,10,1):
    print(i)
for i in range(2,11,2):
    print(i)
for i in range(1,10,2):
    print(i)
for i in range(5,51,5):
    print(i)
for i in range(10,0,-1):
    print(i)
for i in range(20,9,1):
    print(i)
for i in range(30,41):
    print(i)
s='python'
for i in enumerate(s):
    print(i)
for i in range(len(s)):
    print(i)
for i in range(len(s)):
    print(i,s[i])
l=['keerthy','dhatri','bhavana','mahitha']
for i in enumerate(l):
    print(i[0],i[1])
for i in range(len(l)):
    print(i,l[i])
s={1,2,3,4}
for i in enumerate(s):
    print(i[0],i[1])
d={1:2,2:3,3:4}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])
for i in range(10):
    pass
for i in range(10):
    if i==5:
        break
    else:
        print(i)

for i in range(10):
    if i==5:
        continue
    else:
        print(i)
#for with else
pin=12345
for i in range(5):
    epin=int(input("Enter the pin:"))
    if pin==epin:
        print("Login Succesful")
        break
    else:
        print("Incorrect pin:")
else:
    print("Try Again after 60 sec")


products=['bread','sugar','jam','butter']
a='sugar'
for i in products:
    if i==a:
        print(i)
        break
    else:
        print("not found")
