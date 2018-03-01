import numpy as np
import ast

HEADER_OFFSET=2048

def _parse_header(header):
    header = header[:header.find(0)].decode()
    rows, dtype = ast.literal_eval(header)
    return rows, dtype

def _generate_header(dtype, rows):
    header = str((rows, np.dtype(dtype).descr))
    header += (HEADER_OFFSET - len(header)) * '\0'
    return header.encode()

def openShmArray(path):
    fd = open(path, 'rb')
    header = fd.read(HEADER_OFFSET)
    rows, dtype = _parse_header(header)
    return np.memmap(path, dtype=dtype, shape=(rows,), mode='r+', offset=HEADER_OFFSET)

def createShmArray(path, dtype, rows):
    fd = open(path, 'wb')
    header = _generate_header(dtype, rows)
    fd.write(header)
    return np.memmap(path, dtype=dtype, shape=(rows,), mode='r+', offset=HEADER_OFFSET)
