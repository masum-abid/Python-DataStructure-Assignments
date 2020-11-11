name = input("Enter file:")
handle = open(name)


counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    w = line.split()
    wd = w[5]
    delimiter = ':'
    wd = wd.split(delimiter)
    wrd = wd[0]
    if wrd not in counts:
        counts[wrd] = 1
    else:
        counts[wrd] = counts.get(wrd, 0) + 1

for key, val in sorted(counts.items()):
    print(key, val)


///s.txt/mbox-short.txt 