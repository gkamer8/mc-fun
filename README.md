
# Set Up / Installation

I installed OpenMC from source. There are instructions [here](https://docs.openmc.org/en/stable/quickinstall.html#manually-installing-from-source). On Mac, you can run:

```
brew install llvm cmake xtensor hdf5 python libomp libpng
```

to install the prerequisites. Then run:

```
export CXX=/opt/homebrew/opt/llvm/bin/clang++
```

so that the recently installed compiler is used.

Then run:

```
git clone --recurse-submodules https://github.com/openmc-dev/openmc.git
cd openmc
mkdir build && cd build
cmake ..
make
sudo make install
```

which will clone the openmc directory and compile it.

## Install Python Package

Now it makes sense to create a python venv and install openmc. Go to the root dircetory of this project and run:

```
python3 -m venv venv
source venv/bin/activate
cd openmc
python3 -m pip install .
```

### Common Error on MacOS

If you get:

```
CMake Error at /opt/homebrew/Cellar/cmake/3.30.3/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:233 (message):
  Could NOT find OpenMP_C (missing: OpenMP_C_FLAGS OpenMP_C_LIB_NAMES)
Call Stack (most recent call first):
  /opt/homebrew/Cellar/cmake/3.30.3/share/cmake/Modules/FindPackageHandleStandardArgs.cmake:603 (_FPHSA_FAILURE_MESSAGE)
  /opt/homebrew/Cellar/cmake/3.30.3/share/cmake/Modules/FindOpenMP.cmake:600 (find_package_handle_standard_args)
  CMakeLists.txt:84 (find_package)
```

Try going to the CMakeLists.txt file in /openmc and replacing the line `find_package(OpenMC REQUIRED)` with:

```
if(APPLE)
  if(CMAKE_C_COMPILER_ID MATCHES "Clang")
    set(OpenMP_C "${CMAKE_C_COMPILER}")
    set(OpenMP_C_FLAGS "-fopenmp=libomp -Wno-unused-command-line-argument")
    set(OpenMP_C_LIB_NAMES "omp")
    set(OpenMP_omp_LIBRARY "/opt/homebrew/opt/libomp/lib/libomp.dylib")
  endif()
  if(CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    set(OpenMP_CXX "${CMAKE_CXX_COMPILER}")
    set(OpenMP_CXX_FLAGS "-fopenmp=libomp -Wno-unused-command-line-argument")
    set(OpenMP_CXX_LIB_NAMES "omp")
    set(OpenMP_omp_LIBRARY "/opt/homebrew/opt/libomp/lib/libomp.dylib")
  endif()
endif()

find_package(OpenMP REQUIRED)
```

Then re-run the cmake command. Then the make and make install.

### Manging Git Inside Git

Note that if you followed the above steps, you might have a git repo inside a git repo - which can be annoying. I just ignored the whole thing (see: .gitignore). You may also need to get rid of any .git related files inside `openmc` to reduce any complication.

## Get Data

`TODO`
