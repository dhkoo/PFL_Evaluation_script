import re
import sys

f = open(sys.argv[1], 'r') 
lines = f.readlines() 
pattern = r'^write\s\s\s\s\s(\d+[.]\d+)'
total_sum = 0
count = 0

for line in lines:
	match = re.search(pattern,line)
	if match:
		total_sum+=float(match.group(1))
		count = count + 1

mean = total_sum/float(count)
print(mean)

f.close()
