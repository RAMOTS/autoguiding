import cv2

def getBrightest(frame, showboxes=True, color=(0, 0, 255)):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    r = 49
    gray = cv2.GaussianBlur(gray, r, r, 0)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    return (maxLoc)
