fruit='banana'
# two types of iteration with or without iteration variable
index=0
# 1.
while index < len(fruit):
    letter=fruit[index]
    print(index, letter)
    index=index+1
# 2.
for letter in fruit:
    print(letter)

