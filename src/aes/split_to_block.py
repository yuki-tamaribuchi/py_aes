def split_to_block(string):
	assert(len(string)%16 == 0)

	blocks = []

	for i in range(len(string)//16):
		token = string[i*16:i*16+16]

		rows = [[], [], [], []]

		for j in range(4):
			for k in range(4):
				rows[j].append(token[j + k*4])
		blocks.append(rows)

	return blocks