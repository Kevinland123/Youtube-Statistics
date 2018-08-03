print("Alright we got this!")
#import codecs

name = input("Enter file:")
if len(name) < 1 : 
    name = "history.html"

file = open(name, encoding="UTF-8")

#f=codecs.open(name, 'r')
#print(f.read())

record = dict()

for line in file:
    print(line.encode("utf-8"))
    
print("Done")