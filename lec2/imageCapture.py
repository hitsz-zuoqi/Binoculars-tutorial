import cv2
import imutils
import time
from imutils.video import VideoStream
print("Camera Sensor Warming Up in 2 seconds!")
New_VideoStream = VideoStream(src=1,resolution=(1280,480),usePiCamera=False,framerate=60).start()
time.sleep(2.0)
pic_idx = 0
print("type c to capture picture and q to quit!")
while True:
    New_frame = New_VideoStream.read()
    key = cv2.waitKey(1) & 0xFF
    # quit 
    if key == ord("q"):
        break
    # capture frame 
    if key == ord('c'):
        New_frame_left = New_frame[:,640:1280]
        New_frame_right = New_frame[:,0:640]
        cv2.imwrite("CalibIMG/left/left{}.jpg".format(pic_idx),New_frame_left)
        cv2.imwrite("CalibIMG/right/right{}.jpg".format(pic_idx),New_frame_right)
        pic_idx +=1
        print("Please capture the {}th image!".format(pic_idx))
    cv2.imshow("frame",New_frame)

cv2.destroyAllWindows()
New_VideoStream.stop()

    




