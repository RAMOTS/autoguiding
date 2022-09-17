import contrastlines
import brightestDot
import config

def getTarget(frame):
    if config.scanMethod == 0:
            return contrastlines.getvector(frame)
    elif config.scanMethod == 1:
            return brightestDot.getBrightest(frame)
    else:
            return config.targetPoint

