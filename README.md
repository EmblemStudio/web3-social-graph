# POC Web3 Social Graph

1. Grab Ethereum block data
2. Grab specific subsets of that data
  - All transactions with a given address as from or two
  - All transactions that include a given address as from, two, or in `input`
  - All transactions that include an ERC721 transfer call signature in `input`
3. Sort the subsets using social graph algorithms like PageRank

Set up your local `env.py` according to `env.example.py`.

Run `python3 get_blocks.py NUMBER_OF_BLOCKS`, `python3 get_graph.py`, `python3 get_ranks.py`. 

Output will be in `ranks`.