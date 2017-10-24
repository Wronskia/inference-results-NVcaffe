import h5py
import numpy as np

filename1 = 'caffe-dump.h5'
filename2 = 'caffe-dump-nvidia.h5'

f_caffe = h5py.File(filename1, 'r')
f_nvidia_caffe = h5py.File(filename2, 'r')

for i in f_nvidia_caffe['lyr']:
    if np.linalg.norm(list(f_nvidia_caffe['lyr'][str(i)]['output'])) - np.linalg.norm(list(f_caffe['lyr'][str(i)]['output']))>1000:
        print(i)
        break

# To see the output of the last layer
print(np.argmax(list(f_caffe['lyr']['121']['output'])))

