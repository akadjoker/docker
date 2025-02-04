make -DOPENCV_EXTRA_MODULES_PATH=/content/opencv_contrib/modules  \
       -DBUILD_SHARED_LIBS=OFF \
       -DBUILD_TESTS=OFF \
       -DBUILD_PERF_TESTS=OFF \
       -DBUILD_EXAMPLES=OFF \
       -DWITH_OPENEXR=OFF \
       -DWITH_CUDA=ON \
       -DWITH_CUBLAS=ON \
       -DWITH_CUDNN=ON \
       -DOPENCV_DNN_CUDA=ON \
       /content/opencv

make -j8 install
