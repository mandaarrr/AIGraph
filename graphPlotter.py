import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl

g = nx.read_edgelist('RelGraph.txt',create_using=nx.MultiDiGraph(), nodetype=int)
h = nx.MultiDiGraph()

h.add_edges_from(g.edges())

print(nx.info(h))

sp = nx.shell_layout(h)

plt.axis('off')

nx.draw_networkx(h,pos=sp,with_labels=True,font_size=6,node_size=300)

plt.show()
plt.savefig("SamsungNetwork.png", format="PNG")