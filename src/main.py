#import pafy
import json
#import urllib
import urllib.request

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
        #try:
            if 'href="https://www.youtube.com/watch' in x:
                #index = x.find('=')
                index = x.find('?')
                end = x.find('>')
                videoID = x[index:end-1]
                #url = x[index+2:end-1]
                
                api_key = "AIzaSyAihjjJLtRW9D06B9OTYlSVNp_QYvqB9qQ"
                searchUrl = "https://www.googleapis.com/youtube/v3/videos?id=" + videoID + "&key=" + api_key + "&part=contentDetails"
                response = urllib.request.urlopen(searchUrl)
                data = json.loads(response)
                all_data = data['items']
                contentDetails = all_data[0]['contentDetails']
                duration = contentDetails['duration']
                print(duration)
                
                '''video = pafy.new(url)
                #fileGenerated.write(x + "\n")
                fileGenerated.write(video.length + "\n")'''
                videoCount = videoCount + 1
                videoProcessed = videoProcessed + 1
                print("Video", videoProcessed, "out of", totalVideos, "videos processed")
        #except:
        #    #print("Nope")
        #    videoSkipped = videoSkipped + 1
        #    videoProcessed = videoProcessed + 1
        #    print("Video", videoProcessed, "out of", totalVideos, "videos processed")
    
    
print("Videos counted:", videoCount)
print("Videos skipped:", videoSkipped)

fileGenerated.close()
