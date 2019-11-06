import json
import urllib.request
user = input("Enter the track name")
e = urllib.request.urlopen("http://api.musixmatch.com/ws/1.1/track.search?apikey=b98ea5676353047750c0ea8d35995f96&q_track="+user+"&page_size=20")
y = e.read().decode("utf-8")
di = json.loads(y)
track_list = di["message"]["body"]["track_list"]
#print(track_list)
for i in track_list:
    print(i["track"]["track_name"])
