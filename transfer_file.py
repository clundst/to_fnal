#!/usr/bin/python3
##NOTE: Uses configparser forcing python3


#import preflight
#import get_list
#import send_files
#import finish_up
import os
import configparser


config_file = "/home/clundst/to_fnal/to_fnal.config"

def log_it():
    print ("Job's Done\n")
    return
def send_files(list):
    print (list, "\n")
    for file in list:
      print ("file =", file)
    return

def landing_check(list):
    print (list, "\n")
    return
def remove_stale_files(list):
    print (list,"\n")
    return
  
def preflight():
    problem = False
    print ("Entering pre-flight... \n")	
    if problem :
      print ("Problem found...aborting\n")
      return 1
    return 0
def readpath(config_file):
    import configparser 
    cfg = configparser.ConfigParser()
    cfg.read(config_file)
    path = cfg['FROM_T3']['path_to_files']
    return path
  
def get_list(path):
    
    print ("Path from config is = ", path, "\n")
    list=[]
    list = os.listdir(path)
#      print ("path to walk = ", path)
#      for name in files :
#       print ("Name in files = ", name)
#       list.append(name)
    return(list)

preflight()


path = readpath( config_file )
files = get_list(path)

send_files(files)
landing_check(files)
remove_stale_files(files)
log_it()
exit()


