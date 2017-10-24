../../../opt/caffe/caffe/build/tools/caffe test \
--model="test.prototxt" \
--iterations="1000" \
--weights="resnet50_cvgj_iter_320000.caffemodel" \
--gpu "0" 2>&1 | tee run.log
