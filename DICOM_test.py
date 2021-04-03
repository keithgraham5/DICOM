'''
DICOM_prtotype_V.3

The conversion of statement to functions

Resources
Learning python > chapter 16, 17

keywords
def, function, lexical scoping (local, nonlocal, global)

'''
import glob
import matplotlib.pyplot as plt
import numpy as np
import os
import pydicom as dicom



#file paths
src = '/Users/keithgraham/PycharmProjects/ICT/RD'
dst = '/Users/keithgraham/PycharmProject/ICT/DICOM_complete'

class Dicom:
    '''open, read, calibrate and normalise Dicom archive'''

    def __init__(self, src):
        '''Initialize src attribute'''
        self.src = src

#loop through directory identiying files ending with .dcm
    def loopDicomFiles(self):

# def loopDicomFile(self):
# openedFiles = [] # empty list
# for i in glob.iglob('/Users/keithgraham/PycharmProjects/ICT/RD/**/*.dcm', recursive=True):
#     if i.endswith('.dcm'): # if file in loop ends with .dcm
#         openedFiles.append(i) #append said file ending in dcm to emtpy list

        openedFiles = []
        for i in os.listdir(self.src):
            if i.endswith(".dcm"):
                openedFiles.append(i)
            return(openedFiles)
            print(openedFiles)

    # def readDicomFile(self):
    # readFiles = []
    # for i in openedFiles:
    #     dataset = dicom.dcmread(images)
    #     readFiles.append(dataset)
    #
    # def calibrateDicomArrays(self):
    # calibratedFiles = []
    # for i in readFiles:
    #     calibrateArray = arry.pixel_array * arry.DoseGridScaling
    #     calibratedFiles.append(calibrateArray)
    #
    #
    #
    # def calibrateArrays(self):
    # z, x, y = calibratedFiles[0].shape
    # combineArray = np.zeros([z, x, y])
    #
    # for beam in calibratedFiles:
    #     combineArray = combineArray + beam

Dicom(src)
#Main program

#
# plt.imshow(combineArray[30,:,:])
# plt.show()





