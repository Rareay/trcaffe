

cd int8_mode
rm build -rf
mkdir build
cd build
cmake ..
make
cd ..
./build/app
cd ..

echo " "
echo "done!"