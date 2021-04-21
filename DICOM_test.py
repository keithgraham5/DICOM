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
    def loop_dicom_files(self):

# def loopDicomFile(self):
# openedFiles = [] # empty list
# for i in glob.iglob('/Users/keithgraham/PycharmProjects/ICT/RD/**/*.dcm', recursive=True):
#     if i.endswith('.dcm'): # if file in loop ends with .dcm
#         openedFiles.append(i) #append said file ending in dcm to emtpy list

        openedFiles = []
        for i in os.listdir(self.src):
            if i.endswith(".dcm"):
                openedFiles.append(i)

    def read_dicom_file(self):
        readFiles = []
        for i in self:
            dataset = dicom.dcmread(i)
            readFiles.append(dataset)

    def calibrate_dicom_arrays(self):
        calibratedFiles = []
        for i in self:
            calibrateArray = arry.pixel_array * arry.DoseGridScaling
            calibratedFiles.append(calibrateArray)


    def combine_arrays(self):
        z, x, y = calibratedFiles[0].shape
        combineArray = np.zeros([z, x, y])

        for beam in self:
            combineArray = combineArray + beam

    def EQ_arrray(self):
        '''array.shape '''
        m, n, o = array.shape
        for i in range(n)
            for j in range(m)
                for h in range (o)
event = Dicom(src)
event.loop_dicom_files()
event.read_dicom_file()
event.calibrate_dicom_arrays()
event.combine_arrays()




#Main program

#
# plt.imshow(combineArray[30,:,:])
# plt.show()





