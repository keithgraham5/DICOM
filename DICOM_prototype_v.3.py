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

class Dicom:
    '''open, read, calibrate and normalise Dicom archive'''

    def __init__(self):
        '''Initialize src attribute'''
        self.loop_dicom_files()
        self.loop_dicom_files_read()
        self.calibrate_arrays()
        # self.combine_array()



# loop through directory identiying files ending with .dcm
    def loop_dicom_files (self):
        '''method loops through directory, identifies file ending with .dcm
        append those files to an empty list, list is returned'''
        self.dicom_files = []
        for i in glob.iglob('/Users/keithgraham/PycharmProjects/ICT/RD/**/*.dcm', recursive=True):
            if i.endswith('.dcm'):
                self.dicom_files.append(i)#append said files to empty list
        print(self.dicom_files)


    def loop_dicom_files_read(self):
        '''Loop DICOM files reading each into an empty list'''
        self.beams = []
        for i in self.dicom_files:
            ds = dicom.dcmread(i)
            self.beams.append(ds)
        print(self.beams)

    def calibrate_arrays(self):
        self.calibrateArrays = []
        for arry in self.beams:
            calibrateArray = arry.pixel_array * arry.DoseGridScaling
            self.calibrateArrays.append(calibrateArray)
        print(self.calibrateArrays)

# n, m, o = calibrateArrays.shape
# for i in range(n)
#     for j in range(m)
#         for h in range(o)
#             x = array(i, j, h)
#             n = 5
#             c = 3



    # def combine_array(self):
    #     z, x, y = calibrateArrays[0].shape
    #     self.combineArray = np.zeros([z, x, y])
    #     for beam in calibrateArrays:
    #         self.combineArray = combineArray + beam
    #         plt.imshow(self.combineArray[30,:,:])
    #         plt.show()
    #     print(self.combineArray)

# Creates an empty array based on the shape of the first array
#     def show_image(self):
#         plt.imshow(self.combineArray[30,:,:])
#         plt.show()

work = Dicom()

