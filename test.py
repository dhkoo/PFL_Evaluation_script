import os
import sys
import time


for i in range(50):
	if os.fork() == 0:
			if os.fork() == 0:
				if os.fork() == 0:
					os.system("python dn2.py basiclustre")
					sys.exit()
				else:
					os.system("ssh dn3 'python dn3.py basiclustre'")
					os.wait()
					sys.exit()
			else:
				os.system("ssh dn4 'python dn4.py basiclustre'")
				os.wait()
				sys.exit()
	else:
		os.wait()

	
for i in range(50):
	if os.fork() == 0:
			if os.fork() == 0:
				if os.fork() == 0:
					os.system("python dn2.py pflhdd")
					sys.exit()
				else:
					os.system("ssh dn3 'python dn3.py pflhdd'")
					os.wait()
					sys.exit()
			else:
				os.system("ssh dn4 'python dn4.py pflhdd'")
				os.wait()
				sys.exit()
	else:
		os.wait()
			

for i in range(50):
	if os.fork() == 0:
			if os.fork() == 0:
				if os.fork() == 0:
					os.system("python dn2.py pflssd")
					sys.exit()
				else:
					os.system("ssh dn3 'python dn3.py pflssd'")
					os.wait()
					sys.exit()
			else:
				os.system("ssh dn4 'python dn4.py pflssd'")
				os.wait()
				sys.exit()
	else:
		os.wait()
