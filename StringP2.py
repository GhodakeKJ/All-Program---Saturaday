s="hyderabad is Capital Of Telangana"
print(s.capitalize()) #Hyderabad is capital of telangana First Letter Capitalize Only
print(s.title()) #Hyderabad Is Capital Of Telangana First Letter Of Every Word Will Capitalize
print(s.find("b")) #Finding Index Of char 6
print(s.isalnum()) #False
a="Python"
print(a.isalnum())
print(a.isalpha())
print(a.isdigit())
b="1234"
print(b.isdigit()) #True
print(s.islower()) #False
print(s.isupper())
print(s.upper()) #HYDERABAD IS CAPITAL OF TELANGANA
print(s.lower())  #hyderabad is capital of telangana
tpl=("Java","Python","Data Science")
s=" "
print(s.join(tpl))
k="Python-Is-An-OOP-Lang"
h=" "
print(k.split("-"))
