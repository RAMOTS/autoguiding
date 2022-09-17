# common information
import cv2

filepath = cv2.CAP_DSHOW  # 'IMGP6756.MOV'#'X:/Astrofotos Rohdaten/2022-05-15 Dreifach ISS/2022-05-15-0121_6-CapObj.AVI'#
windowsize = (960, 540)

versionname = 'RAMOTS Autotracking V1'
scanMethod = 0  # 0 = Contrastlines
targetPoint = [0.5, 0.5]  # From where does my Vector start?
viewpos = [0.5, 0.5]
viewsize = 0.2
parameterchange = 0.01
controlling = False

send_interval = 0.2  # datavector sending time in sec

# Proportionalregler
interval = 0.2
PID_P = 0.15
PID_I = 0.05
PID_D = 0.2
