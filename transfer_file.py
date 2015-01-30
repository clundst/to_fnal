#!/opt/python3/bin/python3
##NOTE: Uses configparser forcing python3


#import preflight
#import get_list
#import send_files
#import finish_up
import os
import subprocess
import configparser
import lcg_util_wrapper

mode = "testing"
#Subroutines fTor tasking

def log_it():
    print ("Job's Done\n")
    return
  
def landing_check(list):
    print ("Landing Check Invoked\n")
    return  
  
  
def send_files(list,config_file):
	path_head = readcfg(config_file,"path_to_files")
	SURL = readcfg(config_file,"destinationSURL")
	created_files = []
	error_message = ""
	for file in list:
		exit_status = 0
		defineMethod = readcfg(config_file,"method")
		if defineMethod == "cp":
        		print("using cp, sending" , path_head+file, " to ", SURL+file, "\n")
        		exit_status = subprocess.call(["cp", path_head+file, SURL+file])
        		created_files.append(SURL+file)

		if defineMethod == "srmv2":
			full_source_text = "file:/"+path_head+file
			full_dst_text = SURL + file
			print("using srmv2, sending " , full_source_text, " to ", full_dst_text, "\n")
#			lcgCmd = "lcg-cp  -b  -D srmv2 " + full_source_text + " " + full_dst_text 
			(exit_status,error_message) = lcg_util_wrapper.lcg_copy(full_source_text, full_dst_text, 'srmv2', 'none', 'srmv2', nobdii, 1, 0, hcc, 'ignored', 'ignored', NULL , NULL)  		
#			print ("lcg-cmd = ", lcgCmd )
#			os.system(lcgCmd)
			created_files.append(SURL+file)
	if exit_status:
		print("Error in file transfer for file , ", full_source_text )
		exit(1)
	return


  
  
def remove_stale_files(list):
    print ("Remove Stale Files Invoked \n")
    return
  
def preflight(config_file):
    problem = False
    if not (os.path.isfile(config_file)):
      problem = True
      print ("CONFIG FILE MISSING \n")
    print ("Entering pre-flight... \n")	
    if problem :
      print ("Problem found...aborting\n")
      return 1
    return 0
  
  
def readcfg(config_file,target):
    import configparser 
    cfg = configparser.ConfigParser()
    cfg.read(config_file)
    path = cfg[mode][target]
    return path
  
def get_list(path):
    list=[]
    list = os.listdir(path)
    return(list)

def get_which_number(list):
    week=-99
    test=-100
    for item in list:
      list_substring = item.split("_")
      print ("Substring item #3 = ", list_substring[1])
    week = list_substring[1]
    return week

def get_upstream_file(config_file):
	files_on_server = []

	SURL = readcfg(config_file,"destinationSURL")
	lcgCmd = "lcg-ls  -b  -D srmv2 " + SURL
	files_on_server = subprocess.check_output(lcgCmd, shell=True)
	return files_on_server
