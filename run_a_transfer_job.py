#!/usr/bin/python
##NOTE: Uses configparser forcing python3

import os
import subprocess
import transfer_file



config_file = "/home/hep/clundst/to_fnal/to_fnal/to_fnal.config"

if transfer_file.preflight(config_file):
  print ("Problems found in preflight tests.")
  exit(1)

files = transfer_file.get_list(transfer_file.readcfg(config_file,"path_to_files"))
week = transfer_file.get_which_number(files)
transfer_file.send_files(files, config_file)
transfer_file.remove_stale_files(files)
transfer_file.log_it()
exit()

