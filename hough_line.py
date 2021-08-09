# coding=utf-8
import cv2 
import numpy as np 
  

img = cv2.imread('./input/raw_img.jpg') 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

edges = cv2.Canny(gray, 50, 200,apertureSize = 3) 

lines = cv2.HoughLines(edges, 1, np.pi/180, 300) 

line_len = 1000
for i in range(len(lines)):
    r,theta = lines[i, 0, 0], lines[i, 0, 1]
    a = np.cos(theta)
    b = np.sin(theta) 
    x0 = a*r  
    y0 = b*r  
    x1 = int(x0 + line_len*(-b)) 
    y1 = int(y0 + line_len*(a)) 
    x2 = int(x0 - line_len*(-b)) 
    y2 = int(y0 - line_len*(a))  
    cv2.line(img,(x1,y1), (x2,y2), (0,255,0),2) 

cv2.imwrite('./output/hough_line.jpg', img) 
cv2.imshow("result", img)
cv2.waitKey(0)
