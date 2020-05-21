counts = dict()
print("Enter a line of text:")
line = input('')
words = line.split()
print('Words: ', words)
print('Counting:....')
for word in words:
    counts[word] = counts.get(word, 0)+1
print("Counts:", counts)
for key in counts:
    print(key,counts[key])
like, um, no, I refuse to do this, as compared to the other ones we actually tried. Now we're not even going to try. It's like dude, how about we just write some Python code to solve this problem? I know how this turns out. We've seen this story before. 