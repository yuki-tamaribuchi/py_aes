def shift_rows(data):
	shifted_data = []
	for block in data:
		shifted_block = []
		for i, token in enumerate(block):
			shifted_token = token[i:] + token[:i]
			shifted_block.append(shifted_token)
		shifted_data.append(shifted_block)

	return shifted_data


def reverse_shift_rows(data):
	reversed_data = []
	for block in data:
		reversed_block = []
		for i, token in enumerate(block):
			reversed_token = token[-i:] + token[:-i]
			reversed_block.append(reversed_token)
		reversed_data.append(reversed_block)
	return reversed_data