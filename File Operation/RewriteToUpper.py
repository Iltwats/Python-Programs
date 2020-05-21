# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    Chang = line.upper()
    Edited = Chang.rstrip()
    print(Edited)
