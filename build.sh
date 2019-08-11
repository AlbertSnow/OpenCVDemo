mkdir build 
cd build 
## cmake -DCMAKE_INSTALL_PREFIX:PATH=../build/bin ..
cmake ..
cmake --build . --target install --config Release