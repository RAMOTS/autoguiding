import config as cfg
import cv2
import serial_handling as se


# Returns true until esc pressed
def checkkeyboard():
    # Tastendrucke abfangen
    k = cv2.waitKey(2)
    if k == 27:  # Esc key to stop
        return False
    elif k == 119:  # w
        cfg.targetPoint[1] -= cfg.parameterchange
    elif k == 115:  # s
        cfg.targetPoint[1] += cfg.parameterchange
    elif k == 97:  # a
        cfg.targetPoint[0] -= cfg.parameterchange
    elif k == 100:  # d
        cfg.targetPoint[0] += cfg.parameterchange
    elif k == 43:  # +
        cfg.viewsize += cfg.parameterchange
    elif k == 45:  # -
        cfg.viewsize -= cfg.parameterchange
    elif k == 114:  # r
        cfg.targetPoint = [0.5, 0.5]
    elif k == 32:  # space
        if cfg.controlling:
            se.sendstop()
        cfg.controlling = not cfg.controlling
    # else:
    # print(k)
    # Werte limitieren
    if cfg.viewsize < 0:
        cfg.viewsize = 0
    if cfg.viewsize > 1:
        cfg.viewsize = 1
    if cfg.targetPoint[0] < 0:
        cfg.targetPoint[0] = 0
    if cfg.targetPoint[0] > 1:
        cfg.targetPoint[0] = 1
    if cfg.targetPoint[1] < 0:
        cfg.targetPoint[1] = 0
    if cfg.targetPoint[1] > 1:
        cfg.targetPoint[1] = 1
    return True


def drawline(frame, pt1, pt2, color=(0, 0, 255), width=2):
    sy, sx, h = frame.shape
    cv2.line(frame, (int(pt1[0] * sx), int(pt1[1] * sy)), (int(pt2[0] * sx), int(pt2[1] * sy)), color, width)


def drawrectangle(frame, pt, size, color=(0, 255, 0), width=2):
    sy, sx, h = frame.shape
    pt1 = (int((pt[0] - (size / 2)) * sx), int((pt[1] - (size / 2)) * sy))
    pt2 = (int((pt[0] + (size / 2)) * sx), int((pt[1] + (size / 2)) * sy))
    cv2.rectangle(frame, pt1, pt2, color, width)
