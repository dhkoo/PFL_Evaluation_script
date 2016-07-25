import time
import os
import random


workload = ['2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','2k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','4k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','8k','16k','16k','16k','16k','16k','16k','16k','16k','16k','16k','16k','16k','16k','16k','16k','16k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','32k','64k','64k','64k','64k','64k','64k','64k','64k','64k','64k','64k','64k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','128k','256k','256k','256k','256k','256k','256k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','512k','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','1m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','2m','4m','4m','4m','4m','4m','4m','4m','4m','8m','8m','8m','8m','8m','8m','8m','8m','8m','8m','16m','16m','16m','16m','32m','32m','32m','64m','128m','128m','256m','256m','256m','512m','1g','2g','4g','8g','16g','32g','64g']

index = 0
iterative = 5
threads = 16
basic_elapsedtime_array = []
pflhdd_elapsedtime_array = []
pflssd_elapsedtime_array = []
filesizes_array = []

while index < iterative:

	#filesizes = ['','','','','','','','']
	#transfersizes = ['','','','','','','','']
	#tmp = [0,0,0,0,0,0,0,0]
	filesizes = ['','','','','','','','','','','','','','','','']
	transfersizes = ['','','','','','','','','','','','','','','','']
	tmp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

	for i in range(0,threads):
		filesizes[i] = workload[random.randrange(0,400)]
		if filesizes[i].find('k') != -1:
			tmp[i] = int(filesizes[i].replace('k',""))
		if filesizes[i].find('m') != -1:
			tmp[i] = int(filesizes[i].replace('m','')) * 1024
		if filesizes[i].find('g') != -1:
			tmp[i] = int(filesizes[i].replace('g','')) * 1024 * 1024

	tmp.sort()

	for i in range(0,threads):
		if tmp[i] < 1024:
			filesizes[i] = str(tmp[i])+'k'
			transfersizes[i] = filesizes[i]
		if tmp[i] >= 1024 and tmp[i] < 1024*1024:
			filesizes[i] = str(tmp[i]/1024)+'m'
			transfersizes[i] = '1m'
		if tmp[i] > 1024*1024:
			filesizes[i] = str(tmp[i]/(1024*1024))+'g'
			transfersizes[i] = '1m'


	start1 = time.time()

	os.system("ior -w -t "+transfersizes[0]+" -b" +filesizes[0]+ "-F -m -e -o /lustre/hdd4/testfile0 &") 
	os.system("ior -w -t "+transfersizes[1]+" -b" +filesizes[1]+ "-F -m -e -o /lustre/hdd4/testfile1 &") 
	os.system("ior -w -t "+transfersizes[2]+" -b" +filesizes[2]+ "-F -m -e -o /lustre/hdd4/testfile2 &") 
	os.system("ior -w -t "+transfersizes[3]+" -b" +filesizes[3]+ "-F -m -e -o /lustre/hdd4/testfile3 &") 
	os.system("ior -w -t "+transfersizes[4]+" -b" +filesizes[4]+ "-F -m -e -o /lustre/hdd4/testfile4 &") 
	os.system("ior -w -t "+transfersizes[5]+" -b" +filesizes[5]+ "-F -m -e -o /lustre/hdd4/testfile5 &") 
	os.system("ior -w -t "+transfersizes[6]+" -b" +filesizes[6]+ "-F -m -e -o /lustre/hdd4/testfile6 &") 
	os.system("ior -w -t "+transfersizes[7]+" -b" +filesizes[7]+ "-F -m -e -o /lustre/hdd4/testfile7 &") 
	os.system("ior -w -t "+transfersizes[8]+" -b" +filesizes[8]+ "-F -m -e -o /lustre/hdd4/testfile8 &") 
	os.system("ior -w -t "+transfersizes[9]+" -b" +filesizes[9]+ "-F -m -e -o /lustre/hdd4/testfile9 &") 
	os.system("ior -w -t "+transfersizes[10]+" -b" +filesizes[10]+ "-F -m -e -o /lustre/hdd4/testfile10 &") 
	os.system("ior -w -t "+transfersizes[11]+" -b" +filesizes[11]+ "-F -m -e -o /lustre/hdd4/testfile11 &") 
	os.system("ior -w -t "+transfersizes[12]+" -b" +filesizes[12]+ "-F -m -e -o /lustre/hdd4/testfile12 &") 
	os.system("ior -w -t "+transfersizes[13]+" -b" +filesizes[13]+ "-F -m -e -o /lustre/hdd4/testfile13 &") 
	os.system("ior -w -t "+transfersizes[14]+" -b" +filesizes[14]+ "-F -m -e -o /lustre/hdd4/testfile14 &") 
	os.system("ior -w -t "+transfersizes[15]+" -b" +filesizes[15]+ "-F -m -e -o /lustre/hdd4/testfile15 ") 

	time.sleep(2)
	end1 = time.time()
	elapsedtime1 = end1 - start1 -2

	basic_elapsedtime_array.append("{0:0.4f}".format(elapsedtime1))

	start2 = time.time()

	os.system("ior -w -t "+transfersizes[0]+" -b" +filesizes[0]+ "-F -m -e -o /lustre/hdd1/testfile0,4m,/lustre/hdd3/testfile1,64g &")
	os.system("ior -w -t "+transfersizes[1]+" -b" +filesizes[1]+ "-F -m -e -o /lustre/hdd1/testfile2,4m,/lustre/hdd3/testfile3,64g &")
	os.system("ior -w -t "+transfersizes[2]+" -b" +filesizes[2]+ "-F -m -e -o /lustre/hdd1/testfile4,4m,/lustre/hdd3/testfile5,64g &")
	os.system("ior -w -t "+transfersizes[3]+" -b" +filesizes[3]+ "-F -m -e -o /lustre/hdd1/testfile6,4m,/lustre/hdd3/testfile7,64g &")
	os.system("ior -w -t "+transfersizes[4]+" -b" +filesizes[4]+ "-F -m -e -o /lustre/hdd1/testfile8,4m,/lustre/hdd3/testfile9,64g &")
	os.system("ior -w -t "+transfersizes[5]+" -b" +filesizes[5]+ "-F -m -e -o /lustre/hdd1/testfile10,4m,/lustre/hdd3/testfile11,64g &")
	os.system("ior -w -t "+transfersizes[6]+" -b" +filesizes[6]+ "-F -m -e -o /lustre/hdd1/testfile12,4m,/lustre/hdd3/testfile13,64g &")
	os.system("ior -w -t "+transfersizes[7]+" -b" +filesizes[7]+ "-F -m -e -o /lustre/hdd1/testfile14,4m,/lustre/hdd3/testfile15,64g &")
	os.system("ior -w -t "+transfersizes[8]+" -b" +filesizes[8]+ "-F -m -e -o /lustre/hdd1/testfile16,4m,/lustre/hdd3/testfile17,64g &")
	os.system("ior -w -t "+transfersizes[9]+" -b" +filesizes[9]+ "-F -m -e -o /lustre/hdd1/testfile18,4m,/lustre/hdd3/testfile19,64g &")
	os.system("ior -w -t "+transfersizes[10]+" -b" +filesizes[10]+ "-F -m -e -o /lustre/hdd1/testfile20,4m,/lustre/hdd3/testfile21,64g &")
	os.system("ior -w -t "+transfersizes[11]+" -b" +filesizes[11]+ "-F -m -e -o /lustre/hdd1/testfile22,4m,/lustre/hdd3/testfile23,64g &")
	os.system("ior -w -t "+transfersizes[12]+" -b" +filesizes[12]+ "-F -m -e -o /lustre/hdd1/testfile24,4m,/lustre/hdd3/testfile25,64g &")
	os.system("ior -w -t "+transfersizes[13]+" -b" +filesizes[13]+ "-F -m -e -o /lustre/hdd1/testfile26,4m,/lustre/hdd3/testfile27,64g &")
	os.system("ior -w -t "+transfersizes[14]+" -b" +filesizes[14]+ "-F -m -e -o /lustre/hdd1/testfile28,4m,/lustre/hdd3/testfile29,64g &")
	os.system("ior -w -t "+transfersizes[15]+" -b" +filesizes[15]+ "-F -m -e -o /lustre/hdd1/testfile30,4m,/lustre/hdd3/testfile31,64g")

	time.sleep(2)
	end2 = time.time()
	elapsedtime2 = end2 - start2 -2

	pflhdd_elapsedtime_array.append("{0:0.4f}".format(elapsedtime2))

	start3 = time.time()

	os.system("ior -w -t "+transfersizes[0]+" -b" +filesizes[0]+ "-F -m -e -o /lustre/ssd1/testfile0,4m,/lustre/hdd3/testfile1,64g &")
	os.system("ior -w -t "+transfersizes[1]+" -b" +filesizes[1]+ "-F -m -e -o /lustre/ssd1/testfile2,4m,/lustre/hdd3/testfile3,64g &")
	os.system("ior -w -t "+transfersizes[2]+" -b" +filesizes[2]+ "-F -m -e -o /lustre/ssd1/testfile4,4m,/lustre/hdd3/testfile5,64g &")
	os.system("ior -w -t "+transfersizes[3]+" -b" +filesizes[3]+ "-F -m -e -o /lustre/ssd1/testfile6,4m,/lustre/hdd3/testfile7,64g &")
	os.system("ior -w -t "+transfersizes[4]+" -b" +filesizes[4]+ "-F -m -e -o /lustre/ssd1/testfile8,4m,/lustre/hdd3/testfile9,64g &")
	os.system("ior -w -t "+transfersizes[5]+" -b" +filesizes[5]+ "-F -m -e -o /lustre/ssd1/testfile10,4m,/lustre/hdd3/testfile11,64g &")
	os.system("ior -w -t "+transfersizes[6]+" -b" +filesizes[6]+ "-F -m -e -o /lustre/ssd1/testfile12,4m,/lustre/hdd3/testfile13,64g &")
	os.system("ior -w -t "+transfersizes[7]+" -b" +filesizes[7]+ "-F -m -e -o /lustre/ssd1/testfile14,4m,/lustre/hdd3/testfile15,64g &")
	os.system("ior -w -t "+transfersizes[8]+" -b" +filesizes[8]+ "-F -m -e -o /lustre/ssd1/testfile16,4m,/lustre/hdd3/testfile17,64g &")
	os.system("ior -w -t "+transfersizes[9]+" -b" +filesizes[9]+ "-F -m -e -o /lustre/ssd1/testfile18,4m,/lustre/hdd3/testfile19,64g &")
	os.system("ior -w -t "+transfersizes[10]+" -b" +filesizes[10]+ "-F -m -e -o /lustre/ssd1/testfile20,4m,/lustre/hdd3/testfile21,64g &")
	os.system("ior -w -t "+transfersizes[11]+" -b" +filesizes[11]+ "-F -m -e -o /lustre/ssd1/testfile22,4m,/lustre/hdd3/testfile23,64g &")
	os.system("ior -w -t "+transfersizes[12]+" -b" +filesizes[12]+ "-F -m -e -o /lustre/ssd1/testfile24,4m,/lustre/hdd3/testfile25,64g &")
	os.system("ior -w -t "+transfersizes[13]+" -b" +filesizes[13]+ "-F -m -e -o /lustre/ssd1/testfile26,4m,/lustre/hdd3/testfile27,64g &")
	os.system("ior -w -t "+transfersizes[14]+" -b" +filesizes[14]+ "-F -m -e -o /lustre/ssd1/testfile28,4m,/lustre/hdd3/testfile29,64g &")
	os.system("ior -w -t "+transfersizes[15]+" -b" +filesizes[15]+ "-F -m -e -o /lustre/ssd1/testfile30,4m,/lustre/hdd3/testfile31,64g")

	time.sleep(2)
	end3 = time.time()
	elapsedtime3 = end3 - start3 -2

	pflssd_elapsedtime_array.append("{0:0.4f}".format(elapsedtime3))
	

	filesizes_array.append(filesizes)
	index = index + 1


basic_elapsed_mean = 0
pflhdd_elapsed_mean = 0
pflssd_elapsed_mean = 0

for i in range(0,index):
	basic_elapsed_mean = basic_elapsed_mean + float(basic_elapsedtime_array[i])
	pflhdd_elapsed_mean = pflhdd_elapsed_mean + float(pflhdd_elapsedtime_array[i])
	pflssd_elapsed_mean = pflssd_elapsed_mean + float(pflssd_elapsedtime_array[i])
	print("Test "+str(i)+" filesizes : "+str(filesizes_array[i]))


print("Basic Lustre :" +str(basic_elapsedtime_array))
print("PFL(HDD)     :" +str(pflhdd_elapsedtime_array))
print("PFL(SSD)     :" +str(pflssd_elapsedtime_array))


print(" Basic Lustre   Min time : "+str(min(basic_elapsedtime_array))+ " / Max time : "+str(max(basic_elapsedtime_array))+ " / Mean time : "+str("{0:0.4f}".format(basic_elapsed_mean/5)))	
print(" PFL(HDD)       Min time : "+str(min(pflhdd_elapsedtime_array))+ " / Max time : "+str(max(pflhdd_elapsedtime_array))+ " / Mean time : "+str("{0:0.4f}".format(pflhdd_elapsed_mean/5)))	
print(" PFL(SSD)       Min time : "+str(min(pflssd_elapsedtime_array))+ " / Max time : "+str(max(pflssd_elapsedtime_array))+ " / Mean time : "+str("{0:0.4f}".format(pflssd_elapsed_mean/5)))
