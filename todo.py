import argparse

arg = argparse.ArgumentParser()

arg.add_argument("-a", action="store", dest="entry", help="add entry")
arg.add_argument("-d", action="store", dest="delid", help="del entry with id")

args = arg.parse_args()
filepath = "/home/jvol/.conky/todo/To-do.txt"



def adde(entry,filepath):
	wentry = str(entry)
	with open(filepath, "a") as file:
		file.write(wentry + "\n")

def dele(id,filepath):
	id = int(id)
	with open(filepath, "r") as file:
		lines = file.readlines()
	
	lines.pop(id)
	
	with open(filepath, "w") as file:
		file.writelines(lines)

if args.entry != None:
	adde(args.entry,filepath)
if args.delid != None:
	dele(args.delid,filepath)