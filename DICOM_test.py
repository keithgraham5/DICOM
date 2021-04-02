'''
DICOM_prtotype_V.3

The conversion of statement to functions

Resources
Learning python > chapter 16, 17

keywords
def, function, lexical scoping (local, nonlocal, global)

'''
import glob
import numpy as np
import pydicom as dicom
import matplotlib.pyplot as plt

#file paths
src = '/Users/keithgraham/PycharmProjects/ICT/RD'
dst = '/Users/keithgraham/PycharmProject/ICT/DICOM_complete'

#namespaces

#loop through directory identiying files ending with .dcm
def loopDicomFiles():
'''
The iterable is an object with elements that can be looped over.
    Directory containing dicom files
The iterator variable (typically i for index) stores a portion
of the iterable when the for loop is being executed.
    Each dicom file is stores in (i) if it end .dcm
Each DICOM file is appened to out empty list [dicom_files]
Lexixal scoping varible are determined entirely by the location in the souce code
    (i) is a local namespace within openFiles() hence it does
    not clash with loops in other functions
    local namespaces cannot be seen or reffered to outside the function
'''
def loopDicomFile(src):
openedFiles = [] # empty list
for i in glob.iglob('/Users/keithgraham/PycharmProjects/ICT/RD/**/*.dcm', recursive=True):
    if i.endswith('.dcm'): # if file in loop ends with .dcm
        openedFiles.append(i) #append said file ending in dcm to emtpy list

# def readDicomFile():
# readFiles = []
# for i in openedFiles:
#     dataset = dicom.dcmread(images)
#     readFiles.append(dataset)
#
# def calibrateDicomArrays():
# calibratedFiles = []
# for i in readFiles:
#     calibrateArray = arry.pixel_array * arry.DoseGridScaling
#     calibratedFiles.append(calibrateArray)
#
#
#
# def calibrateArrays():
# z, x, y = calibratedFiles[0].shape
# combineArray = np.zeros([z, x, y])
#
# for beam in calibratedFiles:
#     combineArray = combineArray + beam


#Main program
loopDicomFiles()
# readDicomFile()
# calibrateDicomImages()
# calibrateArray()
#
#
# plt.imshow(combineArray[30,:,:])
# plt.show()





