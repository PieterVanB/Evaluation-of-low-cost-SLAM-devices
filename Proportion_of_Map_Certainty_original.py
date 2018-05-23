#!/usr/bin/env python
# inserting numpy library and matplotlib library
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

# FUNCTIONS
# Function create binary array with Threshold and return the array


def getBinary(data, Threshold):
    Array = np.array(data)
    Array[Array <= Threshold] = 1
    Array[Array > Threshold] = 0

    return(Array)

# function to plot the map


def showMap(data):
    cmap = colors.ListedColormap(['black', 'white'])
# size
    plt.subplot(111)
    plt.imshow(data, interpolation='nearest', origin='upper', cmap=cmap)
    plt.show()
    return

# function to calculate the proportion of occupied cells above the threshold to all occupied cells


def getProportion(BinaryMap_Threshold, BinaryMap_AllOccupied):
    x = BinaryMap_Threshold.sum()
    y = BinaryMap_AllOccupied.sum()
    Proportion = y/x
    return (Proportion)


# Read in array defining the name and the delimiter
image = cv2.imread(
    '/home/pieter/bagfiles/tango_bagfiles/gmap-up-Sat-May-19-19-52-32-2018-map.pgm')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print gray_image
np.savetxt('/home/pieter/cbagfiles/tango_bagfiles/gmap-up-Sat-May-19-19-52-32-2018-map1.txt',
           gray_image.astype(float), fmt='%i', delimiter=',')

data = np.loadtxt(
    "/home/pieter/bagfiles/tango_bagfiles/gmap-up-Sat-May-19-19-52-32-2018-map1.txt", dtype='float', delimiter=",")
# caltulate the mean of the array
# first delete all free and unknown space.

meandata = []
rows = data.shape[0]
cols = data.shape[1]
for x in range(0, cols):
    for y in range(0, rows):
        if data[y, x] < 127:
            meandata.append(data[y, x])
print(cols)
print(rows)



UndefinedSpace = 127
Occupancy_Thresh = UndefinedSpace - 1
mean = np.mean(meandata)

# round it up to an integer and show it
int_mean = float(round(mean))
print ('this is the mean', int_mean)
Threshold = int_mean
# Get two binary maps, one with use of the threshold, other with threshold = all accupied values
BinaryMap_Threshold = getBinary(data, Threshold)
x = BinaryMap_Threshold.sum()

BinaryMap_AllOccupied = getBinary(data, Occupancy_Thresh)
y = BinaryMap_AllOccupied.sum()

print(BinaryMap_AllOccupied)
# Get the proportion of cells above threshold to all occupied cels
Proportion = getProportion(BinaryMap_Threshold, BinaryMap_AllOccupied)
print('this is the proportion', Proportion)

# write binary file to file named 'out1'
with open('out1.txt', 'ab') as outfile:
    np.savetxt(outfile, BinaryMap_Threshold, "%i", delimiter=",")

showMap(BinaryMap_AllOccupied)
print "this is all occupied cells condidering unknown space unknown", y
showMap(BinaryMap_Threshold)
print "this the number of all occupied cells concidering the mean", x

