import os
import sys
import time

mode = sys.argv[1]
wl = ["2k","4k","2k","2k","2k","512k","2k","2k","2k","2k"]
start = time.time()
 
if mode == "basiclustre":
	for i in range(len(wl)):
		os.system("/home/lustre/software/ior/bin/ior -w -t "+wl[i]+" -b "+wl[i]+" -F -m -e -o /lustre/hdd4/test > /dev/null")
		time.sleep(1)
	os.system("/home/lustre/software/ior/bin/ior -w -t 1m -b 16g -F -m -e -o /lustre/hdd4/ckfile > /dev/null")

elif mode == "pflhdd":
	for i in range(len(wl)):
		os.system("/home/lustre/software/ior/bin/ior -w -t "+wl[i]+" -b "+wl[i]+" -F -m -e -o /lustre/hdd1/dn4test0,4m,/lustre/hdd3/dn4test1,16g > /dev/null")
		time.sleep(1)
	os.system("/home/lustre/software/ior/bin/ior -w -t 1m -b 16g -F -m -e -o /lustre/hdd1/ckfile0,4m,/lustre/hdd3/ckfile1,16g > /dev/null")

elif mode == "pflssd":
	for i in range(len(wl)):
		os.system("/home/lustre/software/ior/bin/ior -w -t "+wl[i]+" -b "+wl[i]+" -F -m -e -o /lustre/ssd1/dn4test0,4m,/lustre/hdd3/dn4test1,16g > /dev/null")
		time.sleep(1)
	os.system("/home/lustre/software/ior/bin/ior -w -t 1m -b 16g -F -m -e -o /lustre/ssd1/ckfile0,4m,/lustre/hdd3/ckfile1,16g > /dev/null")

else:
	print("mode : basiclustre, pflhdd, pflssd ")
end = time.time()

print("dn4 : "+str("{0:0.2f}".format(end-start)))
