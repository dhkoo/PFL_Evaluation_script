import time
import os
import random
import subprocess


workload = ['2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','16k','16k','16k','16k','16k','16k','16k','16k','16k','16k','16k','16k','16k','16k','16k','16k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','64k','64k','64k','64k','64k','64k','64k','64k','64k','64k','64k','64k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','256k','256k','256k','256k','256k','256k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','4m','4m','4m','4m','4m','4m','4m','4m','8m','8m','8m','8m','8m','8m','8m','8m','8m','8m','16m','16m','16m','16m','32m','32m','32m','64m','128m','128m','256m','256m','256m','512m','1g','1g','4g','4g','16g','16g']

#------- # of iteration --------
basiclustre = []
pflhdd = []
pflssd = []
pflssd_1 = []
iterate = 50

for i in range(0,iterate):

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
	print(workload)
	print(tssize)


	start1 = time.time()
	for i in range(0,len(workload)):
		os.system("ior -w -t "+tssize[i]+" -b" +workload[i]+ "-F -m -e -o /lustre/hdd4/testfile"+str(i)+" &")
		if (i+1)%16 == 0:
			os.system("sleep 0.5")

	while True:
		check = subprocess.check_output('ps', shell=True)
		if str(check).find('ior') == -1:
			print("end")
			break
		time.sleep(0.5)

	end1 = time.time()
	time.sleep(1)

	elap1 = end1 - start1
	basiclustre.append(elap1)

	#----------------------------------------------
	index1 = 0
	index2 = 1

	start2 = time.time()
	for i in range(0,len(workload)):
		os.system("ior -w -t "+tssize[i]+" -b" +workload[i]+ "-F -m -e -o /lustre/hdd1/testfile"+str(index1)+",4m,/lustre/hdd3/testfile"+str(index2)+",16g &")
		if (i+1)%16 == 0:
			os.system("sleep 0.5")

		index1 = index1 + 2
		index2 = index2 + 2

	while True:
		check = subprocess.check_output('ps', shell=True)
		if str(check).find('ior') == -1:
			print("end")
			break
		time.sleep(0.5)

	end2 = time.time()
	time.sleep(1)

	elap2 = end2 - start2
	pflhdd.append(elap2)

	#---------------------------------------------

	start3 = time.time()
	for i in range(0,len(workload)):
		os.system("ior -w -t "+tssize[i]+" -b" +workload[i]+ "-F -m -e -o /lustre/ssd1/testfile"+str(index1)+",4m,/lustre/hdd3/testfile"+str(index2)+",16g &")
		if (i+1)%16 == 0:
			os.system("sleep 0.5")

		index1 = index1 + 2
		index2 = index2 + 2

	while True:
		check = subprocess.check_output('ps', shell=True)
		if str(check).find('ior') == -1:
			print("end")
			break
		time.sleep(0.5)

	end3 = time.time()
	time.sleep(1)

	elap3 = end3 - start3
	pflssd.append(elap3)

#===============================================

	start4 = time.time()
	for i in range(0,len(workload)):
		os.system("ior -w -t "+tssize[i]+" -b" +workload[i]+ "-F -m -e -o /lustre/ssd1/testfile"+str(index1)+",4m,/lustre/hdd4/testfile"+str(index2)+",16g &")
		if (i+1)%16 == 0:
			os.system("sleep 0.5")

		index1 = index1 + 2
		index2 = index2 + 2

	while True:
		check = subprocess.check_output('ps', shell=True)
		if str(check).find('ior') == -1:
			print("end")
			break
		time.sleep(0.5)

	end4 = time.time()
	time.sleep(1)

	elap4 = end4 - start4
	pflssd_1.append(elap4)

f = open("/home/lustre/lfs/python/wlresultFile1", 'w')
f.write("Basic Lustre :" +str(basiclustre)+"\n")
f.write("PFL(HDD) :" +str(pflhdd)+"\n")
f.write("PFL(SSD) :" +str(pflssd)+"\n")
f.write("PFL(SSD)_1 :" +str(pflssd_1)+"\n")
f.close()
