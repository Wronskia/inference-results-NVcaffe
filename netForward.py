import caffe
import h5py
import argparse

def dump_inference(file):
    GPU_ID = 2
    caffe.set_mode_gpu()
    caffe.set_device(GPU_ID)
    f = h5py.File(file,'r')
    net = caffe.Net('deploy.prototxt',
		        'resnet50_cvgj_iter_320000.caffemodel',
		        caffe.TEST)

    #im = caffe.io.load_image('../../data-imagenet/test_imagenet_val1/ILSVRC2012_val_00012352.JPEG')
    print(f['input'][0])
    net.blobs['data'].data[...] =f['input'][0]
    net.forward()
    f = h5py.File('caffe-dump-nvidia.h5','w')
    sbgrp=f.create_group("lyr")
    i=0
    for layer in net.blobs.keys():
        print(layer)
        print(i)
        sbsbgrp=sbgrp.create_group(str(i))
        #if i==0:
        #    sbsbgrp.create_dataset("input",data=f['input'][0])
        sbsbgrp.create_dataset("output",data=net.blobs[layer].data)
        sbsbgrp.attrs['Name']=layer
        sbsbgrp.attrs['DataType']=9
        i+=1
    f.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', help='input data file')
    args = parser.parse_args()
    dump_inference(args.infile)


if __name__ == '__main__':
    main()
