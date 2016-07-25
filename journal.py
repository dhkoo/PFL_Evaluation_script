import time
import sys
import os
import random
import subprocess

def stddev(lst):
	temp = []
	mean = sum(lst) / float(len(lst))
	for i in range(len(lst)):
		tmep.append(float(abs(lst[i] - mean))**2)

	return (sum(temp) / (len(lst)-1) **0.5)

def ps_check():
	while True:
		check = subprocess.check_output('ps', shell=True)
		if str(check).find('ior') == -1:
			#print("small file I/O finished")
			break
		time.sleep(1.5)


def ior(mode, threads, iterative, tsize, bsize):

	index1 = 0
	index2 = 1

	if mode == 0:
		for i in range(threads):
			if i != threads-1:
				os.system("ior -i "+str(iterative)+" -w -t "+tsize+" -b "+bsize+" -F -m -e -o /lustre/hdd4/testfile"+str(i)+" > /dev/null &")
			else:
				os.system("ior -i "+str(iterative)+" -w -t "+tsize+" -b "+bsize+" -F -m -e -o /lustre/hdd4/testfile"+str(i)+" > /dev/null")
	elif mode == 1:
		for i in range(threads):
			if i != threads-1:
				os.system("ior -i "+str(iterative)+" -w -t "+tsize+" -b "+bsize+" -F -m -e -o /lustre/hdd1/testfile"+str(index1)+",4m,/lustre/hdd3/testfile"+str(index2)+",16g > /dev/null &")
	
			else:
				os.system("ior -i "+str(iterative)+" -w -t "+tsize+" -b "+bsize+" -F -m -e -o /lustre/hdd1/testfile"+str(index1)+",4m,/lustre/hdd3/testfile"+str(index2)+",16g > /dev/null")

			index1 = index1 + 2
			index2 = index2 + 2

	elif mode == 2:
		for i in range(threads):
			if i != threads-1:
				os.system("ior -i "+str(iterative)+" -w -t "+tsize+" -b "+bsize+" -F -m -e -o /lustre/ssd1/testfile"+str(index1)+",4m,/lustre/hdd3/testfile"+str(index2)+",16g > /dev/null &")

			else:
				os.system("ior -i "+str(iterative)+" -w -t "+tsize+" -b "+bsize+" -F -m -e -o /lustre/ssd1/testfile"+str(index1)+",4m,/lustre/hdd3/testfile"+str(index2)+",16g > /dev/null")

			index1 = index1 + 2
			index2 = index2 + 2

	elif mode == 3:
		for i in range(threads):
			if i != threads-1:
				os.system("ior -i "+str(iterative)+" -w -t "+tsize+" -b "+bsize+" -F -m -e -o /lustre/ssd1/testfile"+str(index1)+",4m,/lustre/hdd4/testfile"+str(index2)+",16g > /dev/null &")

			else:
				os.system("ior -i "+str(iterative)+" -w -t "+tsize+" -b "+bsize+" -F -m -e -o /lustre/ssd1/testfile"+str(index1)+",4m,/lustre/hdd4/testfile"+str(index2)+",16g > /dev/null")

			index1 = index1 + 2
			index2 = index2 + 2
	else:
		print("Select mode : 0~3 ( basic Lustre : 0 / PFL(HDD) : 1 / PFL(SSD) : 2 / PFL(SSD)+HDD1 : 3 )")



def jtest1():

	sfsize = ["4m","8m"]
	#sfsize = ["4m"]
	mode = ["basiclustre","pflhdd","pflssd"]

	for ss in sfsize:
		print("*"*15+ss+"*"*15)
		for i in range(3): # mode
			print("="*15+mode[i]+"="*15)
			for j in range(7): # iteration // j=7 : 1600iter
				if os.fork() == 0:
					if os.fork() == 0:
						iteration = 25*pow(2,j) # 25,50,100,.. 1600 iteration
						print("="+str(iteration)+" iteration=")
						start = time.time()
						ior(i,8,iteration,"1m",ss) 
						#ps_check()
						end = time.time()
						print("small file : "+str("{0:0.2f}".format(end-start))+"s")
						sys.exit()
					else:
						start = time.time()

						if i == 0:
							os.system("ior -w -t 1m -b 16g -F -m -e -o /lustre/hdd4/test > /dev/null")
						elif i == 1:
							os.system("ior -w -t 1m -b 16g -F -m -e -o /lustre/hdd1/test0,4m,/lustre/hdd3/test1,16g > /dev/null")
						else:
							os.system("ior -w -t 1m -b 16g -F -m -e -o /lustre/ssd1/test0,4m,/lustre/hdd3/test1,16g > /dev/null")
							
						end = time.time()
						print("large file : "+str("{0:0.2f}".format(end-start)))
						os.wait()
						sys.exit()
				else:
					os.wait()
					print("-"*30)
					time.sleep(2)

def jtest2():
	mode = ["basiclustre","pflhdd","pflssd","pflssdhdd"]
	sfsize = ["4m","8m"]
	#sfsize = ["8m"]
	#threadpersize = ["2g","3g"]
	threadpersize = ["3g"]
	iteration = ""

	for tps in range(1):
		print("#"*15+threadpersize[tps]+"#"*15)
		for ss in sfsize:
			print("*"*15+ss+"*"*15)
			for i in range(4): # mode
				print("="*15+mode[i]+"="*15)
				for j in range(4): # 2^0~2^3 #of threads
					if os.fork() == 0:
						if os.fork() == 0:
							if ss == "4m":
								iteration = int(512*pow(1.5,tps)) # 512:2g // 768:3g		
							elif ss == "8m":
								iteration = int(256*pow(1.5,tps)) 
							start = time.time()
							ior(i,8,iteration,"1m",ss) 
							end = time.time()
							print("small file : "+str("{0:0.2f}".format(end-start)))
							sys.exit()
						
						else:
							index1 = 0
							index2 = 1
							start = time.time()
							if i == 0:
								for lc in range(pow(2,j)):
									if lc != pow(2,j)-1:
										os.system("ior -w -t 1m -b 16g -F -m -e -o /lustre/hdd4/test"+str(lc)+" > /dev/null &")
										#print(j)
									else:
										os.system("ior -w -t 1m -b 16g -F -m -e -o /lustre/hdd4/test"+str(lc)+" > /dev/null")
										#print(j)
							elif i == 1:
								for lc in range(pow(2,j)):
									if lc != pow(2,j)-1:
										os.system("ior -w -t 1m -b 16g -F -m -e -o /lustre/hdd1/test"+str(index1)+",4m,/lustre/hdd3/test"+str(index2)+",16g > /dev/null &")
										#print(j)
									else:
										os.system("ior -w -t 1m -b 16g -F -m -e -o /lustre/hdd1/test"+str(index1)+",4m,/lustre/hdd3/test"+str(index2)+",16g > /dev/null")
										#print(j)
									index1 = index1 + 2
									index2 = index2 + 2			

							elif i == 2:
								for lc in range(pow(2,j)):
									if lc != pow(2,j)-1:
										os.system("ior -w -t 1m -b 16g -F -m -e -o /lustre/ssd1/test"+str(index1)+",4m,/lustre/hdd3/test"+str(index2)+",16g > /dev/null &")
										#print(j)
									else:
										os.system("ior -w -t 1m -b 16g -F -m -e -o /lustre/ssd1/test"+str(index1)+",4m,/lustre/hdd3/test"+str(index2)+",16g > /dev/null")
										#print(j)
									index1 = index1 + 2
									index2 = index2 + 2			

							else:
								for lc in range(pow(2,j)):
									if lc != pow(2,j)-1:
										os.system("ior -w -t 1m -b 16g -F -m -e -o /lustre/ssd1/test"+str(index1)+",4m,/lustre/hdd4/test"+str(index2)+",16g > /dev/null &")
										#print(j)
									else:
										os.system("ior -w -t 1m -b 16g -F -m -e -o /lustre/ssd1/test"+str(index1)+",4m,/lustre/hdd4/test"+str(index2)+",16g > /dev/null")
										#print(j)
									index1 = index1 + 2
									index2 = index2 + 2			
							end = time.time()
							print("large file : "+str("{0:0.2f}".format(end-start)))
							os.wait()
							sys.exit()
		
					else:
						os.wait()
						print("-"*30)
						time.sleep(2)
def main():
	#jtest1()
	jtest2()

if __name__ == '__main__':
	main()
