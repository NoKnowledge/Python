#Jimmy Lauchoy
#CS 1122
#HW03

#part 2
#convert decimal to binary
def dec_to_bin(decimal):
	binary = bin(decimal)
	return binary
#convert hex string to word string
def hex_to_char(string_list):
	converted_string = ""
	for i in string_list:
		letter_value = chr(i) 
		converted_string += letter_value
	return converted_string
#convert binary to hex
def bin_to_hex(binary_string):
	new_string = binary_string.split()
	int_list = []
	for i in new_string:
		str_to_int = int(i)
		int_list.append(str_to_int)
	hex_string = ""
	for x in int_list:
		hex_string += hex(x) + ' '
	return hex_string
#convert octal to decimal
def oct_to_dec(octal_num):
	dec_num = 0
	counter = 0
	octal_str = str(octal_num)
	digits = len(octal_str) - 1
	while digits >= 0:
		dec_num += (int(octal_str[counter]) * 8**(digits))
		digits -= 1
		counter += 1
	return dec_num
	
	'''for i in octal_str:
		dec_num += (int(octal_str[i]) * (8**digits-1)) 
		digits -= 1
		print(dec_num)
	return dec_num
	str_num = str(octal_num)
	dec_num = ()
	for i in len(str_num):
		#while n in str_num => 0:
			#dec_num += '''

def main():
	bin_result = dec_to_bin(decimal)
	print(bin_result)
	word_result = hex_to_char(hex_string)
	print(word_result)
	hex_result = bin_to_hex(bin_string)
	print(hex_result)
	dec_result = oct_to_dec(octal)
	print(decimal_result)

