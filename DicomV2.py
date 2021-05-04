'''DICOM Tool box of functions.

Library of the functions for DICOM processing

Each series consists of Dicom files, each Dicom file represents a different RT dose beam hitting the tumour
and plus number of stabilising beams.  Each Dicom consists of a header and image data set. The information
within the header is organized as a constant and standardized series of tags. The image is stored as pixel_data
which can be returned to the caller as a numpy. Each array shape is [Z, X, Y] [71, 128, 176]. This toolkit
enables the parsing of Dicom components, calibrates the pixel array data and combine the data from each beam
to create an image.

Author: K F Graham
Version 2
Addition of iterations (loops) into the pipeline

Package included:

Python 3.8.8
glob >  searches for all the pathnames matching pattern
numpy > for computing application
matplotlib -> for visulizations
pydicom > for workin with DICOM files
'''

import glob
import numpy as np
import pydicom
import matplotlib.pyplot as plt

#file paths
src = '/Users/keithgraham/PycharmProjects/ICT/RD'
dst = '/Users/keithgraham/PycharmProject/ICT/DICOM_complete'

'''Directory iteration over an iterable filepath to create file list'''
dicom_files = [] #creates and empty list
for file_name in glob.iglob('/Users/keithgraham/PycharmProjects/ICT/RD/**/*.dcm', recursive=True):
    if file_name.endswith('.dcm'): #if iterable variables end in .dcm execute code
        dicom_files.append(file_name) #for file ending in .dcm append to the list dicom_files

'''Parse iteration over an iterable list (dicom_files) to parse components'''
files = [] #create an empty list
for images in dicom_files:
    dataset = pydicom.dcmread(images)# for each iterable variable parse into components and save as a data set
    files.append(dataset)# for each dataset append into a new list called beams


'''iteration over an iterable  list (beams) calibrate pixel data'''
calibratedArrays = []#create an empty list
for arry in files:# for each iterabel variable (arry) from iterabel list (beams)
    calibration = arry.pixel_array * arry.DoseGridScaling#multiple the pixel_array data by the DoseGridScaling
    calibratedArrays.append(calibration)# for each calibration append into a new list called calibratedArrays

'''Return a new array with a given shape filled with zeros'''
z, x, y = calibratedArrays[0].shape#takes the shape of the calibrated array [z, x, y] [71, 128, 176]
combinedbeams = np.zeros([z, x, y])#returns a new array of the defined shape filled with zeros saves array to variable

'''Combinign beam iteration over an interable list (calibratedArrays) '''
for each_beam in calibratedArrays:
    combinedbeams = combinedbeams + each_beam


# Creates an empty array based on the shape of the first array
'''Show image'''
plt.imshow(combinedbeams[30,:,:])
plt.show()