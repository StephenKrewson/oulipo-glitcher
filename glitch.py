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
			
			print("starting byte", jpeg_start)
			
			index_chars(bytes[jpeg_start:])
			
			
			
			# now open up a .jpg file in out-dir, write headers to it
		
		else:
			print("PNG not supported yet.")

			
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
	
	# interpret as utf-8, ignoring errors
	chars = byte_array.decode('utf-8', 'ignore')

	for char in chars:
		d[char] += 1
		
	
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
	printHistogram(d)
	return (d, l)
	

def printHistogram(d):                      # Function 2
    '''Prints out chars by frequency'''
    ordered = sorted(d, key=d.get, reverse=False)
    max_val = d[ordered[-1]]                # Normalize max value to 50 chars
    total = 0                               # 
    for key in ordered:
        total += d[key]
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