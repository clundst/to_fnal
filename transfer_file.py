#!/usr/bin/python3
##NOTE: Install configparser module on client machine for this to work.
##python-confparser.noarch for fedora


import preflight
import get_list
import send_files
import finish_up
import os
import configparser

config_file = "/home/clundst/to_fnal/to_fnal.config"


preflight.preflight()
print ("Hello World \n")
files = get_list.get_list(config_file)
send_files.send_files(files)
send_files.landing_check(files)
send_files.remove_stale_files(files)
finish_up.log_it()
exit()
