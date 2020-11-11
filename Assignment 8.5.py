fname = input("Enter file name: ")
fh = open(fname)
count = 0
for i in fh:
    i = i.rstrip()
    if not i.startswith('From '):
        continue
    count = count + 1
    x = i.split()
    print(x[1])
    

print('There were', count, 'lines in the file with From as the first word')
    	
