'''DICOM Tool box of functions.

Library of the functions for DICOM processing

Author: K F Graham
Version 1.0, 2.0


Package included:

Python 3.8.8
glob >  searches for all the pathnames matching pattern
numpy > for computing application
matplotlib -> for visulizations
plotly > for interactive visualizstion
pydicom > for workin with DICOM files
'''

# imports
import pydicom as dicom
import numpy as np
import os
import matplotlib.pyplot as plt

# Source filepaths
src = '/Users/keithgraham/PycharmProjects/ICT/RD'
filepath = '/Users/keithgraham/Desktop/01. Rotations /ICT /RD'

#destination filepaths
dst = '/Users/keithgraham/PycharmProject/ICT/DICOM_complete'



# matplotlib
'''code displays the image, dataset is the specic pixel data we want to display 
 the voxel coordinate can be inputted '''
plt.imshow(dataset[30,:,:])
plt.show()

#os
os.listdir('path/to/file')

for filename in os.listdir(filepath):
    if filename.endswith(".dcm"):
        print(os.path.join(filepath, filename))
    else:
        continue

#python
'''The range() function returns a sequence of numbers, starting from 0 
by default, and increments by 1 (by default), and stops before a specified number
syntax = range(start, stop, step)'''
range()
'''The len() function returns the number of items in an object. 
Syntax len(object)'''
len()

#use range() and len() in a loop to access each item by index
for i in range(len(object))

# pydicom
dataset = dicom.dcmread('path/to/file')








#loads the DICOM images
def load_scan(src):
    slices = [dicom.dcmread(src + '/' + s, force=True) for s in os.listdir(src)]
    slices = [s for s in slices if 'SliceLocation' in s]
    slices.sort(key=lambda x: int(x.InstanceNumber))
    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2])
    except:
        slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)
    for s in slices:
            s.SliceThickness = slice_thickness

    return slices #list of DICOM

#set path and load files

patient_dicom = load_scan(src)
patient_pixel = get_pixel_hu(patient_dicom)

#sanity check
#plt.imshow(ds.pixel_array[5,:,:])
#plt.show()



import os
import pydicom as dicom
import matplotlib.pyplot as plt
import numpy as np

#file paths (src - source), (dst - destination)
src = '/Users/keithgraham/PycharmProjects/ICT/RD'
dst = '/Users/keithgraham/PycharmProject/ICT/DICOM_complete'
#returns a list containing the names of the entries in the directory given by path
CT_images = os.listdir(src)

#for file in CT_images:
#   print(file)
#print(CT_images)


slices = [dicom.read_file(src + '/' + filename)
          for filename in CT_images]

#print(slices)

for i,dicom_data in enumerate(slices):
   array2d=dicom_data.pixel_array

#print(array2d)

#for filename in os.listdir(src):
#    if filename.endswith(".dcm"):
#        print(os.path.join(src, filename))
#    else:
#        continue

CT_images = os.listdir(src)
print(CT_images)
# slices = [dicom.read_file(src + '/' + filename)
#           for filename in CT_images]
#
# for i,dicom_data in enumerate(slices):
#    array2d=dicom_data.pixel_array
#
# for i in range(71):
#     plt.imshow(array2d[i,:,:], cmap="gray")
#     plt.show()


import pydicom as dicom
import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_modality_lut


folder_input = "/Users/keithgraham/PycharmProjects/ICT/pydicom/dataset/RD.1.2.826.0.1.3680043.2.526.1984402481.1596625336217.43912.dcm"
#dcmread is going to read this input into an object
ds = dicom.dcmread(folder_input)
arr = ds.pixel_array
hu = apply_modality_lut(arr, ds)
#print(ds.pixel_array)
#print(ds.Columns)
#print(ds.Rows)


def
normalisedArrays = []
for norm in calibrateArrays:
    normalised = 7*calibrateArrays((calibrateArrays+3)/(2+3))
    normalisedArrays.append(normalised)


plt.imshow(ds.pixel_array[5,:,:])
plt.show()

plt.imshow(ds.pixel_array[30,:,:])
plt.show()

'''The iterable is an object with elements that can be looped over.Directory containing dicom files
The iterator variable (typically i for index) stores a portion
of the iterable when the for loop is being executed.
Each dicom file is stores in (i) if it end .dcm
Each DICOM file is appened to out empty list [dicom_files]
Lexixal scoping varible are determined entirely by the location in the souce code(i) is a local namespace within openFiles() hence it does
not clash with loops in other functions
local namespaces cannot be seen or reffered to outside the function
'''