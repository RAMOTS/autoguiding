import cv2
import helperfunctions as hf


def get_average(frame, boxes):
    sy, sx, h = frame.shape
    xmax = 0
    xmin = sx
    ymax = 0
    ymin = sy
    for box in boxes:
        x, y, w, h = box
        if x < xmin:
            xmin = x
        if x + w > xmax:
            xmax = x + w
        if y < ymin:
            ymin = y
        if y + h > ymax:
            ymax = y + h
    x = int((xmin + xmax) / 2)
    y = int((ymin + ymax) / 2)
    x /= sx
    y /= sy
    return [x, y]


def get_average_bad(boxes: []):
    count = 0
    average_x = 0
    average_y = 0
    for box in boxes:
        x, y, w, h = box
        center_x = (x + w) / 2
        center_y = (y + h) / 2
        average_x = average_x + 1 / (count + 1) * (center_x - average_x)
        average_y = average_y + 1 / (count + 1) * (center_y - average_y)
        count += 1
    return [average_x, average_y]


def getvector(frame, showboxes=True, color=(0, 0, 255)):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 20)
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    boxes = []
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        if y < 479 and x < 640 and w > 10 and h > 10:
            boxes.append(cv2.boundingRect(c))
            if showboxes:
                cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 0, 255))
    return get_average(frame, boxes)
