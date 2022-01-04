import requests
import sys
import env
import json

# run this script with the number of blocks you want: `python3 get_blocks.py 5`
n = 100
if len(sys.argv) > 1:
  n = int(sys.argv[1])

blocks = []
block_number = requests.post(
  env.ALCHEMY,
  json={
    "jsonrpc": "2.0",
    "method": "eth_blockNumber",
    "params": [],
    "id": 0
  }
).json()['result']
# minus one so we get the # of the blocks from sys.argv
block_number = hex(int(block_number, 16) - 1)

while n >= 0:
  res = requests.post(
    env.ALCHEMY,
    json={
      "jsonrpc": "2.0",
      "method": "eth_getBlockByNumber",
      "params": [block_number, True],
      "id": 0
    }
  ).json()
  blocks.append(res)
  n -= 1
  block_number = hex(int(block_number, 16) - 1)

f = open("blocks.json", "w")
json.dump(blocks, f)
print("Finished")