import locale, re
from collections import defaultdict

def guess_notepad_encoding(filepath, default_ansi_encoding=None):
    with open(filepath, 'rb') as f:
        data = f.read(3)
    if data[:2] in ('\xff\xfe', '\xfe\xff'):
        return 'utf-16'
    if data == u''.encode('utf-8-sig'):
        return 'utf-8-sig'
    # presumably "ANSI"
    return default_ansi_encoding or locale.getpreferredencoding()

print(guess_notepad_encoding('manet2.jpg'))

with open('manet2.jpg', 'rb') as f:
    shitt = f.read().decode('ASCII', 'ignore')
    for i in f.readlines():
        print(i.strip().decode('utf-8-sig', 'ignore'))

def indexChars(input_string):               # Function 1
    '''Gets freqs of all chars, indexes alphabetical chars'''
    d = defaultdict(lambda: 0)                                  # Stores char types and freqs
    l = []                                  # Indexes all [a-zA-Z] chars
    for i in range(len(input_string)):                    
        try:
            if input_string[i] in d:
                d[input_string[i]] += 1
            try:
                if re.match('[a-zA-Z]', input_string[i]):
                    l.append((input_string[i], i))
            except UnicodeDecodeError:
                pass
            else:
                d[input_string[i]] += 1
        except UnicodeDecodeError:
            pass
    return (d, l)

def printHistogram(d):                      # Function 2
    '''Prints out chars by frequency'''
    ordered = sorted(d, key=d.get, reverse=False)
    max_val = d[ordered[-1]]                # Normalize max value to 50 chars
    total = 0                               # 
    for key in ordered:
        total += d[key]
        #hist = key * (int(int(d[key])) * 50 / int(max_val))
        print(key, d[key], total)

printHistogram(indexChars(shitt)[0])