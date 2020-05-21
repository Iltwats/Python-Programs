#Compute pay of workers using functions.
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
def computepay(h, r):
    if h <= 40:
        pr = h * r
    elif h > 40:
        pr = 40 * r + (h-40)*1.5*r
    else:
        print("Error")
    return pr


hrs = float(input("Enter Hours:"))
rate = float(input("Enter rate:"))
p = computepay(hrs, rate)
print("Pay", p)
