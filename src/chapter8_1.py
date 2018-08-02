print("WALUIGI NUMBAH ONE!")
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    thing = line.split()
    for a in thing:
        if a not in lst:
            lst.append(a)
    #lst.append(line.split())
print(lst)
lst.sort()
print(lst)

print("did it work")