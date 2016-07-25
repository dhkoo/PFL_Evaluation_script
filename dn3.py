import os
import time
import sys

lst = []
mode = sys.argv[1]

start = time.time()

if mode == "basiclustre":
	for i in range(2500):
		os.system("/home/lustre/software/ior/bin/ior -w -t 2k -b 2k -F -m -e -o /lustre/hdd4/dn3testfile1 > /dev/null &")
		os.system("/home/lustre/software/ior/bin/ior -w -t 2k -b 2k -F -m -e -o /lustre/hdd4/dn3testfile2 > /dev/null &")
		os.system("/home/lustre/software/ior/bin/ior -w -t 2k -b 2k -F -m -e -o /lustre/hdd4/dn3testfile3 > /dev/null &")
		os.system("/home/lustre/software/ior/bin/ior -w -t 2k -b 2k -F -m -e -o /lustre/hdd4/dn3testfile4 > /dev/null ")
elif mode == "pflhdd":
	for i in range(2500):
		os.system("/home/lustre/software/ior/bin/ior -w -t 2k -b 2k -F -m -e -o /lustre/hdd1/dn3testfile1 > /dev/null &")
		os.system("/home/lustre/software/ior/bin/ior -w -t 2k -b 2k -F -m -e -o /lustre/hdd1/dn3testfile2 > /dev/null &")
		os.system("/home/lustre/software/ior/bin/ior -w -t 2k -b 2k -F -m -e -o /lustre/hdd1/dn3testfile3 > /dev/null &")
		os.system("/home/lustre/software/ior/bin/ior -w -t 2k -b 2k -F -m -e -o /lustre/hdd1/dn3testfile4 > /dev/null ")
elif mode == "pflssd":
	for i in range(2500):
		os.system("/home/lustre/software/ior/bin/ior -w -t 2k -b 2k -F -m -e -o /lustre/ssd1/dn3testfile1 > /dev/null &")
		os.system("/home/lustre/software/ior/bin/ior -w -t 2k -b 2k -F -m -e -o /lustre/ssd1/dn3testfile2 > /dev/null &")
		os.system("/home/lustre/software/ior/bin/ior -w -t 2k -b 2k -F -m -e -o /lustre/ssd1/dn3testfile3 > /dev/null &")
		os.system("/home/lustre/software/ior/bin/ior -w -t 2k -b 2k -F -m -e -o /lustre/ssd1/dn3testfile4 > /dev/null ")

else:
	print("mode : basiclustre, pflhdd, pflssd")

end = time.time()

print("dn3 : "+str("{0:0.2f}".format(end-start)))
