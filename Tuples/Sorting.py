d={'a':10,'b':1,'c':22}
t=sorted(d.items())
print(t)
for k,v in t:
    print(k,v)
c = {'a': 10, 'b': 1, 'c': 22}
print(sorted([(v,k) for k,v in c.items()]))
