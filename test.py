#!/usr/bin/env python

import serial

with serial.Serial('/dev/ttyACM0', timeout=0.5) as psu:
    print("Opened port on {}".format(psu.name))
    print("Querying device")
    psu.write(b'*IDN?')
    print(psu.readline())
    print()

    print("Current Setting:")
    psu.write(b'ISET1?')
    print(psu.readline())

    print("Setting Current limit to 0.5A")
    psu.write(b'ISET1:0.5')
    # seems you to need to read a byte before sending the next command
    psu.read()

    print("New Current Setting:")
    psu.write(b'ISET1?')
    print(psu.readline())
    print()

    print("Voltage Setting:")
    psu.write(b'VSET1?')
    print(psu.readline())

    print("Setting Voltage to 5.00V")
    psu.write(b'VSET1:5.00')
    psu.read()

    print("New Voltage Setting:")
    psu.write(b'VSET1?')
    print(psu.readline())
    print()

    print("Output ON")
    psu.write(b'OUT1')
    psu.read()

    print("Output OFF")
    psu.write(b'OUT0')
    psu.read()
