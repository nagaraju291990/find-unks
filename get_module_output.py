import glob
import sys
import subprocess
from pathlib import Path
import re

given_dir = sys.argv[1]

fp1 = open('module_out.txt','w')
#path = Path(r''+root_dir)
for filename in glob.iglob(given_dir + '**/**/**', recursive=False):
	#print("Sentence id=", filename)
	#print(filename)
	if(re.search('/morph.*tmp.*out', filename)):
		print(filename)
		with open(filename, encoding="utf8", errors='ignore') as fp:
			morph_lines = fp.read().split("\n") # Create a list containing all lines
		#fp.close()

		for morph_line in morph_lines:
			print(morph_line)
			#if(re.search('unk,,,', morph_line)):
			#	fp1.write(morph_line + "\n")
				#print(morph_line)