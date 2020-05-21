#Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
#Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).

hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate:"))
sum = hrs*rate
print("Pay: "+str(sum))
