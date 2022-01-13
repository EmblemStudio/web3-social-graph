import requests
import json
import env
from graphs import getGraph
from Web3PageRank import PageRank

n = open('nodes.json')
nodes = json.load(n)
gg = getGraph('edges')
edges = gg.get_connections()

pr = PageRank(beta=0.85, edges=edges, node_ids=nodes, epsilon=1e-6, max_iterations=20, node_num=nodes['count'])
PageRank_vector = pr.pageRank()
node_scores = {}

for node in nodes:
  if 'count' != node:
    node_scores[node] = (
      nodes[node],
      PageRank_vector[nodes[node]]
    )

sorted_nodes = sorted(node_scores, key=lambda n: node_scores[n][1], reverse=True)

r = open('ranks', 'w')
ranks = ''
for sn in sorted_nodes:
  url = (
    "https://api.etherscan.io/api?module=contract&action=getsourcecode&address=" + 
    str(sn) + 
    "&apikey=" + 
    env.ETHERSCAN
  )
  res = requests.get(url)
  name = ''
  if res.status_code == 200:
    res = res.json()
  if res['status'] == '1':
    name = res['result'][0]['ContractName']
  if name == '':
    name = 'Unverified or EOA'
  print(str(sn) + '\t' + str(node_scores[sn][1]) + '\t' + name)
  ranks += str(sn) + '\t' + str(node_scores[sn][1]) + '\t' + name + '\n'
r.write(ranks)