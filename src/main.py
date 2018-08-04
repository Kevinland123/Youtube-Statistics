import json
import isodate
import datetime
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

totalTimeSeconds = 0

for lines in fileRead:
    line = lines.encode("utf-8")
    new = line.decode().split()
    totalVideos = len(new)
    for x in new:
        try:
            if 'href="https://www.youtube.com/watch' in x:
                index = x.find('?')
                end = x.find('>')
                videoID = x[index+3:end-1]
                
                api_key = "AIzaSyCAExHHkEP_iB9RYmHXlaXC-pjPkj9RWQw"
                searchUrl = "https://www.googleapis.com/youtube/v3/videos?id=" + videoID + "&key=" + api_key + "&part=contentDetails"
                response = urllib.request.urlopen(searchUrl)
                bla = response.read()
                encoding = response.info().get_content_charset('utf-8')
                data = json.loads(bla.decode(encoding))
                all_data = data['items']
                contentDetails = all_data[0]['contentDetails']
                duration = contentDetails['duration']
                
                duration = isodate.parse_duration(duration)
                durationseconds = duration.total_seconds()
                video_dur = str(datetime.timedelta(seconds=durationseconds))
                print(video_dur)
                
                totalTimeSeconds = totalTimeSeconds + durationseconds
                
                videoCount = videoCount + 1
                videoProcessed = videoProcessed + 1
                print("Video", videoProcessed, "out of", totalVideos, "videos processed")
        except:
            print("Nope")
            videoSkipped = videoSkipped + 1
            videoProcessed = videoProcessed + 1
            print("Video", videoProcessed, "out of", totalVideos, "videos processed")
    
print("Videos counted:", videoCount)
print("Videos skipped:", videoSkipped)

totalTime = str(datetime.timedelta(seconds=totalTimeSeconds))
print(totalTime)

fileGenerated.close()
