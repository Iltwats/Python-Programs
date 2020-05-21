t=[9,41,12,3,74,15]
k=t[1:3]        #slicing of list
t.append(89)    # add the element to the last of list
t.append(1)
print(t)
print(k)
print(len(t))       #prints length of list
print(max(t))       #prints max element of list
print(min(t))       #prints min element of list
print(sum(t))       #prints sum of elements of list
print("{:.2f}".format(sum(t)/len(t)))       #prints average elements of list round off to 2 places

t.sort()        # sorts the array in ascending order
print(t)    
t.pop(2)        # removes the element at index 2 from the list
print(t)
print(t.index(41))      # tells index of a particular element
t.append(3)
print(t.count(3))       # tells the count of a element in the list
