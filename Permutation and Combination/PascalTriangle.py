#Program to find n chose k using pascal triangle

C=dict() #C([n,k]) is equal to n chose k
for n in range(8):
    C[n,0]=1
    C[n,n]=1

    for k in range(1,n):
        C[n,k]=C[n-1,k-1]+C[n-1,k]

print(C[6,3])

# Program to find sum of all elements upto nth row in Pascal triangle.
# Function to find sum of all elements upto nth row.


def calculateSum(n):

	# Initialize sum with 0
	sum = 0

	# Calculate 2 ^ n
	sum = 1 << n

	return (sum - 1)


# Driver unicode
n = 6
print("Sum of all elements:", calculateSum(n))
