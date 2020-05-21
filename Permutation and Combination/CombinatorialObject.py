from itertools import product
from itertools import permutations
from itertools import combinations
#Rule of sum
print(['Alice', 'Bob', 'Charlie']  + [0, 1, 2, 3, 4])
print("__")
#Rule of product
for p in product(['a', 'b', 'c'], ['x', 'y']):
  print("".join(p))
print("__")
#Tuples
for p in product("ab", repeat=3):
  print("".join(p))
print("__")
#Permutations
for p in permutations("abcd", 2):
  print("".join(p))
print("__")
#Combinations
for c in combinations("abcdefgh",2):
    print("".join(c))
print("__")
