#!/opt/python3/bin//python3
##NOTE: Uses configparser forcing python3

import transfer_file
import os
import subprocess

config_file = "/home/hep/clundst/to_fnal/to_fnal/to_fnal.config"


def get_upstream_file(config_file):
	files_on_server = []
	SURL = readcfg(config_file,"destinationSURL")
	lcgCmd = "lcg-ls  -b  -D srmv2 " + SURL
	files_on_server = os.system(lcgCmd)
	return files_on_server

server_ls = []
server_ls = get_upstream_file(config_file)

print("server_ls = ", server_ls)
exit()

