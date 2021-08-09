# coding=utf-8
import cv2
import numpy as np

img0 = cv2.imread("./input/indoor.jpeg")
img = cv2.cvtColor(img0,cv2.COLOR_BGR2GRAY)

fld = cv2.ximgproc.createFastLineDetector()
dlines = fld.detect(img)

for dline in dlines:
    x0 = int(round(dline[0][0]))
    y0 = int(round(dline[0][1]))
    x1 = int(round(dline[0][2]))
    y1 = int(round(dline[0][3]))
    cv2.line(img0, (x0, y0), (x1,y1), (0,255,0), 1, cv2.LINE_AA)

cv2.imwrite('./output/fld_indoor.jpg', img0)
cv2.imshow("FLD", img0)
cv2.waitKey(0)
cv2.destroyAllWindows()
