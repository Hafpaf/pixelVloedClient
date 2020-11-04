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

IP = "10.42.1.12"
PORT = 5005

# Specifies UDP usage
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Color box size
width, height = 200,200

# Color box offset
xoff, yoff = 0, 0

# ----------
# Start here
# ----------
def pixelColor():
    return (random.randint(0,255), # R
            random.randint(0,255), # G
            random.randint(0,255)) # B
choosenColor = pixelColor()

# -----------------
# Protocol 0  logic
# -----------------
def to_coord(num):
    return pack('BB', num & 0xFF, num >> 8)

pixel_count = 0
current_packet = None

def new_packet():
    global current_packet 
    global pixel_count
    current_packet = bytes([0, 0]) #protocol header
    pixel_count = 0
new_packet()

def finish_packet(packets):
    if pixel_count > 0:
        packets.append(current_packet)
        new_packet()

def set_pixel_raw(packets, x, y, r, g, b):
    global current_packet 
    global pixel_count
    current_packet += bytes([*to_coord(x), *to_coord(y), r, g, b])
    pixel_count +=1
    if pixel_count >= 160: #160 is max pixel/packet
        finish_packet(packets)

def set_pixel(packets, x, y, c):
    r, g, b = c[0], c[1], c[2]
    set_pixel_raw(packets, x + xoff, y + yoff, r, g, b)

def build_img(packets):
    for x in range(width):
        for y in range(height):
            #cpixel = pixels[x, y]
            set_pixel(packets, x, y, choosenColor)
    finish_packet(packets)

print("Build have finished, starting to send UDP")
while True:
    packets=[]
    build_img(packets)
    # makes really nice fading effect:
    random.shuffle(packets)
    for n in range(1,25):
        #print(n)
        for p in packets:
            sock.sendto(p, (IP, PORT))
    xoff += 100
    yoff += 100
    xmax = xoff+width
    ymax = yoff+height
    if xmax > 1600:
        xoff = 0
    if ymax > 1200:
        yoff = 0
