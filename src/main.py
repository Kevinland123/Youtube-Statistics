print("Alright we got this!")
#import codecs

name = input("Enter file:")
if len(name) < 1 : 
    name = "history2.html"

file = open(name, encoding="UTF-8")

#f=codecs.open(name, 'r')
#print(f.read())

record = dict()
videoCount = 0

for lines in file:
    line = lines.encode("utf-8")
    line.split()
    print(line)
    
print("Done")