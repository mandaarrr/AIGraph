import snap

mapping = snap.TStrIntSH()
G0 = snap.LoadEdgeListStr(snap.PNEANet, "dataList.txt", 0, 1, mapping)

snap.SaveEdgeList(G0, "testGraph.txt", "Save as tab-separated list of edges")

snap.PrintInfo(G0)

"""

snap.DelDegKNodes(G0,1,0)
snap.DelDegKNodes(G0,1,0)
snap.DelDegKNodes(G0,1,0)
snap.DelDegKNodes(G0,1,0)

snap.PrintInfo(G0)


DegToCntV = snap.TIntPrV()
snap.GetOutDegCnt(G0, DegToCntV)
for item in DegToCntV:
    print "%d nodes with out-degree %d" % (item.GetVal2(), item.GetVal1())
"""

"""
Components = snap.TCnComV()
snap.GetSccs(G0, Components)
for CnCom in Components:
    print "Size of component: %d" % CnCom.Len()
"""

"""
DegToCntV = snap.TIntPrV()
snap.GetInDegCnt(G0, DegToCntV)
for item in DegToCntV:
    print "%d nodes with in-degree %d" % (item.GetVal2(), item.GetVal1())
"""

"""
for outDeg in range(25,3200):
	for inDeg in range (15,20):
		snap.DelDegKNodes(G0,outDeg,inDeg)
		snap.DelDegKNodes(G0,outDeg,0)

for inDeg in range(15,275):
	for outDeg in range(15,370):
		snap.DelDegKNodes(G0,outDeg,inDeg)
		snap.DelDegKNodes(G0,outDeg,0)

print("After deletion")

DegToCntV = snap.TIntPrV()
snap.GetOutDegCnt(G0, DegToCntV)
for item in DegToCntV:
    print "%d nodes with out-degree %d" % (item.GetVal2(), item.GetVal1())

DegToCntV = snap.TIntPrV()
snap.GetInDegCnt(G0, DegToCntV)
for item in DegToCntV:
    print "%d nodes with in-degree %d" % (item.GetVal2(), item.GetVal1())
 
"""
snap.DelZeroDegNodes(G0)

f = open("dictionary.txt", "w")
for NodeId in range(1,G0.GetMxNId()):
	if G0.IsNode(NodeId):
		line = ("%d: '%s',\n" %(NodeId,mapping.GetKey(NodeId)))
		f.write(line)
		pass
f.close()

snap.SaveEdgeList(G0, "testGraphFinal.txt", "Save as tab-separated list of edges with no Zero InDeg Nodes")

srcNode = "scotland"

NIdV = snap.TIntV()
NIdV.Add(mapping.GetKeyId(srcNode))
print ("Source Node: ",mapping.GetKeyId(srcNode),"is",srcNode)
for dstNode in range (1,G0.GetMxNId()):
	if G0.IsEdge(mapping.GetKeyId(srcNode),dstNode):
		NIdV.Add(dstNode)
		pass

SubGraph = snap.GetSubGraph(G0, NIdV)


for outDeg in range(00,10):
	for inDeg in range (00,10):
		snap.DelDegKNodes(SubGraph,outDeg,inDeg)


for dstNode in range (1,SubGraph.GetMxNId()):
	if SubGraph.IsEdge(mapping.GetKeyId(srcNode),dstNode):
		print(dstNode,mapping.GetKey(dstNode))


Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(SubGraph, Nodes, Edges, 1.0)
for node in Nodes:
    print "node: %d centrality: %f" % (node, Nodes[node])

print snap.IsConnected(SubGraph)

snap.SaveEdgeList(SubGraph, "RelGraph.txt", "Save as tab-separated list of edges with no Zero InDeg Nodes")

print("Number of edges is %d" % (snap.CntUniqDirEdges(SubGraph)))

snap.PrintInfo(SubGraph)