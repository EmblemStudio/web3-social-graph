import json
# import sys

f = open('blocks.json')
blocks = json.load(f)

# match sys.argv[0]:
#   case "example":
#     print("process")

# ETHEREUM FUNCTION SIGNATURES
  # ERC721
    # transferFrom(address,address,uint256):	0x23b872dd
    # safeTransferFrom(address,address,uint256):	0x42842e0e

# for each block
  # for each transaction
    # if the input begins with one of the specified function signatures
      # record an edge using the from and to addresses
      # (future: also include the value to give this edge a weight)

e = ''
n = {'count': 0}

for block in blocks:
  for tx in block['transactions']:
    funcSig = tx['input'][0:10]
    if funcSig == '0x23b872dd' or funcSig == '0x42842e0e':
      e += tx['from'] + '\t' + tx['to'] + "\n"
      if tx['from'] not in n:
        n[tx['from']] = n['count']
        n['count'] += 1
      if tx['to'] not in n:
        n[tx['to']] = n['count']
        n['count'] += 1

f = open('edges', 'w')
f.write(e)
f = open('nodes.json', 'w')
json.dump(n, f)