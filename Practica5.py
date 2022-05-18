import numpy as np
from matplotlib import pyplot as plt
import cv2 #opencv
import os
from math import sqrt
import imutils

imagen1=cv2.imread('Prueba.png')
retval, paso1= cv2.threshold(imagen1, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('original',imagen1)
cv2.imshow('threshold',paso1)
cv2.waitKey(0)
cv2.destroyAllWindows()


imagen2 = cv2.imread('Prueba.png',cv2.IMREAD_GRAYSCALE)
retval, paso2= cv2.threshold(imagen2, 32, 255, cv2.THRESH_BINARY)
cv2.imshow('original',imagen2)
cv2.imshow('threshold',paso2)
cv2.waitKey(0)
cv2.destroyAllWindows()

th = cv2.adaptiveThreshold(imagen2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('original',imagen1)
cv2.imshow('Adaptive threshold',th)
cv2.waitKey(0)
cv2.destroyAllWindows()

retval2,threshold2 = cv2.threshold(imagen2,120,255,cv2.THRESH_OTSU)
cv2.imshow('original',imagen1)
cv2.imshow('Otsu threshold',threshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()

retval2,threshold3 = cv2.threshold(imagen2,120,255,cv2.THRESH_BINARY)
cv2.imshow('original',imagen1)
cv2.imshow('BINARY',threshold3)
cv2.waitKey(0)
cv2.destroyAllWindows()

retval2,threshold4 = cv2.threshold(imagen2,120,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('original',imagen1)
cv2.imshow('Otsu +BINARY',threshold4)
cv2.waitKey(0)
cv2.destroyAllWindows()

retval2,threshold5 = cv2.threshold(imagen2,100,255,cv2.THRESH_BINARY_INV)
cv2.imshow('original',imagen1)
cv2.imshow('BINARYINV',threshold5)
cv2.waitKey(0)
cv2.destroyAllWindows()

retval2,threshold6 = cv2.threshold(imagen2,200,100,cv2.ADAPTIVE_THRESH_GAUSSIAN_C+cv2.THRESH_BINARY_INV)
cv2.imshow('original',imagen1)
cv2.imshow('BINARY INV+GAUSSIAN',threshold6)
cv2.waitKey(0)
cv2.destroyAllWindows()

threshold7= cv2.adaptiveThreshold(imagen2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 115, 1)
cv2.imshow('original',imagen2)
cv2.imshow('Adaptive thresholdBININV',threshold7)
cv2.waitKey(0)
cv2.destroyAllWindows()



cv2.waitKey(0)
cv2.destroyAllWindows()
