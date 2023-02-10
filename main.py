from pytube import Playlist,YouTube
import time
class dowanloader:
    def __init__(self,link,method,d_type,quality) -> None:
        self.link=link
        self.method=method.lower()
        self.links=[]
        self.d_type=d_type.lower()
        self.quality=quality
        if method=="p":
            self.link_breaker()
    
    def quality_resolver(self):
        pass
        
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
