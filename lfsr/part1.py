# these are just large numbers to initialize 32bits
bitstring_one = (1 << 31) | 888475480
bitstring_two = (1 << 31) | 1109000000
# print("{:32b}".format(bitstring_one))
# print("{:32b}\n".format(bitstring_two))
output = []
for i in range(64):
  output.append((bitstring_one ^ bitstring_two) & 1)
  # print(f"{(bitstring_two >> 1) & 1} XOR {(bitstring_two >> 10) & 1}")
  bitstring_one_newbit = (bitstring_one ^ (bitstring_one >> 1) ^ (bitstring_one >> 10)) & 1
  # print(f"{(bitstring_two >> 7) & 1} XOR {(bitstring_two >> 13) & 1} XOR {(bitstring_two >> 30) & 1}")
  bitstring_two_newbit = (bitstring_two ^ (bitstring_two >> 7) ^ (bitstring_two >> 13) ^ (bitstring_two >> 30)) & 1

  # assign new bit to position 31
  bitstring_one = (bitstring_one >> 1) | (bitstring_one_newbit << 31)
  bitstring_two = (bitstring_two >> 1) | (bitstring_two_newbit << 31)

# print("\n{:32b} ".format(bitstring_one))
# print("{:32b} ".format(bitstring_two))
print()
for bit in output[0:20]:
  print(bit, end='')
print("\n")