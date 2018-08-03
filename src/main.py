print("Alright we got this!")
#import codecs

name = input("Enter file:")
if len(name) < 1 : 
    name = "history3.html"

file = open(name, encoding="UTF-8")

#f=codecs.open(name, 'r')
#print(f.read())

record = dict()
videoCount = 0

for lines in file:
    line = lines.encode("utf-8")
    new = line.decode().split()
    for x in new:
        if 'href="https://www.youtube.com/watch' in x:
            print(x.encode("utf-8"))
            videoCount = videoCount + 1
print(videoCount)