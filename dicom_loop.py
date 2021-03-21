import os
import glob
import numpy as np
from pydicom import dcmread
directory = '/Users/keithgraham/PycharmProjects/ICT/pydicom/dataset'
for filename in os.listdir(directory):
    if filename.endswith(".dcm"):
        print(os.path.join(directory, filename))
    else:
        continue