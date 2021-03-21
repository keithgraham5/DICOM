'''DICOM Tool box of functions.

Library of the functions for DICOM processing

Author: K F Graham
Version 1.0


Package included:

Python 3.6
chart_studio >
pydicom > for reading DICOM files
numpy > for computing application
scipy >also computing application
skimage > collections of algorithms for image processing
matplotlib -> for visulizations
plotly > for interactive visualizstion
ipywidget > are interactive HTML widgets for interactive plots

'''

# common packages
import numpy as np
import os
import copy
from math import *
import matplotlib.pyplot as plt
from functools import reduce

# reading in dicom files
import pydicom as dicom

# skimage image processing packages
from skimage import measure, morphology
from skimage.morphology import ball, binary_closing
from skimage.measure import label, regionprops

# scipy linear algebra functions
from scipy.linalg import norm
import scipy.ndimage

# ipywidgets for some interactive plots
from ipywidgets.widgets import *
import ipywidgets as widgets

# plotly 3D interactive graphs
import plotly
from plotly.graph_objs import *
import chart_studio.plotly as py
# set plotly credentials here
# this allows you to send results to your account plotly.tools.set_credentials_file(username=your_username, api_key=your_key)



#loads the DICOM images
def load_scan(path):
    slices = [dicom.dcmread(path + '/' + s, force=True) for s in os.listdir(path)]
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
path = "/Users/keithgraham/PycharmProjects/ICT/pydicom/dataset"
patient_dicom = load_scan(path)
patient_pixel = get_pixel_hu(patient_dicom)

#sanity check
#plt.imshow(ds.pixel_array[5,:,:])
#plt.show()