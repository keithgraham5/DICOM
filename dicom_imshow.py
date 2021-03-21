import pydicom as dicom
import matplotlib.pyplot as plt
from pydicom.pixel_data_handlers.util import apply_modality_lut


folder_input = "/Users/keithgraham/PycharmProjects/ICT/pydicom/dataset/RD.1.2.826.0.1.3680043.2.526.1984402481.1596625336217.43912.dcm"
#dcmread is going to read this input into an object
ds = dicom.dcmread(folder_input)
arr = ds.pixel_array
hu = apply_modality_lut(arr, ds)
#print(ds.pixel_array)
#print(ds.Columns)
#print(ds.Rows)

plt.imshow(ds.pixel_array[5,:,:])
plt.show()

plt.imshow(ds.pixel_array[30,:,:])
plt.show()