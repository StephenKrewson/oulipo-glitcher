import base64, binascii, sys
from collections import defaultdict
from os import walk, path

def glitchFile(filename):
    d = defaultdict(lambda:0)
    bells = 0
    locations = []
    with open(filename, 'rb') as f:
        data = bytearray(f.read())
    for x in range(len(data)):
        d[data[x]] += 1
        if data[x] == 7:
            bells += 1
            locations.append(x/len(data))
            if x % 7 == 0:
                data.insert(x, 7)
    with open(filename.split('.')[0] + 'MOD.' + filename.split('.')[1], 'wb') as target:
        target.write(data)
    print(locations)
for dirpath, dirnames, filenames in walk(path.abspath(sys.argv[1])):
    for i in filenames:
        files = path.join(dirpath, i)
        if files[-7:-4] != 'MOD':
            glitchFile(files) 

'''
for key in d:
    try:
        print(chr(key), d[key])
        howmany += 1
    except:
        UnicodeEncodeError
'''
