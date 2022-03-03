from aes.sbox import lookup
from aes.sbox import reverse_lookup

def sub_bytes(data):
	converted_data = []

	for block in data:
		converted_block = []
		for token in block:
			converted_block.append([lookup(t) for t in token])
		converted_data.append(converted_block)

	return converted_data

def reverse_sub_bytes(data):
	reversed_data = []

	for block in data:
		reversed_block = []
		for token in block:
			reversed_block.append([reverse_lookup(t) for t in token])
		reversed_data.append(reversed_block)
	return reversed_data