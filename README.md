# inference-results-NVcaffe


- Download the .caffemodel from here : Google
https://drive.google.com/open?id=0B6VgjAr4t_oTTDh2SVJIa2VkZVU

- The imagenet data I used for inference are present in test.txt
- resize.py to resize the imagenet data keeping the aspect ratio
- `python3 netForward.py image.h5` to store each output layer
- caffe-dump.py to compare two output .h5 files layer by layer
- `./run.sh` to launch the testing on the test.txt data
