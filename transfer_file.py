#!/usr/bin/python
import preflight
import get_list
import send_files
import finish_up


preflight.preflight()
print "Hello World \n"
files = get_list.get_list()
send_files.send_files(files)
send_files.landing_check(files)
send_files.remove_stale_files(files)
finish_up.log_it()
exit()
