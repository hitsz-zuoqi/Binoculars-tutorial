# Triangulation.py
import cv2
import numpy as np
from Calib import USB_Camera

def triangulation(pointl_vec,pointr_vec,R,t,cam_matrix_left,cam_matrix_right,n):
    pointl_cam_vec = []
    pointr_cam_vec = []
    for pointl in pointl_vec:
        pointl_cam_vec.append([(pointl[0] - cam_matrix_left[0, 2]) / cam_matrix_left[0, 0],(pointl[1] - cam_matrix_left[1, 2]) / cam_matrix_left[1, 1]])
    for pointr in pointr_vec:
        pointr_cam_vec.append([(pointr[0] - cam_matrix_right[0, 2]) / cam_matrix_right[0, 0],(pointr[1] - cam_matrix_right[1, 2]) / cam_matrix_right[1, 1]])
    T1 = np.array([[1.,0.,0.,0.],[0.,1.,0.,0.],[0.,0.,1.,0.]])
    T2 = np.concatenate((R,t),axis=1)
    # print(T1,T2)
    pointl_cam_vec = np.array(pointl_cam_vec).transpose()
    pointr_cam_vec = np.array(pointr_cam_vec).transpose()
    # print(pointl_cam_vec)
    # print(pointr_cam_vec)

    pts_4d = np.zeros((4,n))
    cv2.triangulatePoints(T1,T2,pointl_cam_vec,pointr_cam_vec,pts_4d)
    pts_3d = []
    for i in range(n):
        x = pts_4d[0,i]/pts_4d[3,i]
        y = pts_4d[1,i]/pts_4d[3,i]
        z = pts_4d[2,i]/pts_4d[3,i]
        pts_3d.append([x,y,z])
    pts_3d = np.array(pts_3d)

    return pts_3d