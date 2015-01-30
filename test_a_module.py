#!/opt/python3/bin//python3
##NOTE: Uses configparser forcing python3

import os
import subprocess
import transfer_file



config_file = "/home/hep/clundst/to_fnal/to_fnal/to_fnal.config"
files_on_server = transfer_file.get_upstream_file(config_file)
print ("Files on Server : ", files_on_server)
