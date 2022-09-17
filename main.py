import config as cfg
import contrastlines as cl
import helperfunctions as hf
import cv2
import stereoPID as sp
import serial_handling as se
import time


def playvideo(filepath):

    #Video vorbereiten
    cap = cv2.VideoCapture(filepath)

    #Fenster benennen
    cv2.namedWindow(cfg.versionname, cv2.WINDOW_AUTOSIZE)

    last_sent_time = time.time()

    #Frame für Frame durchgehen
    while hf.checkkeyboard():
        ret_val, frame = cap.read()
        #print(frame.shape)

        #Objektposition finden nach Algo
        posobj = cfg.targetPoint
        if cfg.scanMethod == 0:
            posobj = cl.getvector(frame, showboxes=True)

        #Overlays machen
        hf.drawline(frame, posobj, cfg.targetPoint)
        hf.drawrectangle(frame, cfg.viewpos, cfg.viewsize)

        #PID Regler einsetzten und anzeigen
        correct = sp.calculatePID(posobj, cfg.targetPoint)
        hf.drawline(frame, (correct[0] + cfg.targetPoint[0], correct[1] + cfg.targetPoint[1]), cfg.targetPoint, color=(255, 0, 0))

        #Seriell senden
        if cfg.controlling:
            hf.drawrectangle(frame, (0.5, 0.5), 1, width=40, color=(0, 0, 255))

            if time.time() - last_sent_time > cfg.send_interval:
                last_sent_time = time.time()
                #Serial senden
                se.sendvector(correct)

        #Ausgabe machen
        output = cv2.resize(frame, cfg.windowsize)
        cv2.imshow(cfg.versionname, output)

    cv2.destroyAllWindows()


def main():
    playvideo(cfg.filepath)


if __name__ == '__main__':
    main()
