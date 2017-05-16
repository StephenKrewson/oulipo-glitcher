# Stephen Krewson, 15 May 2017 (created 2014, revised 2015)
#
# Oulipean Image Glitching
#
# Usage: python3 glitch.py <input-imgs-dir> <output-imgs-dir>
#
# Supported filetypes: JPEG, PNG


from collections import defaultdict
import imghdr
from os import walk, path
import re
import sys


def glitch(img, type, lexicon):
	'''Oulipean glitch of binary data within JPEG or PNG'''
	# first step is to open the file and convert to byte array
	with open(img,'rb') as f:
		bytes = bytearray(f.read())
	
		# skip headers if it's a jpeg
		if type is 'jpeg':
			jpeg_start = skip_jpeg_header(bytes)
			scan_area = bytes[jpeg_start:]
			
			# get byte frequencies and alphabet locations
			indexed = index_chars(scan_area)
			
			words_found = findWords(indexed[1], lexicon)
			
			# now open up a .jpg file in out-dir, write headers to it
		
		else:
			print("PNG not supported yet.")

			
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
			
			
			
def skip_jpeg_header(byte_array):
	'''skips to the start of the scan in a jpeg; input is byte array, see:
	https://github.com/snorpey/glitch-canvas/blob/master/src/glitch/jpgHeaderLength.js
	'''
	start_scan = 417
	for i in range(len(byte_array) - 1):
		if byte_array[i] is 0xff and byte_array[i+1] is 0xDA:
			start_scan = i + 2
			break
	return start_scan


def index_chars(byte_array):
	# counts for all utf-8 codepoints in the scan section of the image
	d = defaultdict(lambda: 0)
	
	# list of tuples of (char, index) within the byte array
	l = []
	
	# interpret as ASCII, ignoring errors (another version use utf-8 + accents)
	chars = byte_array.decode('ascii', 'ignore')

	# increment counts
	for i,char in enumerate(chars):
		d[char] += 1
		# remember positions of all letters
		if re.match('[a-zA-Z]', char):
			l.append((char, i))
		
	
	'''
	for i in range(len(byte_array)):
	
		# try to convert to unicode
		try:
			char = byte_array[i].decode('utf-8')
			d[char] += 1
			
			if re.match('[a-zA-Z]', char):
				l.append((char, i))
			
		except UnicodeDecodeError:
			pass'''
			
	
	return (d, l)
	

def printHistogram(d):                      # Function 2
    '''Prints out chars by frequency'''
	# sort in ascending order of most frequent
    ordered = sorted(d, key=d.get, reverse=False)
    max_val = d[ordered[-1]]
	
	# print out that character in proportion to its frequency
    for key in ordered:
		# but normalize such that the most frequent is 50 chars long
        hist = key * round(d[key] * 50 / max_val)
        print(key, hist)
	
	
# Initialize the program; get params and check file
def main():

	# there should only be three arguments
	if (len(sys.argv) is not 3):
		exit("Usage: python3 glitch.py <input-imgs-dir> <output-imgs-dir>")
		
	# need to load the list of words
	lexicon = set(open('dict.txt','r').read().lower().split())	
	
		
	# here is where we want to capture some options from the user
	# or keep it on the CLI and more minimal?? (I like that better)
	# cite: oulipo compendium and https://snorpey.github.io/jpg-glitch/
	# also the amazing twitter/mammoth project that doesn't allow E
	# constraints: don't use PIL, try to have everything running on static
	# webpage eventually; simplest ways to work with images
	# future ideas: incorporate word embeddings, like modulate slope of word2vec
	# also: learn to make python3 expressive with glitch just like python2
	# also also: connection to pedagogy and cs50 whodunit pset4
		
	# go through each file in <input-dir>; we use the absolute path
	# so that ANY directory on the machine can be specified
	for dirpath, dirnames, filenames in walk(path.abspath(sys.argv[1])):
		for i in filenames:
			file = path.join(dirpath, i)
			
			# figure out if this file is a jpeg or png (otherwise ignore)
			imgtype = imghdr.what(file)
			if imgtype not in ['jpeg','png']:
				continue
				
			# assuming we have valid image...
			print("glitching", i)
			glitch(file, imgtype, lexicon)
			
	# end of main()
	print("hippo")


if __name__ == '__main__':
	main()