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
onesrc = '/Users/keithgraham/PycharmProjects/ICT/RD/RD.1.2.826.0.1.3680043.2.526.552059069.15966253338440.43870.dcm'
src = '/Users/keithgraham/PycharmProjects/ICT/RD'
filepath = '/Users/keithgraham/Desktop/01. Rotations /ICT /RD'

#destination filepaths
dst = '/Users/keithgraham/PycharmProject/ICT/DICOM_complete'

#numpy
'''The shape fo an array is the number of elements in each dimension
Numpy arrsy have an attribute called shape that returns a tuple with
 each index having the number corresponsing elements'''
array.shape

#os.listdir
'''returns a list containning the names of the entrie in the directory given by path '''
dicom_files = []
for i in os.listdir(src):
    if i.endswith(".dcm"):
        dicom_files.append(i)


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
ds.pixel_array.shape








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




'''makes the dicom file readable then converts the 1D image data a ndarray. From this ndarray we can get its shape or dimensions
and print this infomration to the screen'''
# ds = dicom.dcmread('/Users/keithgraham/PycharmProjects/ICT/RD/RD.1.2.826.0.1.3680043.2.526.552059069.15966253338440.43870.dcm')
# print(ds.pixel_array.shape)

'''Converting a DICOM image to a jpeg'''

import numpy as np
import pydicom as dicom
from PIL import Image
import os

# im = dicom.dcmread('/Users/keithgraham/PycharmProjects/ICT/RD/RD.1.2.826.0.1.3680043.2.526.552059069.15966253338440.43870.dcm')
# im = im.pixel_array.astype(float)
# rescaled_image = (np.maximum(im,0)/im.max())*255
# final_image = np.uint8(rescaled_image)
#
# final_image =Image.fromarray(final_image)

def get_names(path):
    '''Function will get all the names form a folder. The loop will return 3 types of data,
    the root, the directory name and the file name (the root refers to the top level directory of a file '''
    names = [] #create an empty list
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            _, ext = os.path.splitext(filename)#spliting the extenstion to see if the image extension containts dicom, the split is stores in to two variables
            if ext in ['.dcm']:# now we see if the variable extension is .dcm or not
                names.append(filename)# if the extension is DCM then append this name to the names[]

    return names


def convert_dcm_jpeg(dicom_file, slice_no):# # each time the convert_dcm_jpeg function is called and passed the loop variable from
    #below (argument (name) into the parameter (dicom_file) an object is created.
    # path = '/Users/keithgraham/PycharmProjects/ICT/RD/' + name
    # dicom_heading = dicom.dcmread(path)
    dicom_heading = dicom.dcmread('/Users/keithgraham/PycharmProjects/ICT/RD/' + dicom_file)  #When the object is passed
    # the function it object is maniplates sohere we are making the object readable sing dicom.dcmread
    # dicom_heading = dicom.dcmread(name) does not work needs directory to file
    #print(dicom_heading.pixel_array.shape) this just prints our the shape of thep i[ixel array
    all_slices_from_individual_dicom_file = dicom_heading.pixel_array.astype(float)# each dicom file represents an
    # individual beam, each beam is composed of 71 slices, the dicom.dcmread provides a readable version of our Dicom
    # file to thevariable dicom_heading. This variable will also contain pixel data for each of the 71 slices.
    # we want to extract that pixel data and convert to a numpy array hence .pixel_array returns the pixel data as a numpy.ndarray
    #As we are going to be performing computational calculation on those values we want to convert all pixel to a flaot
    # The values we are dealing with the a pixel array are typicall whole number. if we divide a whole number by a whole
    # number we end up decimal places. Python will try and keep things as simple as possible so if we give it a
    # Whole number to dived by python will give us a whole number in return. if we divide 1 by 3 (1//3) for example we get 0.
    # when what we should get is 0.3333 losing.
        #if you type in 1/3 python sees this as a fraction not a dividision and returns it as 0.3333
    #So if the image is in integer why convert to a pixel_array. Well Dicom images are stores as 1D human unreadable
    # datasets so pixel_array converts and structures this data into human readable, so as previosuly mentioned the
    # reason we ensure everything in the array is treated as a float is to maintian precison durint calculaltiosn
    individual_slice_from_each_dicom = all_slices_from_individual_dicom_file[slice_no, :, :]
    #Here we start to access the individual pixel arrays from each slice of the DICOM file
    #Here we use the second argument passed up form the loop in the function call to the parameter of def convert_dcm_jpeg.
    #the second variable passed into the funciton is used to call upon the coordinate along the z,x,y. (71, 128, 176)
    #so far we have one Dicom file we passed as a loop variable form which we select 1 of its slices based on the lopp
    # varialbe being used to access the z coodinates. if you look back up to the top of our code you can see that we
    # make the the dicom files readable using the dicom.dcmread. this is essntially a function with a lot of hidden
    # functinalities. These functinoalites enable python to undestand that when we give it an array coordinate python
    # know what we are looking for. So dcmread is not just open and read me, it telling python this is how to read me.
    # coordinates which we passed in as a variable. Both loop variable were created in the function call but not defined
    #untill passed into the def  convert_dcm_to jpeg()
    rescaled_image = (np.maximum(individual_slice_from_each_dicom,0)/individual_slice_from_each_dicom.max())*255
    # So now we an individual Dicom file from which we have obtained acess to an indiviudal slice of that file and that
    # slice we now represent as a pixel array.
    # now we need to reshape the pixel array into the same dimension as a the jpeg so we need to normalise or data
    # we normalise each data point in the pixel by adding and/or multipleing by constaints so that values fall between
    # 0 and 1
    # above we have two arrays, both of these arrays are the same. np.maximum compares both of these arrays.
    # from the first array we set the lowest number wheater negatibe or positive to zero. any nummber obove this will
    # then be greater than zero
    # we then call upon the data from a second array (same data, same array) and called the maximum number in the arrray.
    # Dvididing these two numbers between each other essentially place all those numbers in the array between between 0 and 1.
    # Then we multille by 255 as 0 = black and 255 = peak white so everything inbetween can be expresssed as grey scale
    final_image = np.uint8(rescaled_image)
    # unit8 data type uses unsigned 8 bit integers which is the range of a pixel so essnetially we are making our image
    # machine readable again
    final_image =Image.fromarray(final_image)#
    # here we are simple creating an image memeory from obhect exporint the array
    return final_image
    #here we are retruning this image back to the line

names = get_names('/Users/keithgraham/PycharmProjects/ICT/RD/')

for name in names: #loops through the names list created by the calling of the function get_names
    # print(name) #as each loop variable enters the name variable the filename is printed
    # for slice in range(71)#each file contains 71 slices through which the for loop iterates over
    for slice in range(0, len(name) -1):#same as above except using the len function to sum the total number of files in the (see convert_dcm_jpeg)
        image = convert_dcm_jpeg(name, slice) # we call the convert_dcm_jpeg function with two arguments required (the loop variable name and the slice variable
        image.save(name+'_'+ str(slice) +'.jpg')
        print("saved")
