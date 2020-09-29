#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
#Once 'done' is entered, print out the largest and smallest of the numbers.
#If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.

largest = None
smallest = None
while True:
    try:
        num = (input("Enter a number: "))
        if num == "done":
            break
        #print (num)
        num = int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
            smallest = num
    except ValueError:
        print("Invalid input")


print("Maximum is", largest)
print("Minimum is", smallest)