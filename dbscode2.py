import sys

def create_header(hd_dict,line):
	# max key length is 7, binary ie base 2
	# create dict with while loop with each header char 
	# as values, binary sequence as keys: 0,00,01...100 etc
	# 1,11,111,1111,etc are not used as keys, they indicate
	# end of segment, hence (2^key_len)-1, eg (2^3)-1 = 7
	BASE = 2
	MAX_KEY_LEN = 7
	key_len = 1
	index = 0
	line = line.rstrip("\n")
	line_len = len(line)
	while ((index < line_len) and (key_len <= MAX_KEY_LEN)):
		for j in range(pow(BASE,key_len)-1):
			#str in binary format eg: 02b is 00, 03b is 000, etc
			binary_str = format(j,('0'+str(key_len)+'b'))
			hd_dict[binary_str] = line[index]
			index += 1
			if index == line_len:
				break
		key_len += 1
	return True

	
def is_header(line):
	# msg only consist of 1s and Os and newlines
	# a line that contains anything else is treated as a header
	# newlines are ignored

	line = line.rstrip("\n")
	if line == "":
		return False
	lineset = set(line)
	binset = {"0","1"}
	if lineset == binset or lineset == {'0'} or lineset == {'1'}:
		return False
	return True


def decode_msg(hd_dict,msg_body,file):
	# read msg_body sequentially with while loop
	# New segments start with xxx binary to indicate key length
	# key length is 000 indicates end of msg, stop decoding
	# move i to after xxx binary, read i:i+key_len as key to header

	KEY_LEN_BIN = 3
	BASE = 2
	if not hd_dict:
		print("no header data")
		return False
	else:		
		msg_body_len = len(msg_body)
		i = 0
		key_len=0
		new_seg = True
		while (i < msg_body_len):
			if new_seg:
				new_seg = False			
				key_len = int(msg_body[i:i+KEY_LEN_BIN],BASE)
				i = i + KEY_LEN_BIN
				if key_len == 0:
					outputfile.write("\n")
					return True
			dict_key = msg_body[i:i+key_len]
			if set(dict_key) != {'1'}:
				if dict_key in hd_dict:
					dict_value = hd_dict[dict_key]
					outputfile.write(dict_value)
					print("{}:{}".format(dict_key,dict_value))
				else:
					print("{} not in header".format(dict_key))
			else:
				new_seg = True
			i = i + key_len
	return True



inputf = "dbsinputfile.txt"
outputf = "dbsoutput.txt"
if len(sys.argv) == 3:
	inputf = sys.argv[1]
	outputf = sys.argv[2]
elif len(sys.argv) == 2:
	inputf = sys.argv[1]
inputfile = open(inputf, "r")
outputfile =open(outputf, "w")
print(inputfile)
line = inputfile.readline()

hd_dict = {}
msg_body = ""
msg_count = 0

while line:
	if (line !="\n"):
		if is_header(line):
			print(msg_body)
			#decode prev msg_body before processing new header
			if decode_msg(hd_dict,msg_body,outputfile):
				msg_count += 1
			print(line, end="")
			hd_dict = {} 
			msg_body = ""
			create_header(hd_dict,line)
		else:
			line = line.rstrip("\n")
			msg_body = msg_body + line
	line = inputfile.readline()
# end of file has been reached, decode last msg_body
print(msg_body)	
if decode_msg(hd_dict,msg_body,outputfile):
	msg_count += 1
print("Number of messages: {}".format(msg_count))
inputfile.close()
outputfile.close()