from aes.split_to_block import split_to_block
from string.string_to_ord import string_to_ord
from aes.sub_bytes import sub_bytes
from aes.shift_rows import shift_rows
from aes.mix_columns import mix_columns
from aes.add_round_key import add_round_key
from byte.list_to_bytes import list_to_bytes

def encrypt(data, key_instance):
	data = string_to_ord(data)
	data = split_to_block(data)
	data = sub_bytes(data)
	data = shift_rows(data)
	data = mix_columns(data)
	data = add_round_key(data, key_instance)
	data = list_to_bytes(data)
	return data

	
	