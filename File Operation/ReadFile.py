import os
os.getcwd()
fhand = open('est.txt')
inp=fhand.read()
print(len(inp))
print(inp[:20])

