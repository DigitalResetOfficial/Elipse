# Import Modules
import json
import os
import time
# Create A Workspace
workspace = os.path.dirname(os.path.realpath(__file__))
# Make "Logs" Directory
if not os.path.exists(workspace + "/logs"):
	os.makedirs("logs")
# Create Log
log = open(workspace + "/logs/" + time.strftime("%I:%M:%S") + "-log" +  ".log", "w")
# Create "Workspace" Directory
if not os.path.exists(workspace + "/workspace"):
	os.makedirs("workspace")
	log.write("Created Workspace Directory @ " + time.strftime("%I:%M:%S") + "\n")
# File Name
fName = raw_input("File Name: ")
# Create The Project
project = open("workspace/"+ fName, "w")
log.write("Created Project " + fName + " @ " + time.strftime("%I:%M:%S") + "\n")
# Let User Code File
inp = 1
while inp == 1:
	li = raw_input("")
	if li == "*/EndOfFile/*":
		inp = 0
		log.write("Saved Project " + fName + " @ " + time.strftime("%I:%M:%S") + "\n")
		project.close()
		log.close()
	else:
		project.write(li + "\n")
		log.write("Wrote line " + "\"" + li + "\" " + "on project " + fName + " @ " + time.strftime("%I:%M:%S") + "\n")
