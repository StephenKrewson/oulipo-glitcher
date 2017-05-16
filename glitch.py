# Stephen Krewson, 15 May 2017 (created 2014, revised 2015)
#
# Oulipean Image Glitching
#
# Usage: python3 glitch.py <input-imgs-dir> <output-imgs-dir>
#
# Supported filetypes: JPEG, PNG


import imghdr
from os import walk, path 
import sys


def glitch(img, type):
	'''Oulipean glitch of binary data within JPEG or PNG'''
	# first step is to skip over the headers
	with open(img,'rb') as f:
	
		input_string = f.read().decode('ASCII', 'ignore')
		print(input_string)
	
		if type is 'jpeg':
			print(img)
		
		else:
			print("PNG not supported yet.")
		


# Initialize the program; get params and check file
def main():

	# there should only be three arguments
	if (len(sys.argv) is not 3):
		exit("Usage: python3 glitch.py <input-imgs-dir> <output-imgs-dir>")
		
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
			glitch(file, imgtype)
			
	# end of main()
	print("hippo")


if __name__ == '__main__':
	main()