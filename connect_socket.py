#!/usr/bin/python

import socket, time, struct, sys

for string in payload:
	try:
		IpAddress = str(sys.argv[1])
		port = int(sys.argv[2])
	except IndexError:
		print "[+] Usage example: python %s Host_IP_Address Port" % sys.argv[0]
		sys.exit()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    print "\nSending..."
    s.connect((IpAddress,port))
    print repr (s.recv(1024))
    
    # s.send('USER test' +'\r\n') # send username "test"
    # print repr (s.recv(1024))

    # s.send('PASS test\r\n') # send password "test"
    # print repr (s.recv(1024))
    s.close() # close socket
    print "\nDone!"
except:
    print "Could not connect!”

