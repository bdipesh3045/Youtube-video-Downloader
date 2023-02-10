link="https://youtu.be/Zv11L-ZfrSg"
link="https://youtu.be/is38pqgbj6A"
from pytube import YouTube
a=YouTube(link)
data=a.streams
# .filter(file_extension='mp4')
for i in data.filter(progressive=True):
    
    try:
        
            print(f"{i.itag}:{i.resolution}")
    except:
        pass
print("  ")
for i in data.filter(file_extension='mp4'):
    try:
        resol=i.resolution
        
        if resol:
            print(f"{i.itag}:{resol}")
    except:
        pass
bit={}
for z in data.filter(only_audio=True):
    bit[f"""{(z.abr).split("kbps")[0]}"""]=f"{z.itag}"
a=max(map(int, bit.keys()))
print({f"{a}":f"{bit[str(a)]}"})


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


