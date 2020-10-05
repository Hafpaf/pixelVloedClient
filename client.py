#!/usr/bin/python3
"""
This is an example client for Pixelvloed, a pixelFlut UDP server.

It does the following:
1. Choose a random RGB colour,
2. Assign next (x,y) coordinate to color.
3. Create list of packets
4. Choose random packet from the list
5. Send choosen packet

Based of https://github.com/JanKlopper/pixelvloed/
and  https://gitlab.com/pyjam.as/pixelvloet
"""

import socket
import random
from struct import pack

IP = "ipAddress"
PORT = 5005

# Specifies UDP usage
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Color box size
width, height = 500,500
# Color box offset
xoff, yoff = 0, 0
# Choose a color
pixelColor = (random.randint(0,255), # R
              random.randint(0,255), # G
              random.randint(0,255)) # B

def to_coord(num):
    return pack('BB', num & 0xFF, num >> 8)

def packet(x, y, r, g, b):
    result = bytes([0, 0])
    result += bytes([*to_coord(x), *to_coord(y), r, g, b])
    return result

def imagepacket(x, y):
    r, g, b = pixelColor
    result = packet(x + xoff, y + yoff, r, g, b)
    return result

packets = [imagepacket(x, y)
           for x in range(width)
           for y in range(height)]
random.shuffle(packets)

while True:
    for p in packets:
        sock.sendto(p, (IP, PORT))