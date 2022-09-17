'''import random
import time

from serial import Serial
from serial_handling import to_f32_le_bytes, appendchecksum

# Serial takes these two parameters: serial device and baudrate
ser = Serial(port="COM4", baudrate=115200, timeout=.1)

if not ser.isOpen():
    print("Opening port")
    ser.open()


def send_once():
    vektor = [1.0, 1.0]

    datavector = bytearray()
    datavector.append(85)  # Startbyte
    datavector.append(66)  # Src Dest (Von Computer an Motorsteuerung)
    datavector.append(101)
    datavector.append(to_f32_le_bytes(vektor[0])[0])
    datavector.append(to_f32_le_bytes(vektor[0])[1])
    datavector.append(to_f32_le_bytes(vektor[0])[2])
    datavector.append(to_f32_le_bytes(vektor[0])[3])
    datavector.append(to_f32_le_bytes(vektor[1])[3])
    datavector.append(to_f32_le_bytes(vektor[1])[2])
    datavector.append(to_f32_le_bytes(vektor[1])[1])
    datavector.append(to_f32_le_bytes(vektor[1])[0])
    appendchecksum(datavector)

    print(ser.write(datavector), "bytes sent")
    print(datavector)


def test_random():
    rng = random.Random(1)
    while True:
        datavector = bytearray()
        datavector.append(85)  # Startbyte
        datavector.append(66)  # Src Dest (Von Computer an Motorsteuerun
        datavector.append(101)

        bytes = bytearray(rng.getrandbits(8) for _ in range(0, 8))
        #print(bytes[0], bytes[1], bytes[2], bytes[3], bytes[4], bytes[5], bytes[6], bytes[7])
        for b in bytes:
            datavector.append(b)

        print(datavector)

        appendchecksum(datavector)
        ser.write(datavector)
        time.sleep(0.1)


while True:
    send_once()
    time.sleep(0.1)'''
