mkdir output 
mkdir build 
cd build 
## cmake -DCMAKE_INSTALL_PREFIX:PATH=../output ..
cmake ..
cmake --build . --target install --config Release