import time
import os
import random
import sys

mode = sys.argv[1]

workload = ["32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","32k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","64k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","128k","256k","256k","256k","256k","512k","512k","512k","512k","512k","512k","512k","512k","1m","1m","1m","1m","1m","2m","2m"]

for i in range(900):
	workload.append("4k")
for i in range(320):
	workload.append("8k")
for i in range(100):
	workload.append("16k")


random.shuffle(workload)

tssize = []
tmp = []

for i in range(0,len(workload)):
	tmp.append(0)
	tssize.append("")

for i in range(0,len(workload)):
	if workload[i].find('k') != -1:
		tmp[i] = int(workload[i].replace('k',""))
	if workload[i].find('m') != -1:
		tmp[i] = int(workload[i].replace('m','')) * 1024
	if workload[i].find('g') != -1:
		tmp[i] = int(workload[i].replace('g','')) * 1024 * 1024	


for i in range(0,len(workload)):
	if tmp[i] < 1024:
		tssize[i] = str(tmp[i])+'k'
	else:
		tssize[i] = "1m" 

index1 = 0
index2 = 1

start = time.time()
if mode == "basiclustre":
	for i in range(0,len(workload)):
		os.system("ior -w -t "+tssize[i]+" -b" +workload[i]+ "-F -m -e -o /lustre/hdd4/testfile"+str(i)+" > /dev/null")
		if i%100 == 0:
			time.sleep(1)

elif mode == "pflhdd":
	for i in range(0,len(workload)):
		os.system("ior -w -t "+tssize[i]+" -b" +workload[i]+ "-F -m -e -o /lustre/hdd1/testfile"+str(index1)+",4m,/lustre/hdd3/testfile"+str(index2)+",16g > /dev/null")
		if i%100 == 0:
			time.sleep(1)
		index1 = index1 + 2
		index2 = index2 + 2

elif mode == "pflssd":
	for i in range(0,len(workload)):
		os.system("ior -w -t "+tssize[i]+" -b" +workload[i]+ "-F -m -e -o /lustre/ssd1/testfile"+str(index1)+",4m,/lustre/hdd3/testfile"+str(index2)+",16g > /dev/null")
		if i%100 == 0:
			time.sleep(1)
		index1 = index1 + 2
		index2 = index2 + 2
end = time.time()

print("dn2 : "+str("{0:0.2f}".format(end-start)))
