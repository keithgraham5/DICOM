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


# #loops through files endwith .dcm
# for filename in os.listdir(src):
#     if filename.endswith(".dcm"):
#         dicom.dcmread(

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