# import networkx as nx
# import matplotlib.pyplot as plt

# G = nx.cycle_graph(12)
# pos = nx.spring_layout(G)

# cf = plt.figure(1, figsize=(8,8))
# ax = cf.add_axes((0,0,1,1))

# for n in G:
#     G.node[n]['draw'] = nx.drawing.draw_networkx_nodes(G,pos,nodelist=[n], label=None,node_size=200,alpha=0.5,node_color='r')
# for u,v in G.edges():
#     G[u][v]['draw']=nx.drawing.draw_networkx_edges(G,pos,edgelist=[(u,v)],alpha=0.5,arrows=False,width=5)

# plt.ion()
# plt.draw()

# sp = nx.shortest_path(G,0,6)
# edges = zip(sp[:-1],sp[1:])

# for u,v in edges:
#     plt.pause(1)
#     G.node[u]['draw'].set_color('r')
#     G.node[v]['draw'].set_color('r')
#     G[u][v]['draw'].set_alpha(1.0)
#     G[u][v]['draw'].set_color('r')
#     plt.draw()