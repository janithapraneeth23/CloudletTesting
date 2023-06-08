import sys
from camera import VideoCamera
import cv2
import features
import timeit
import os

ds_factor=1
class ParentGuide(VideoCamera):  
    def __init__(self, url):
        path = os.getcwd()
           #https://www.youtube.com/watch?v=2fmkmp-_KH0
        print(path)
        img = cv2.imread('C:\\Users\\janitha\\IdeaProjects\\finalYearProject_Cloudlet\\src\\main\\java\\com\\janitha\\videoenhancer\\client\\external\\cloudletPlugins\\logo_train.png')
        self.train_features = features.getFeatures(img)
        self.cur_time = timeit.default_timer()
        self.frame_number = 0
        self.scan_fps = 0
        super().__init__(url)

    
    def get_frame(self):
        frame_count = 0
        start_time = cv2.getTickCount()
        while self.video.isOpened():
            ret, frame = self.video.read()
            if not ret:
                break
            frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor,
            interpolation=cv2.INTER_AREA)
            height, width = frame.shape[:2]
            w, h = (16, 16)
            
            frame_count += 1
            self.frame_number += 1
            if not self.frame_number % 100:
                self.scan_fps = 1 / ((timeit.default_timer() - self.cur_time) / 100)
                self.cur_time = timeit.default_timer()
    
            region = features.detectFeatures(frame, self.train_features)
    
            cv2.putText(frame, f'FPS {self.scan_fps:.3f}', org=(0, 50),
                        fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        fontScale=1, color=(0, 0, 255))
    
            if region is not None:
                temp = cv2.resize(frame, (w, h), interpolation=cv2.INTER_LINEAR)
    
    # Initialize output image
                output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    
                #id_kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
                #blur_img2 = cv2.GaussianBlur(frame, (45, 45), 1000)
                #blur_img = cv2.GaussianBlur(blur_img2, (45, 45), 1000)
                cv2.imshow("Video", output)
                cv2.waitKey(1)
                continue
    
                #box = cv2.boxPoints(region)
                #box = np.int0(box)
                #cv2.drawContours(frame, [box], 0, (0, 255, 0), 2)
    
            end_time =  cv2.getTickCount()
            total_time = (end_time - start_time) / cv2.getTickFrequency()
            fps = frame_count / total_time
            print("FPS:", fps)
            #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow("Video", frame)
            cv2.waitKey(1)

            
            
        self.video.release()

        
      

    
    def get_audio(self):
        play_url = self.bestaudio.url
        return play_url
    


# n = len(sys.argv)
# host = sys.argv[1]
# port = sys.argv[2]
# cloudletPort = sys.argv[3]
URL = 'https://www.youtube.com/watch?v=cQPz3FfpEK0' 
#sys.argv[4]


# print("\n", host, " ", port, " ", URL)

originalCamera = ParentGuide(URL)

originalCamera.get_frame()



print('End Succefully')
