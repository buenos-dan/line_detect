import cv2
from pylsd2 import LineSegmentDetection, LineSegmentDetectionED

fullName, out_path = './input/raw_img.jpg', './output/edlines.jpg'

src = cv2.imread(fullName, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# input single channel image
lines = LineSegmentDetectionED(gray)

for l in lines:
    pt1, pt2 = tuple(l[:2]), tuple(l[2:4])
    cv2.line(src, pt1, pt2, (0, 255, 0), 1)
cv2.imshow("edlines", src)
cv2.waitKey(0)
cv2.imwrite(out_path, src)
