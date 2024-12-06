import sys
from hmvlib.models import delete_record, replace_record

def main:
	sysarglist = sys.argv
	sysarglist.pop(0)
	assert len(sysarglist) == 2, "Insufficient number of arguments provided"

	filename_in = sysarglist[0]
	filename_out = sysarglist[1]
	assert filename_in, "Input CSV filename must be provided"
	assert filename_out, "Output CSV filename must be provided"

	if sysarglist[2] == 'D':
		delete_record(filename_in, filename_out)
	else if sysarglist[2] == 'R':
		replace_record(filename_in, filename_out)
