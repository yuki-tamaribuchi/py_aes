def merge_block(data):
	merged_list = []

	for block in data:
		block_length = len(block)
		for i in range(block_length):
			for j in range(block_length):
				merged_list.append(block[j][i])
	return merged_list