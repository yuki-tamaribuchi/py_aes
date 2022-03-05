from string.string_to_ord import string_to_ord

def add_round_key(data, key_instance):
	key = key_instance.get_key()

	added_data_all = []

	for data_ in data:
		added_data = []
		for d, k in zip(data_, key):		
			added = []
			for d_, k_ in zip(d, k):
				added.append(d_^k_)

			added_data.append(list(added))
		added_data_all.append(added_data)

	return added_data_all
		