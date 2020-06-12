"""===========================================================================
    此檔案適用在 linux 編譯環境 !! 
	
    編譯指令 : 
        python3 setup.py build
  
    include_dirs : opencv 標頭檔路徑
    library_dirs : opencv library 路徑
    libaries : opencv library 檔名
    

==============================================================================="""

from setuptools import setup, Extension

setup(ext_modules=[
    Extension(
        'cxxFunc', ['cxxFunc.cpp'],
        extra_compile_args=["-std=c++14", "-O3"],
        include_dirs=['.', '/opt/intel/openvino_2019.3.334/opencv/include'],
        library_dirs=['/opt/intel/openvino_2019.3.334/opencv/lib'],
        libraries=[
            'opencv_highgui', 'opencv_video',
            'opencv_videoio', 'opencv_dnn', 'opencv_imgproc',
            'opencv_core'
        ]),
])
