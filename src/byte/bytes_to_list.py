def bytes_to_list(data):

	data_byte_list = list(data)

	data_list = []
	for i in range(0, len(data_byte_list), 2):
		data_list.append(data_byte_list[i]<<8 | data_byte_list[i+1])
	
	new_data_list = []
	for i in range(0, len(data_list), len(data_list)//2):
		block = data_list[i:i+16]
		new_block = [block[j:j+4] for j in range(0, len(block), 4)]
		new_data_list.append(new_block)
	return new_data_list