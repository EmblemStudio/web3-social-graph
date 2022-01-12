import json
from operator import itemgetter
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
  ranks += str(sn) + '\t' + str(node_scores[sn][1]) + '\n'
r.write(ranks)