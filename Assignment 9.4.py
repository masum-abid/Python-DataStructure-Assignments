name = input("Enter file:")
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    w = line.split()
    wd = w[1]
    if wd not in counts:
        counts[wd] = 1
    else:
        counts[wd] = counts.get(wd, 0) + 1        
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        
print(bigword, bigcount)
