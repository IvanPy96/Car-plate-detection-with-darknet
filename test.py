cd darknet

sed -i 's/OPENCV=0/OPENCV=1/' Makefile
sed -i 's/GPU=0/GPU=1/' Makefile
sed -i 's/CUDNN=0/CUDNN=1/' Makefile
sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile

make

./darknet detector test 'darknet/build/darknet/x64/data/obj.data' yolov3-tiny.cfg 'darknet/build/darknet/x64/data/backup/yolov3-tiny_1000_1.weights' 'darknet/build/darknet/x64/data/obj/example.jpg' -thresh 0.5

