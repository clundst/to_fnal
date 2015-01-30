#!/opt/python3/bin//python3
##NOTE: Uses configparser forcing python3

import os
import subprocess
import transfer_file.py



config_file = "/home/hep/clundst/to_fnal/to_fnal/to_fnal.config"

if preflight(config_file):
  print ("Problems found in preflight tests.")
  exit(1)

files = get_list(readcfg(config_file,"path_to_files"))
week = get_which_number(files)
send_files(files, config_file)
remove_stale_files(files)
log_it()
exit()

