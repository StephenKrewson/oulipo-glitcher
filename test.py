import locale, re, sys, string
from collections import defaultdict
from os import walk, path
import time
start_time = time.clock()

lexicon = set(open('dict2.txt','r').read().lower().split())


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

def findWords(l, lexicon):                  # Function 3
    '''Finds English words in alphabetical chars'''
    max_len = max(list(map(len, lexicon)))        # Longest word in the set of words
    words_found = []                        # set of words found, starts empty
    for i in range(len(l)):                # for each possible starting position in the corpus
        chunk = l[i:i+max_len]              # chunk that is the size of the longest word
        for j in range(len(chunk)):        # loop to check each possible subchunk
            word = chunk[:j]
            test = ''                       # Grap letters from the tuple
            for k in range(len(word)):
                test += word[k][0].lower()  # Build up word
            if test in lexicon and len(test) > word_min:
                if oulipo == 1:             # Option for N + ? glitch
                    same_length = sorted([x for x in lexicon if len(x) == len(test)])
                    new_word = same_length[(same_length.index(test) + shift2) % len(same_length)]
                    #print test, new_word, shift2, len(same_length) 
                    for y in range(len(word)):
                        if word[y][0].isupper():
                            word[y] = (new_word[y].upper(), word[y][1])
                        else: word[y] = (new_word[y], word[y][1])
                    words_found.append(word)
                else:
                    words_found.append(word)# Add list of tuples to master word list
    return words_found                      # Returns array of valid words and their indexes

word_min = int(sys.argv[1])
oulipo = int(sys.argv[2])
shift2 = int(sys.argv[3])
delete = int(sys.argv[4])
shift = int(sys.argv[5])
printHistogram(indexChars(shitt)[0])

inputString = indexChars(shitt)[1]

holder = findWords(inputString, lexicon)
for word in holder:
    string1 = ''
    for letter in word:
        string1 += letter[0].lower()
    print(string1)

def glitchFile(filename):
    '''Transforms found words in JPG and writes a modified file'''
    with open(filename,'rb') as f:          # Open JPEG and read it in binary mode
        input_string = f.read().decode('ASCII', 'ignore')             
    results = indexChars(input_string)      # Call indexChars function
    words_found = findWords(results[1], lexicon)
    new_string = input_string               # Build up new string from substrings of input
    for i in words_found:
        for j in i:
            char_val = string.ascii_letters.index(j[0]) 
            if delete == 1:
                replace = ' '               # Semantic content 'whited' out
            else: replace = string.ascii_letters[(char_val + shift) % 52]
            new_string = new_string[:j[1]] + replace + new_string[j[1]+1:]
    new_file = filename.split('.')[0] + 'MOD.' + filename.split('.')[1]
    #print(new_string)
    with open(new_file, 'wb') as f:
        f.write(bytearray(new_string, 'ANSI'))

for dirpath, dirnames, filenames in walk(path.abspath(sys.argv[6])):
    for i in filenames:
        files = path.join(dirpath, i)
        if files[-7:-4] != 'MOD':
            print(files)
            print(glitchFile(files))               # Call glitch function on original files
print('Program:\t{0}\nDuration (s):\t{1}\nDirectory:\t{2}\nNo. of files:\t{3}\nHistogram?\t{4}\nWord length >\t{5}\nDelete words?\t{6}\nChars shifted:\t{7}\nOulipo swap?\t{8}\nIf yes, N + ?:\t{9}'.format(
    path.basename(__file__), time.clock() - start_time, dirpath, len(filenames), hist, word_min, delete, shift, oulipo, shift2))