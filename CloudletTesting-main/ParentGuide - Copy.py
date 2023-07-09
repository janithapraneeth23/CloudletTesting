import sys
from camera import VideoCamera
import cv2
import features
import timeit
import os

#sys.stdout = open('FPS_ads.log', 'w')
startUp=1
ds_factor=1
start_time_s = cv2.getTickCount()

class ParentGuide(VideoCamera):  
    def __init__(self, url):
        path = os.getcwd()
           #https://www.youtube.com/watch?v=2fmkmp-_KH0
        print(path)
        img = cv2.imread('C:\\Personal\\Msc\\Project\\server\\server\\src\\main\\java\\com\\janitha\\videoenhancer\\client\\external\\cloudletPlugins\\logo_train.png')
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
            # self.frame_number += 1
            # if not self.frame_number % 100:
            #     self.scan_fps = 1 / ((timeit.default_timer() - self.cur_time) / 100)
            #     self.cur_time = timeit.default_timer()
            #     print("FPS:", self.scan_fps)
                
            end_time =  cv2.getTickCount()
            total_time = (end_time - start_time) / cv2.getTickFrequency()
            fps = frame_count / total_time
            sys.stdout.write("FPS : {}\n".format(fps))
            font_face = cv2.FONT_HERSHEY_SIMPLEX
            scale = 3
            color = (0, 0, 0)
            thickness = cv2.FILLED
            text = "Hello From Cloudlet"
            txt_size = cv2.getTextSize(text, font_face, scale, thickness)
            
            
            frame=cv2.resize(frame,None,fx=ds_factor,fy=ds_factor,
            interpolation=cv2.INTER_AREA)
            pos = (100,100)
            bg_color = (255,0,0)
            margin = 2
            
            end_x = pos[0] + txt_size[0][0] + margin
            end_y = pos[1] - txt_size[0][1] - margin
            
            cv2.rectangle(frame, pos, (end_x, end_y), bg_color, thickness)
            cv2.putText(frame, text, pos, font_face, scale, color, 1, cv2.LINE_AA)
        
    #         region = features.detectFeatures(frame, self.train_features)
    
    
    #         if region is not None:
    #             temp = cv2.resize(frame, (w, h), interpolation=cv2.INTER_LINEAR)
    
    # # Initialize output image
    #             output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    
    #             #id_kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    #             #blur_img2 = cv2.GaussianBlur(frame, (45, 45), 1000)
    #             #blur_img = cv2.GaussianBlur(blur_img2, (45, 45), 1000)
    #             cv2.imshow("Video", output)
    #             cv2.waitKey(1)
    #             continue
    
    #             box = cv2.boxPoints(region)
    #             #box = np.int0(box)
    #             cv2.drawContours(frame, [box], 0, (0, 255, 0), 2)
    

            #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imshow("Video", frame)
            global startUp
            if startUp:
                end_time_s =  cv2.getTickCount()
                total_time_s = (end_time_s - start_time_s) / cv2.getTickFrequency()
                print("start up time:", total_time_s)
                startUp = 0
                break
            cv2.waitKey(1)

            
        sys.stdout.close()
        self.video.release()

        
      

    
    def get_audio(self):
        play_url = self.bestaudio.url
        return play_url
    


# n = len(sys.argv)
# host = sys.argv[1]
# port = sys.argv[2]
# cloudletPort = sys.argv[3]
URL =  'https://www.youtube.com/watch?v=nIClYOTYluA'
#URL = 'https://www.youtube.com/watch?v=cQPz3FfpEK0' 
#sys.argv[4]


# print("\n", host, " ", port, " ", URL)

originalCamera = ParentGuide(URL)

originalCamera.get_frame()



print('End Succefully')
