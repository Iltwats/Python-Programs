#code that lists all salads combination from T=`tomato', B=`bell pepper', L=`lettuce', E=`eggplant for 7 units
# similar to selection 7 types from 4
from itertools import combinations_with_replacement
count=0
for c in combinations_with_replacement("TBLE", 7):
    print("".join(c))
    count+=1

print(count)