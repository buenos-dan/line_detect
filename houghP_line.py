# coding=utf-8
import cv2 
import numpy as np 
  
img = cv2.imread('./input/raw_img.jpg') 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

edges = cv2.Canny(gray,50,200,apertureSize = 3) 

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, 50, 10) 


for i in range(len(lines)): 
	cv2.line(img,(lines[i, 0, 0],lines[i, 0, 1]), (lines[i, 0, 2],lines[i, 0, 3]), (0,255,0), 1) 

cv2.imwrite('./output/houghP_line.jpg', img) 
cv2.imshow("result", img)
cv2.waitKey(0)
