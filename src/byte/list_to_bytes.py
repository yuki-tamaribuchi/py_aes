def list_to_bytes(data):
	data_list = []

	for block in data:
		for token in block:
			for elem in token:
				data_list.append(elem.to_bytes(2, 'big'))
	return b"".join(data_list)