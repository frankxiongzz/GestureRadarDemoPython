
#???????dll??

import os
import sys
from ctypes import *



dll = CDLL('D:\GestureRadarDemoPython\GestureRadarSDK.dll')


def recvRAW(x, y, reserve, z):
    print("x: %d, y: %d, z:%d" % (x, y, z))
    return 0


def recvRecognise(strName, score):
    print("x: %d, y: %d, z:%d" % (x, y, z))
    return 0


if __name__ == '__main__':

    callbackRAW = CFUNCTYPE(c_void_p, c_int32, c_int32, c_int32, c_int32)
    callbackRawHandler = callbackRAW(recvRAW)
    callbackRecognise = CFUNCTYPE(c_void_p, c_char_p, c_double)
    callbackRecogniseHandler = callbackRecognise(recvRecognise)

    # ??????
    #namelist ??
    NameList = ["Circle", "Triangle"]

    string1 = 'Circle'
    string2 = 'Triangle'

    b_string1 = string1.encode('utf-8')
    b_string2 = string2.encode('utf-8')

    p = c_char_p*2
    namelist = p(c_char_p(b_string1),c_char_p(b_string2))

    dll.registerLoopCallBack(callbackRawHandler, callbackRecogniseHandler, True, 2, namelist)

    a = input()
    print("Start Rec")
    # ??????
    dll.releaseLoopCallBack()
