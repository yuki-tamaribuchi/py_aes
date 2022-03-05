multiple_matrix = [
	[2, 3, 1, 1],
	[1, 2, 3, 1],
	[1, 1, 2, 3],
	[3, 1, 1, 2]
]

def mix_columns(data):
	mixed_data = []

	for block in data:
		mixed_block = []
		for i, token in enumerate(block):
			mixed_token = [a*b for a,b in zip(token, multiple_matrix[i])]
			mixed_block.append(mixed_token)
		mixed_data.append(mixed_block)
	return mixed_data


def reverse_mix_columns(data):
	reversed_data = []

	for block in data:
		reversed_block = []
		for i, token in enumerate(block):
			reversed_token = [a//b for a,b in zip(token, multiple_matrix[i])]
			reversed_block.append(reversed_token)
		reversed_data.append(reversed_block)
	return reversed_data
	