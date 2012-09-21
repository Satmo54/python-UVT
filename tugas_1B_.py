#!/usr/bin/env python2

start="04:20:10"
end="10:30:20"

def selisih(mulai, akhir):
	import datetime as dt
	start_dt = dt.datetime.strptime(mulai, '%H:%M:%S')
	end_dt = dt.datetime.strptime(akhir, '%H:%M:%S')
	diff = (end_dt - start_dt) 
	print diff
	
selisih(start, end)
