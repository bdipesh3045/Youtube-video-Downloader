from pytube import Playlist,YouTube
import time
class dowanloader:
    def __init__(self,link,method,d_type) -> None:
        self.link=link
        self.temp=YouTube(link)  
        self.stream=self.temp.streams
        self.method=method.lower()
        self.links=[]
        self.unique=[]
        self.d_type=d_type.lower()
        if method=="p":
            self.quality_resolver()
        print(self.unique)
        
        
    
    
    def quality_resolver(self):
        data=self.stream
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
    
        keys=[]
        for d in li:
            for z in d:
                
                if (d[z][1]=="p") :
                    keys.append(z)
                    self.unique.append(d)
            for key in d.keys():
                if key not in keys:
                    keys.append(key)
                    self.unique.append(d)
        
        self.quality=input("Enter the required pictures quality as 144p:")
    
    
    
        
    def link_breaker(self):
        p=Playlist(self.link)
        
        for url in p:
            self.links.append(url)
        if self.d_type=="v":
            self.down()
            
    def down(self):
        counter=1
        for i in self.links:
            if counter==16 :
                yt=YouTube(i)
                try:
                    stream=yt.streams.get_by_itag(22)
                    stream.download()
                except:
                    print(f"Video not downloaded:{i}")
                
                time.sleep(10)
            print(f"{counter} Video downloaded")
            counter+=1
            
            # for a in yt.streams:
            #     print(a)
            # print("-----------------------------")  
# I will add the quality download option with highest possiblie quality with threading  
# "137" mime_type="video/mp4" res="1080p"
        
start=dowanloader("https://www.youtube.com/watch?v=ve_0h4Y8nuI&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t","p","v")
