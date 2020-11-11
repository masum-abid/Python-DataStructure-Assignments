fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.split()
    for i in line:
        if not i in lst:
            lst.append(i)
        else:
            continue
lst.sort()
print(lst)
