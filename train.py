cd darknet

sed -i 's/OPENCV=0/OPENCV=1/' Makefile
sed -i 's/GPU=0/GPU=1/' Makefile
sed -i 's/CUDNN=0/CUDNN=1/' Makefile
sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile

make

cp obj.data darknet/build/darknet/x64/data


cp obj.names darknet/build/darknet/x64/data


./darknet detector train 'darknet/build/darknet/x64/data/obj.data' yolov3-tiny.cfg yolov3-tiny.conv.11 -dont_show




