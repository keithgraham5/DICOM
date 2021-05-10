'''DICOM Toolbox of functions.

Library of functions for DICOM RT Dose processing

Each series consists of Dicom files, each Dicom file represents a different RT dose beam targeting the tumour.
Each Dicom consists of a header and image data set. The information within the header is organized as a constant
and standardized series of tags. The image is stored as pixel_data which can be returned to the caller as a
numpy array. Each array shape has [Z, X, Y] coordinates (e.g. [71, 128, 176]) representing each voxel. This
toolkit enables the parsing of Dicom file components, the calibration of the pixel array data with to the
equivalent dose in 2Gy fractions (EQD2) and combine the data from each beam to create an image.

EQD2 Formula
EQD2 = D * ([d +(a/b)] / [2+ (a/b)])
D = total dose given in Gy
d = dose per fraction in Gy
a/b = dose at which the linear and quadratic components of cell kill are equal
n = number of fractions

Author: K F Graham

Version 4
    Addition of EQD2 functionality.

Package included:
glob ->  searches for all the pathnames matching pattern
numpy -> for computing application
matplotlib -> for visualizations
pydicom -> for working with DICOM files
Python 3.8.8
'''

import glob
import numpy as np
import pydicom as dicom
import matplotlib.pyplot as plt

#file paths
src = '/Users/keithgraham/PycharmProjects/ICT/RD'
dst = '/Users/keithgraham/PycharmProject/ICT/DICOM_complete'

n = float(input("What was the number of fraction?"))

def list_dcm_files(src):
    '''Directory iteration over an iterable filepath to create list of the files ending in .dcm'''
    dcm_files = [] #creates and empty list
    for file_name in glob.iglob('/Users/keithgraham/PycharmProjects/ICT/RD/**/*.dcm', recursive=True):
        if file_name.endswith('.dcm'): #if iterable variables end in .dcm execute code
            dcm_files.append(file_name) #for file ending in .dcm append to the list dicom_files
    return (dcm_files) #send the result back to the caller

def parse_dcm_files(dcm_files):
    '''Parse iteration over an iterable list of file paths (dicom_files) to parse components'''
    dcm_file_components = []
    for i in dcm_files:
        ds = dicom.dcmread(i)
        dcm_file_components.append(ds)
    return (dcm_file_components)

def calibrate_array_component(dcm_file_components):
    '''iteration over an iterable list (dcm_file_components), return calibrated SOP class pixel
    data as pixel array'''
    calibrated_pixel_arrays = []
    for component in dcm_file_components:
        calibrateArray = component.pixel_array * component.DoseGridScaling
        calibrated_pixel_arrays.append(calibrateArray)
    return (calibrated_pixel_arrays)

def EQD2_equation(each_beam, n):
    '''Calculates the equivalent dose in 2Gy Fractions at each voxel'''
    z, x, y = each_beam.shape
    # print(z,x,y) # there are 10 beam hence 10 sets of coordinates
    EQD2 = np.zeros([z, x, y])#return a new array of given shape and type,filled with zeros
    for i in range(z):
        for j in range(x):
            for k in range(y):
                EQD2[i, j, k] = each_beam[i, j, k] * ((each_beam[i, j, k]/ n + 3)/(2 + 3))#EQD2 equation
    return(EQD2)


def sum_beams(calibrated_pixel_arrays):
    '''create an empty array in which to sum the totals of each beam'''
    z, x, y = calibrated_pixel_arrays[0].shape
    EQD2_arry = np.zeros([z, x, y])
    for each_beam in calibrated_pixel_arrays:
        EQD2_arry = EQD2_arry + EQD2_equation(each_beam, n)
    return (EQD2_arry)


def visulise(EQD2_arry):
    '''view each slice of the summed beam alond the z access'''
    plt.imshow(EQD2_arry[30,:,:])
    plt.show()

dicom_list = list_dcm_files(src)
dicom_components = parse_dcm_files(dicom_list)
calibrated_pixel_arrays = calibrate_array_component(dicom_components)
EQD2_arry = sum_beams(calibrated_pixel_arrays)
image = visulise(EQD2_arry)