import time

import numpy
from serial import Serial

ser = Serial(port="COM3", baudrate=115200, timeout=.1)


def to_f32_le_bytes(f64):
    return numpy.float32(f64).tobytes()


def sendvector(vektor):
    print(vektor)
    if not ser.isOpen():
        ser.open()
    print(bytes(f'{-vektor[0]};{vektor[1]};0;\n', 'utf-8'))
    ser.write(bytes(f'{-vektor[0]};{vektor[1]};0;\n', 'utf-8'))


def sendstop():
    # Serial zerlegen und Header bauen
    if not ser.isOpen():
        ser.open()
    for i in range(0,4):
        print("Send stop")
        ser.write(bytes(';;1;\n', 'utf-8'))
        time.sleep(0.05)

def appendchecksum(data):
    checksum = 0
    for i, v in enumerate(data):
        checksum += v
    checksum %= 256
    data.append(checksum)
