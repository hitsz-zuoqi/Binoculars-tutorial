from imutils.video import VideoStream
import cv2
import time

vs = VideoStream(src=0, usePiCamera=False, resolution=(1280, 480),
		framerate=60).start()
time.sleep(2.0)

while True:
    frame = vs.read()
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
		

cv2.destroyAllWindows()