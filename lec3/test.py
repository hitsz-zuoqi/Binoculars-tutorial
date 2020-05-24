# Test.py
from Triangulation import triangulation
from Calib import USB_Camera
import cv2
import numpy as np
# 标定摄像头，config类保存参数
config = USB_Camera()
Roi_points_right = [
[164.0, 634.0],
[257.0, 602.0],
[351.0, 524.0],
[413.0, 446.0],
[460.0, 383.0],
[117.0, 430.0],
[117.0, 336.0],
[117.0, 273.0],
[117.0, 211.0],
[179.0, 414.0],
[194.0, 273.0],
[210.0, 195.0],
[226.0, 148.0],
[241.0, 399.0],
[272.0, 258.0],
[289.0, 180.0],
[319.0, 133.0],
[304.0, 414.0],
[350.0, 304.0],
[367.0, 242.0],
[397.0, 180.0]
]
Roi_points_left = [
[351.0, 649.0],
[445.0, 618.0],
[538.0, 555.0],
[600.0, 477.0],
[647.0, 399.0],
[304.0, 446.0],
[288.0, 351.0],
[288.0, 289.0],
[289.0, 242.0],
[366.0, 430.0],
[366.0, 289.0],
[382.0, 226.0],
[398.0, 164.0],
[414.0, 414.0],
[444.0, 273.0],
[460.0, 211.0],
[476.0, 148.0],
[476.0, 430.0],
[523.0, 320.0],
[553.0, 258.0],
[569.0, 211.0]
]
pts_3d = triangulation(Roi_points_left,Roi_points_right,config.R,config.T,config.cam_matrix_left,config.cam_matrix_right,21)
pts_3d_norm=np.linalg.norm(pts_3d, axis=1, keepdims=True)

for i in range(21):
  dist = pts_3d_norm[i][0]/1000
  print("distance of point {} is {:.4f}m".format(i,dist))