def encode(msg):
	# codes = [ord(str(char)) for char in msg] + [256]
	# prob = build_prob(codes)
	# fraction_range = encode_fraction_range(codes, prob)
	# binary_fraction = find_binary_fraction(*fraction_range)
	out = ''
	for c in msg:
		out += bin(ord(c)).replace("0b", "").zfill(16)
	return out
	# return ''.join([f"{bin(ord(i))[2:]:>08}" for i in msg])

# def decode(msg):
# 	return ''.join([chr(i) for i in [int(b, 2) for b in msg.split("b")]])

def decode(msg):
	print(len(msg))
	return ''.join([chr(int(i,2)) for i in (msg[i:i + 16] for i in range(0, len(msg), 16))])

msg = "计算机1"
msg = encode(msg)
msg = decode(msg)
print(msg)