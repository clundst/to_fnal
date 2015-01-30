#!/usr/bin/python
import lcg_util

def lcg_copy(full_source_text, full_dst_text, type1, type2, type3, bdii_flag, one, zero, VO, ignored1, ignored2, ignored3 , ignored4):
	exitcode = 0
	error_message=""
	(exitcode,error_message) = lcg_util.lcg_cp3(full_source_text, full_dst_text, type1, type2, type3, bdii_flag, 1, 0, VO, 'ignored', 'ignored', NULL , NULL)

	return(exitcode,error_message)
