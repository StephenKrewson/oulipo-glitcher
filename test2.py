import base64, binascii, sys, winsound, random
from collections import defaultdict
from os import walk, path
import math as m
from bisect import bisect_left

# Get notes and frequencies in Hertz [37 - 5632.08 Hz]
notes = ('A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#')
freqs = []
[freqs.append(37 * m.exp(p * m.log(2)/12)) for p in range(88)]

def decToNote(d, array):
    return d/255 * (len(array) - 1)

def glitchFile(filename):
    d = defaultdict(lambda:0)
    bells = 0
    locations = []
    with open(filename, 'rb') as f:
        data = bytearray(f.read())
    for x in range(len(data)):
        print(chr(data[x]))
        d[data[x]] += 1
        if data[x] == 7:
            bells += 1
            locations.append(x/len(data))
            if x % 7 == 0:
                data.insert(x, 90)
    with open(filename.split('.')[0] + 'MOD.' + filename.split('.')[1], 'wb') as target:
        target.write(data)
for dirpath, dirnames, filenames in walk(path.abspath(sys.argv[1])):
    for i in filenames:
        files = path.join(dirpath, i)
        if files[-7:-4] != 'MOD':
            glitchFile(files)
