fname = input("Enter file name: ")
fh = open(fname)
x=0
y = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x += float(line[20:])
    y += 1 
    
print('Average spam confidence:', x/y)