length = 10
width = 5
area = length * width

if area > 30:
    print("Large area")
else:
    print("Small area")

x = 10
print(x)

age = 25

def greet():
    print(age)


age = 25 # 'age' is an identifier (valid)
_name = "John" # '_name' is a valid identifier
score1 = 88


import keyword

print(keyword.kwlist) # List of all keywords
print(len(keyword.kwlist)) # Total number of keywords



product_name = "Laptop"
price = 45000
in_stock = True
print(product_name, price, in_stock)


a, b, c = 10, 20, 30
print(a, b, c) 


x = y = z = 100
print(x, y, z) 



x = 5
x = 10
print(x)



a, b = 5, 10
a, b = b, a
print(a, b)


x = 100
del x
# print(x) # Raises: NameError: name 'x' is not defined
