#!/usr/bin/env python2
# inserting numpy library and matplotlib library
from __future__ import division
import numpy as np
import scipy as sp
import scipy.ndimage as nd
import matplotlib.pyplot as plt
from matplotlib import colors
import cv2


# Read in array defining the name and the delimiter
image = cv2.imread(
    '/home/pieter/catkin_ws/src/thesis/src/Tue-May-22-18-43-12-2018-map.pgm')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print gray_image
np.savetxt('/home/pieter/catkin_ws/src/thesis/src/Tue-May-22-18-43-12-2018-map.txt',
           gray_image.astype(int), fmt='%i', delimiter=',')

data = np.loadtxt(
    "/home/pieter/catkin_ws/src/thesis/src/Tue-May-22-18-43-12-2018-map.txt", dtype='int', delimiter=",")
# Read in array defining the name and the delimiter

rows = data.shape[0]
colums = data.shape[1]

# Getting the highest value within the map = 'absolute' certainty
Occupied = 0
UnOccupied = 254
print(Occupied)

# unknown space is usually the mean between occupied and unoccupied space
Unknown = 127
print(Unknown)

# Map all uncertain values to occupied values
data[data == Unknown] = Occupied

# Use Otsu binarysation
# convert array to uint8 to use Otsu's binarization
Otsu_data = np.array(data, dtype=np.uint8)

# Otsu's Binarysation returns retVal = optimal threshold Thresh_array = array after binaryzation
retVal, Thresh_array = cv2.threshold(
    Otsu_data, 0, 254, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# print 'Otsu treshold for binarization', retVal

# functie cv2.FindContours gebruikt suzuki's algorithm volgens opencv.org
im2, contours, hierarchy = cv2.findContours(
    Thresh_array, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Het aantal contours tellen. contours bestaat uit een verzameling van vectoren
i = 0	
for elem in contours:
    print(elem)
    i = i+1


print 'number of contours= ', i

#im2 = cv2.drawContours(im2,contours,-1,(0,255,0), 3)
img1 = image.copy()
cnt = contours[1]
cv2.drawContours(img1, contours, -1, (0, 255, 0), 3)
img1 = cv2.resize(img1, (1274, 875))
cv2.imshow('img', img1)

keyVal = cv2.waitKey(0)
if(keyVal == ord('a')):
    exit()
