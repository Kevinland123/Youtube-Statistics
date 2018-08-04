import pafy

print("Alright we got this!")

name = input("Enter file:")
if len(name) < 1 : 
    name = "history2.html"

fileRead = open(name, encoding="UTF-8")
fileGenerated = open('ListOfVideo.txt', 'w')

record = dict()

videoCount = 0
videoSkipped = 0
videoProcessed = 0

for lines in fileRead:
    line = lines.encode("utf-8")
    new = line.decode().split()
    totalVideos = len(new)
    for x in new:
        try:
            if 'href="https://www.youtube.com/watch' in x:
                index = x.find('=')
                end = x.find('>')
                url = x[index+2:end-1]
                
                video = pafy.new(url)
                #print video.length
                
                #fileGenerated.write(x + "\n")
                fileGenerated.write(video.length + "\n")
                videoCount = videoCount + 1
                videoProcessed = videoProcessed + 1
                print("Video", videoProcessed, "out of", totalVideos, "videos processed")
        except:
            #print("Nope")
            videoSkipped = videoSkipped + 1
            videoProcessed = videoProcessed + 1
            print("Video", videoProcessed, "out of", totalVideos, "videos processed")
    
    
print("Videos counted:", videoCount)
print("Videos skipped:", videoSkipped)

fileGenerated.close()