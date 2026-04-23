'''charger = int(input("Enter the charging:"))
if charger<=20:
    print("plz charge your phone")


products = {
    1:{'name':'bread','discount':10},
    2:{'name':'sugar','discount':0},
    3:{'name':'jam','discount':5},
    4:{'name':'butter','discount':0},
    }
print(products)

index = int(input("Enter the index: "))
if products[index]['discount']:
    print(f'{products[index]["name"]} has discount')

#best selller
products = {
    1:{'name':'iphone','best seller':True},
    2:{'name':'realme','best seller':False},
    3:{'name':'poco','best seller':True},
    4:{'name':'oppo','best seller':False},
    }
print(products)
index = int(input("Enter the index: "))
if products[index]['best seller']:
    print(f'{products[index]["name"]} has best seller')
#resume cheking
jd={'python','mysql','javascript','flask'}

skills = set(input("Enter the skills: ").split())

if jd == skills:
    print("Congrats!! your resume is shotlisted")
else:
    print(f"sorry, try again. you need this skills set:{jd-skills}")

#subcribe
plan = True
if plan:
    print("Adds won't run.without interuption")
else:
    print("Adds will run,which watch videos")
#online exam time    
time=9.00
if time<=9.00:
    print("you are allowed into the exam")
else:
    print("timed out! ,your are not allowed")
#rapido
wheels = int(input("Enter the wheels:"))
if wheels == 2:
    print('your bike is on the way.plz play $50')
elif wheels == 3:
    print('your bike is on the way.plz play $100')
elif wheels == 4:
    print('your bike is on the way.plz play $200')
else:
    print('enter a valid input')
    
#nested if


status = input("enter the status")

if status == face:
    print("unlock the mobile")
else:
    print("unable to reg face")
    if status==password:
        print("Unlock the mobile")
    else:
        print('Incorrect passwword')'''
#order
products = {
    1:{'name':'bread','discount':10},
    2:{'name':'sugar','discount':0},
    3:{'name':'jam','discount':5},
    4:{'name':'butter','discount':0},
    }
login_stutus=True
print(products)
order_id = int(input("Enter the index to order:"))
if login_stutus:
    if products[order_id]['stock']:
        print(f"{product[order_id]['name']} is order")
    else:
        print(f"{product[order_id]['name']} is outoff stock")
else:
    print("product was avalable")
    
        




    


