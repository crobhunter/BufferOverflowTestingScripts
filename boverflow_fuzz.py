#!/usr/bin/python

import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IpAddress=""
port=
buffer="A"
counter=100

while len(buffer) <=20
	buffer.append("A" * counter)
	counter=counter + 200

for string in buffer:
	print "Fuzz with %s bytes" $ len(string)
	connect=s.connect(({IpAddress}, {port}))
	s.recv(1024)
	s.send("") #send parameter -example: "ParameterName value\r\n"
	s.recv(1024)
	s.send("PASS" + string + "\r\n") #this request sends the increasing string value
	s.send("QUIT\r\n")
	s.close() #always close the connection
