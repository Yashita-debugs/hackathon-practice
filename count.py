sentence =input("Enter a sentence")
words=sentence.lower().split()
counts = {}
for i in words:
    if i in counts:
        counts[i]=counts[i]+1
    else:
        counts[i]=1
print(counts)
