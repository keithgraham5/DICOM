'''
DICOM_prtotype_V.2

addtion of the eqd2 to arrays
two places this could be placed
1) beforet the array are combined
2) after the arrays have been combined
Doing before the arrays are combined is preferable
this will compenstae for different series of the same patinet being added together

'''
import glob
import numpy as np
import pydicom as dicom
import matplotlib.pyplot as plt

#file paths
src = '/Users/keithgraham/PycharmProjects/ICT/RD'
dst = '/Users/keithgraham/PycharmProject/ICT/DICOM_complete'

#loop through directory identiying files ending with .dcm
dicom_files = []
for file_name in glob.iglob('/Users/keithgraham/PycharmProjects/ICT/RD/**/*.dcm', recursive=True):
    if file_name.endswith('.dcm'):
        dicom_files.append(file_name)


slices = []
for images in dicom_files:
    ds = dicom.dcmread(images)
    slices.append(ds)


calibrateArrays = []
for arry in slices:
    calibrateArray = arry.pixel_array * arry.DoseGridScaling
    calibrateArrays.append(calibrateArray)

# normalised arrays with EQD2


normalisedArrays = []
for norm in calibrateArrays:
    normalised = 7*calibrateArrays((calibrateArrays+3)/(2+3))
    normalisedArrays.append(normalised)


print(normalisedArrays)
# only showing one image
z, x, y = calibrateArrays[0].shape
combineArray = np.zeros([z, x, y])

for beam in calibrateArrays:
    combineArray = combineArray + beam


# Creates an empty array based on the shape of the first array

plt.imshow(combineArray[30,:,:])
plt.show()





