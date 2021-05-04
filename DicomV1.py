'''DICOM Tool box of functions.

Library of the functions for DICOM processing

Each series consists of Dicom files, each Dicom file represents a different RT dose beam hitting the tumour
and plus number of stabilising beams.  Each Dicom consists of a header and image data set. The information
within the header is organized as a constant and standardized series of tags. The image is stored as pixel_data
which can be returned to the caller as a numpy. Each array shape is [Z, X, Y] [71, 128, 176]. This toolkit
enables the parsing of Dicom components, calibrates the pixel array data and combine the data from each beam
to create an image.

Author: K F Graham
Version 1


Package included:

Python 3.8.8
matplotlib -> for visualizations
plotly -> for interactive visualization
pydicom -> for working with DICOM files
'''
# import
import pydicom as dicom
import matplotlib.pyplot as plt

#file paths
src = '/Users/keithgraham/PycharmProjects/ICT/RD'
dst = '/Users/keithgraham/PycharmProject/ICT/DICOM_complete'

# file reading
dataset1 = dicom.dcmread('/Users/keithgraham/PycharmProjects/ICT/RD/RD.1.2.826.0.1.3680043.2.526.552059069.15966253338440.43870.dcm')
dataset2 = dicom.dcmread('/Users/keithgraham/PycharmProjects/ICT/RD/RD.1.2.826.0.1.3680043.2.526.756858128.15966253343630.43890.dcm')
dataset3 = dicom.dcmread('/Users/keithgraham/PycharmProjects/ICT/RD/RD.1.2.826.0.1.3680043.2.526.773810862.15966253340810.43880.dcm')
dataset4 = dicom.dcmread('/Users/keithgraham/PycharmProjects/ICT/RD/RD.1.2.826.0.1.3680043.2.526.811861617.15966253356630.43905.dcm')
dataset5 = dicom.dcmread('/Users/keithgraham/PycharmProjects/ICT/RD/RD.1.2.826.0.1.3680043.2.526.1625265003.1596625333179.43846.dcm')
dataset6 = dicom.dcmread('/Users/keithgraham/PycharmProjects/ICT/RD/RD.1.2.826.0.1.3680043.2.526.1697074823.1596625335890.43908.dcm')
dataset7 = dicom.dcmread('/Users/keithgraham/PycharmProjects/ICT/RD/RD.1.2.826.0.1.3680043.2.526.1739100954.1596625335396.43901.dcm')
dataset8 = dicom.dcmread('/Users/keithgraham/PycharmProjects/ICT/RD/RD.1.2.826.0.1.3680043.2.526.1744971353.1596625333469.43859.dcm')
dataset9 = dicom.dcmread('/Users/keithgraham/PycharmProjects/ICT/RD/RD.1.2.826.0.1.3680043.2.526.1758530822.1596625335141.43897.dcm')
dataset10 = dicom.dcmread('/Users/keithgraham/PycharmProjects/ICT/RD/RD.1.2.826.0.1.3680043.2.526.1984402481.1596625336217.43912.dcm')



#Calibrate the pixel data of each image against the unquie DoseGridScaling varialbe in each DICOM image
ds1 = dataset1.pixel_array * dataset1.DoseGridScaling
ds2 = dataset2.pixel_array * dataset2.DoseGridScaling
ds3 = dataset3.pixel_array * dataset3.DoseGridScaling
ds4 = dataset4.pixel_array * dataset4.DoseGridScaling
ds5 = dataset5.pixel_array * dataset5.DoseGridScaling
ds6 = dataset6.pixel_array * dataset6.DoseGridScaling
ds7 = dataset7.pixel_array * dataset7.DoseGridScaling
ds8 = dataset8.pixel_array * dataset8.DoseGridScaling
ds9 = dataset9.pixel_array * dataset9.DoseGridScaling
ds10 = dataset10.pixel_array * dataset10.DoseGridScaling

print(ds1.shape)
# Add pixel array together
dataset_combined = ds1 + ds2 + ds3 + ds4 + ds5 + ds6 + ds7 + ds8 + ds9 +ds10



plt.imshow(dataset_combined[30,:,:])
plt.show()

