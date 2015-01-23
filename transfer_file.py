#!/usr/bin/python3
##NOTE: Uses configparser forcing python3


#import preflight
#import get_list
#import send_files
#import finish_up
import os
import subprocess
import configparser


config_file = "/home/clundst/to_fnal/to_fnal.config"

#Subroutines for tasking

def log_it():
    print ("Job's Done\n")
    return
  
def landing_check(list):
    print ("Landing Check Invoked\n")
    return  
  
  
def send_files(list,config_file):
    path_head = readcfg(config_file,"path_to_files")
    SURL = readcfg(config_file,"destinationSURL")
    for file in list:
      defineMethod = readcfg(config_file,"method")
      if defineMethod == "mv":
        print("using mv, sending" , path_head+file, " to ", SURL+file, "\n")
        mv_exit = subprocess.call(["mv", path_head+file, SURL+file])
        if mv_exit:
          print ("mv non-zero exit code")  
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
    path = cfg['FROM_T3'][target]
    return path
  
def get_list(path):
    list=[]
    list = os.listdir(path)
    return(list)


#Workflow starts here.  

if preflight(config_file):
  print ("Problems found in preflight tests.")
  exit(1)

files = get_list(readcfg(config_file,"path_to_files"))
send_files(files, config_file)
remove_stale_files(files)
log_it()
exit()


