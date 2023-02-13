link="https://youtu.be/Zv11L-ZfrSg"
# link="https://youtu.be/is38pqgbj6A"
from pytube import YouTube
a=YouTube(link)
data=a.streams
li=[]
# .filter(file_extension='mp4')
for i in data.filter(progressive=True):
    
    try:
            li.append({i.resolution:[i.itag,"p"]})
    except:
        pass

for i in data.filter(file_extension='mp4'):
    try:
        resol=i.resolution
        
        if resol:
            li.append({resol:[i.itag,"m"]})
    except:
        pass
bit={}
for z in data.filter(only_audio=True):
    bit[f"""{(z.abr).split("kbps")[0]}"""]=f"{z.itag}"
a=max(map(int, bit.keys()))
li.append({f"{a}":[f"{bit[str(a)]}","a"]})
unique=[]
index=0
keys=[]
for d in li:
    for z in d:
        
        if (d[z][1]=="p") :
            keys.append(z)
            unique.append(d)
    for key in d.keys():
        if key not in keys:
            keys.append(key)
            unique.append(d)
print(unique)

# stream=a.streams.get_by_itag(251)
# stream.download()

# streams=a.streams
# for i in streams:
#     print(i)
# resolutions = [stream.resolution for stream in streams if stream.resolution]
# itag = [stream.itag for stream in streams if stream.itag and stream.resolution]
# stream = a.streams.get_by_itag('480p')
# stream.download()
# print(itag)
# print(resolutions)
# for i in a.streams:
#     print(i.res)


#  First i need to check all the video that has both audio and video codec if the video has that then we can easily download the video else we have to try download the video and audio speerately and merge them
# stream.download()


