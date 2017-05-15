# Stephen Krewson, 15 May 2017
#
# Oulipean Image Glitching
#
# Usage: python glitch.py <input-dir> <output-dir>


import sys


# Initialize the program; get params and check file
def main():

	# there should only be three arguments
	if (len(sys.argv) is not 3):
		exit("Usage: python glitch.py <input-dir> <output-dir>")
	
	print("hippo")


if __name__ == '__main__':
	main()