import binascii, sys
# one at a time
def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(" ", "").replace("0x", "").replace("\t", "").replace("\n", "")
    ascii_str = binascii.unhexlify(hex_str.encode())
    return ascii_str
 
try:
	hex_in = str(sys.argv[1])
except IndexError:
	print "[+] Usage: python %s 0a" % sys.argv[0]
	sys.exit()

ascii_out = hex_to_ascii(hex_in)
print("ASCII result: {0}".format(ascii_out))
# TODO:  
#	1) Can binascii provide a desc and not just the symbol
# 	2) Add try except to ascii_out
#	3) Can I add functionality to convert 4 bytes at a time
