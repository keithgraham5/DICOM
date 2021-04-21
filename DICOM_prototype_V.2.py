'''
DICOM_prtotype_V.2

Addtion lopping through file

'''
import glob
import numpy as np
import os
import pydicom as dicom
import matplotlib.pyplot as plt

#file paths
src = '/Users/keithgraham/PycharmProjects/ICT/RD'
dst = '/Users/keithgraham/PycharmProject/ICT/DICOM_complete'
def list_dcmfiles_from_directory(src):
    '''loops through directory to find file ext ending in .dcm appends these file to list '''
    dicom_files = [] #creates and empty list
    for file_name in glob.iglob('/Users/keithgraham/PycharmProjects/ICT/RD/**/*.dcm', recursive=True):
        if file_name.endswith('.dcm'):
            dicom_files.append(file_name)
    return (dicom_files)


# def read_dicom_files(dicom_files):
#     '''using pydicom.dcmread to make dicom files readable,
#     each of the dicom represent a single radiation beam devilvered over a complete treatment plan '''
#     single_radiation_beam = []
#     for images in dicom_files:
#         ds = dicom.dcmread(images)
#         single_radiation_beam.append(ds)
#     return (single_radiation_beam)
#
#
#
# def calibrate_arrays(single_radiation_beam):
#         '''Each array require calibration against their individual Dose Grid scaling '''
#         calibrateArrays = []
#         for arry in slices:
#             calibrateArray = arry.pixel_array * arry.DoseGridScaling
#             calibrateArrays.append(calibrateArray)
#         return (calibrateArrays)
#
#
# def combine_array(calibrateArray):
#     '''create an empty array in which to sum the totals of all arrays'''
#     z, x, y = calibrateArrays[0].shape
#     combineArray = np.zeros([z, x, y])
#     for beam in calibrateArrays:
#         combineArray = combineArray + beam
#     return (combineArray)
#
#
#
#
# # plt.imshow(combineArray[30,:,:])
# # plt.show()
#
x = list_dcmfiles_from_directory(src)
print(x)
# read_dicom_files(dicom_files)
# calibrate_arrays(single_radiation_beam)
# combine_array(calibrateArray)