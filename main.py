"""
	執行前 : 因為使用 openvino 裡面的 opencv ，所以需在啟動前輸入 啟動 openvino 指令 !! 

"""
import numpy as np
import ctypes
import cv2
import time
import os
import copy

cxx = ctypes.cdll.LoadLibrary(
    f"./build/lib.linux-x86_64-3.7/cxxFunc.cpython-37m-x86_64-linux-gnu.so")
cxx.donothing.restype = ctypes.POINTER(ctypes.c_uint8)


def test(img):
    start = time.time()
    h = img.shape[0]
    w = img.shape[1]
    rptr = cxx.donothing(
        img.astype(np.uint8).ctypes.data_as(ctypes.c_char_p), h, w)
    r1dimg = np.ctypeslib.as_array(rptr, (h * w * 3, )).copy()
    cxx.release(rptr)
    rimg = r1dimg.reshape((h, w, 3))
    print((time.time() - start) * 1000)
    return rimg


def test2(img):
    start = time.time()
    rimg = copy.deepcopy(img)
    print((time.time() - start) * 1000)
    return rimg


if __name__ == '__main__':
    #     colormap = ColorMap()
    img = cv2.imread("./cube.jpg")
    rimg = test2(img)
    rimg = test(img)
    cv2.imwrite("result.jpg", rimg)
