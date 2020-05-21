#forming groups from 5 people to a 3 member team
import itertools as it 
count=0
for c in it.combinations("abcde",3):
    print("".join(c))
    count+=1
print(count/2)


