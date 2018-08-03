print("Alright we got this!")
# import codecs

name = input("Enter file:")
if len(name) < 1 : 
    name = "history3.html"

fileRead = open(name, encoding="UTF-8")
fileGenerated = open('ListOfVideo.txt', 'w')

record = dict()
videoCount = 0
videoSkipped = 0

for lines in fileRead:
    line = lines.encode("utf-8")
    new = line.decode().split()
    for x in new:
        try:
            if 'href="https://www.youtube.com/watch' in x:
                # print(x.encode("utf-8"))
                # fileGenerated.write(x.encode("utf-8"))
                fileGenerated.write(x + "\n")
                videoCount = videoCount + 1
        except:
            #print("Nope")
            videoSkipped = videoSkipped + 1
print("Videos counted:", videoCount)
print("Videos skipped:", videoSkipped)

fileGenerated.close()