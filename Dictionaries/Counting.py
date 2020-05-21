# Create a dictionary from list items

counts=dict()
names=['csev','cwen','csev','zian','csev']
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1
print(counts)
    
print(counts.get('zian'))