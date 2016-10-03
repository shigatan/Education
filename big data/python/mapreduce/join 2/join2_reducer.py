#!/usr/bin/env python
import sys

abc_channel = 'ABC'
prev_tv_show = ''
isAbc = False
abc_tv_shows = []
tv_shows = {}

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list

    curr_tv_show  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item
	
    if curr_tv_show != prev_tv_show:
	isAbc = False 
	prev_tv_show = curr_tv_show
	tv_shows[curr_tv_show] = 0

    if (isAbc == False and value_in == abc_channel):
	isAbc = True
	abc_tv_shows.append(curr_tv_show)

    if value_in.isdigit():
	if tv_shows.has_key(curr_tv_show):
	    tv_shows[curr_tv_show] += int(value_in)

for key in abc_tv_shows:
    print('{0} {1}'.format(key, tv_shows[key]))
	
