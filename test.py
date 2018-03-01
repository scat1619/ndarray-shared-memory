#! /usr/bin/env python
import sys
from ndarray_shared_memory import *

FILE_PATH = '/tmp/t.shm'

def test_open():
    ar = openShmArray(FILE_PATH)
    ar['a'][1] = 1024
    assert ar['a'][0] == 1
    print (ar)

def test_create():
    ar = createShmArray(FILE_PATH, [('a', np.int64), ('b', np.float64)], 3)
    ar['a'][0] = 1
    ar['b'][1] = 2.0

if __name__ == '__main__':
    if sys.argv[1] == 'open':
        test_open()
    elif sys.argv[1] == 'create':
        test_create()
