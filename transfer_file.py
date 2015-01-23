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

def get_list(config_path):
    import configparser
    cfg = configparser.ConfigParser()
    list = []
    cfg.read(config_path)
    path = cfg['FROM_T3']['path_to_files']
    
    print ("Path from config is = ", path, "\n")
    list = [1,23, 34 ]
    return(list)

preflight()
print ("Hello World \n")
files = get_list(config_file)
send_files(files)
landing_check(files)
remove_stale_files(files)
log_it()
exit()


