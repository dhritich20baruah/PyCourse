# print(2+1)
# a = 10
# a = a+a
# print(a)
# print(type(a))
# print('This is a string')
# print("This is also a string")
# print("This isn't a string")
# print('Hello \n world')
# print('Hello \t world')
# a = len('I am')
# print(a)
x = 'abcdefgh'
y = x[2:]
print(y)
z = x[2:4]
print(z)
v = x[2::2]
print(v)
# Reverse a string
r = x[::-1]
print(r)
string = "dhritiman chandra baruah"
print(string.title())
print(string.upper())
print(string.lower())
# f-string
first_name = 'dhritiman'
last_name = "baruah"
full_name = f"{first_name} {last_name}"
print(full_name);
full_name_greet = f"Hello, {full_name.title()}"
print(full_name_greet)
# format method
full_namef = "{} {}".format(first_name, last_name);
print(full_namef)
# remove extra white space  with .rstrip()
x = " python "
y = x.lstrip() #strip from left
z = x.rstrip() #strip from right
print(y, z)