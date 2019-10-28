import binascii, sys

 
def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(' ', '').replace('0x', '').replace('\t', '').replace('\n', '')
    ascii_str = binascii.unhexlify(hex_str.encode())
    return ascii_str
 
try:
	hex_input = str(sys.argv[1])
except IndexError:
	print "[+] Usage: python %s 0a 0d" % sys.argv[0]
	sys.exit()

ascii_output = hex_to_ascii(hex_input)
print('ASCII result is:{0}'.format(ascii_output))
 

# ascii result is:b'This is an example.'
