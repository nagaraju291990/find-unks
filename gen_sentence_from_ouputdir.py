import glob
import sys
import subprocess
from pathlib import Path
import re

given_dir = sys.argv[1]

fp1 = open('system_out.txt','w')
#path = Path(r''+root_dir)
for filename in glob.iglob(given_dir + '**/**/**', recursive=False):
	#print(filename)
	if(re.search('/wordgen.tmp.out', filename)):
		#print(filename)
		with open(filename, encoding="utf8", errors='ignore') as fp:
			morph_lines = fp.read().split("\n") # Create a list containing all lines
		#fp.close()

		for morph_line in morph_lines:
			#print(morph_line)
			if(not re.search('\(\(', morph_line) and not re.search(r'\)\)', morph_line) and re.search(r'\t', morph_line)):
				token = morph_line.split("\t")[1]
				fp1.write(token+" ")
		fp1.write("\n")
				#print(morph_line)