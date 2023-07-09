import cv2, pafy

ds_factor=1
class VideoCamera(object):
    
    
    def __init__(self, url):
       #url   = "https://www.youtube.com/watch?v=2fmkmp-_KH0"

       self.pafyObj = pafy.new(url)
       streams = self.pafyObj.allstreams
       bestVideo  = self.pafyObj.getbestvideo()
       print(bestVideo)
       #best.resolution, best.extension
       

       #capture = cv2.VideoCapture(best.url)
       #check, frame = capture.read()

       self.video = cv2.VideoCapture(bestVideo.url)
       self.bestaudio = self.pafyObj.getbestaudio()
    
    def __del__(self):
        #releasing camera
        self.pafyObj.release()
    
    def get_frame(self):
       #extracting frames
        ret, frame = self.video.read()
        frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor,
        interpolation=cv2.INTER_AREA)
        cv2.waitkey(10)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
        
    #def get_audio(self):
    #    play_url = self.bestaudio.url
    #   return play_url