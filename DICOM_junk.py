import os
import glob
import numpy as np
import pydicom as dicom

#file paths







# for i,s in enumerate(slices):
#    array2d=s.pixel_array
# print(array2d)

import os


#file paths
src = '/Users/keithgraham/PycharmProjects/ICT/RD'
dst = '/Users/keithgraham/PycharmProject/ICT/DICOM_complete'

'''Using listdir to loop through file path does not work as expected caused a issue in the next loop '''
dicom_files = []
for i in os.listdir(src):
    if i.endswith(".dcm"):
        dicom_files.append(i)
print(dicom_files)

#loops through files endwith .dcm
for filename in os.listdir(src):
    if filename.endswith(".dcm"):
        dicom.dcmread(

# loop through directory identifying file ending with .dcm
#error keeps saying no such file or directory for one of the files
# File_list = []
# for file_name in os.listdir(src):
#     if file_name.endswith('.dcm'):
#         File_list.append(file_name)
#         continue
#     else:
#         continue
#
# print(File_list)





# print(scans)

# for loop through iteration File_list read each file access pixel array data
# This will not work orignal list is being appenned back into the empty list
# slices = []
# for images in scans:
#     ds = dicom.dcmread(images)
#     slices.append(images)
#


# sanity check
# print(slices)






# print(calibrateArrays)

arr = np.vstack(calibrateArrays)

print(arr)
# add element (arrays) in list together




plt.imshow(arr[20,:,:], cmap="gray")
plt.show()


# #List comprehension to read each file
# Read_Files = [dicom.dcmread(files) for files in File_list]

# #sanity check
# print(Read_Files)


# sanity check
# print(ds1)



calibrateArrays

# plt.imshow(dataset_combined[30,:,:], cmap="gray")
# plt.show()

        '''
        DICOM_prtotype_V.2

        Addtion lopping through file

        '''
        import glob
        import numpy as np
        import os
        import pydicom as dicom
        import matplotlib.pyplot as plt

        # file paths
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
            def loop_dicom_files(self):
                '''method loops through directory, identifies file ending with .dcm
                append those files to an empty list, list is returned'''
                self.dicom_files = []
                for i in glob.iglob('/Users/keithgraham/PycharmProjects/ICT/RD/**/*.dcm', recursive=True):
                    if i.endswith('.dcm'):
                        self.dicom_files.append(i)  # append said files to empty list
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

