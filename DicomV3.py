'''DICOM Tool box of functions.

Library of the functions for DICOM processing

Each series consists of Dicom files, each Dicom file represents a different RT dose beam hitting the tumour
and plus number of stabilising beams.  Each Dicom consists of a header and image data set. The information
within the header is organized as a constant and standardized series of tags. The image is stored as pixel_data
which can be returned to the caller as a numpy. Each array shape is [Z, X, Y] [71, 128, 176]. This toolkit
enables the parsing of Dicom components, calibrates the pixel array data and combine the data from each beam
to create an image.

Author: K F Graham
Version 3
Break down scrip and convert into functions

Package included:

Python 3.8.8
glob >  searches for all the pathnames matching pattern
numpy > for computing application
matplotlib -> for visulizations
pydicom > for workin with DICOM files'''

import glob
import numpy as np
import pydicom as dicom
import matplotlib.pyplot as plt

#file paths
src = '/Users/keithgraham/PycharmProjects/ICT/RD'
dst = '/Users/keithgraham/PycharmProject/ICT/DICOM_complete'

def list_dcmfiles_from_directory(src):
    '''Directory iteration over an iterable filepath to create list of the files ending in .dcm'''
    dicom_files = [] #creates and empty list
    for file_name in glob.iglob('/Users/keithgraham/PycharmProjects/ICT/RD/**/*.dcm', recursive=True):
        if file_name.endswith('.dcm'): #if iterable variables end in .dcm execute code
            dicom_files.append(file_name) #for file ending in .dcm append to the list dicom_files
    return (dicom_files) #send the result back to the caller


#
def parse_dicom_files(dicom_files):
    '''Parse iteration over an iterable list (dicom_files) to parse components'''
    files = []
    for images in dicom_files:
        ds = dicom.dcmread(images)
        files.append(ds)
    return (files)

def calibrate_arrays(files):
    '''iteration over an iterable  list (beams) calibrate pixel data'''
    calibrateArrays = []
    for arry in files:
        calibrateArray = arry.pixel_array * arry.DoseGridScaling
        calibrateArrays.append(calibrateArray)
    return (calibrateArrays)


def create_fill_empty_arry(calibrateArray):
    '''create an empty array in which to sum the totals of all arrays'''
    z, x, y = calibrateArray[0].shape
    combinedbeams = np.zeros([z, x, y])
    for each_beam in calibrateArray:
        combinedbeams = combinedbeams + each_beam
    return (combinedbeams)

def visulise(combinedbeams) :
    plt.imshow(combinedbeams[30,:,:])
    plt.show()

dicom_list = list_dcmfiles_from_directory(src)
dicom_components = parse_dicom_files(dicom_list)
calibrated = calibrate_arrays(dicom_components)
carry = create_fill_empty_arry(calibrated)
image = visulise(carry)



