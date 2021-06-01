"""
Plot Graph of all drugs taken with Vitmain D.
Can be generalized to any drug.
"""

import json
import requests
import networkx as nx
import matplotlib.pyplot as plt

def getAdjacencyDict(seriousness=2,countrycode='ca',limit=20):
    query='https://api.fda.gov/drug/event.json?search=serious:"'+str(seriousness)+'"+AND+occurcountry:"'+countrycode+'"&limit='+str(limit)
    response = requests.get(query)
    drugs = json.loads(response.text)

    takentogether=[]
    alltaken=[]
    for result in drugs['results']:
        taken=[]
        for drugstat in result['patient']['drug']:
            prod=drugstat['medicinalproduct']
            print(prod)
            taken.append(prod)
            alltaken.append(prod)
        takentogether.append(taken)


    print(alltaken)
    print(takentogether)
    adjacency={}
    for taken in alltaken:
        takenwith=[]
        for together in takentogether:
            if taken in together:
                for t in together:
                    if t!=taken and t not in takenwith:
                        takenwith.append(t)
        adjacency[taken]=takenwith
    return adjacency

def rootedGraph(d,root):
    V=[]
    E=[]

    droot={}
    droot[root]=d[root]
    for v in d[root]:
        droot[v]=d[v]
    
    for pair in sorted(droot.items(), key=lambda x: x[0]):
        print('drug:{}, takenwith:{}'.format(pair[0],pair[1])) 
    
    for pair in sorted(droot.items(), key=lambda x: x[0]):
        if pair[0] not in V:
            V.append(pair[0])
        for v in pair[1]:
            if v not in V:
                V.append(v)
            e=sorted([pair[0],v])
            if e not in E:
                E.append(e)
    return (V,E)

root='VITAMIN D'
adj=getAdjacencyDict()
d_vitd=rootedGraph(adj,root)

G=nx.Graph()
     
for v in V:
    G.add_node(v)
    
for e in E:
    G.add_edge(e[0],e[1])
    
fig, ax = plt.subplots(figsize=(8,5))    
nx.draw_random(G,with_labels=True, width=0.4,style='dashdot',node_size=1,font_weight='bold',font_size=6,font_color='b')
title="Drugs taken with {}".format(root)
ax.set_title(title, fontweight="bold")
ax.set_xticks([])
ax.set_yticks([])
plt.savefig('VitaminD_clique2.png') 
    
# =============================================================================
# query='https://api.fda.gov/drug/event.json?search=serious:"2"+AND+occurcountry:"ca"&limit=20'
# response = requests.get(query)
# drugs = json.loads(response.text)
# 
# d={}
# takentogether=[]
# alltaken=[]
# for result in drugs['results']:
#     taken=[]
#     for drugstat in result['patient']['drug']:
#         prod=drugstat['medicinalproduct']
#         print(prod)
#         taken.append(prod)
#         alltaken.append(prod)
#     takentogether.append(taken)
# 
# 
# print(alltaken)
# print(takentogether)
# d={}
# for taken in alltaken:
#     takenwith=[]
#     for together in takentogether:
#         if taken in together:
#             for t in together:
#                 if t!=taken and t not in takenwith:
#                     takenwith.append(t)
#     d[taken]=takenwith
# 
# # for k,v in d.items():
# #     print('drug:{}, takenwith:{}'.format(k,v))    
# # 
# # for pair in sorted(d.items(), key=lambda x: x[0]):
# #     print('drug:{}, takenwith:{}'.format(pair[0],pair[1]))   
#      
# V=[]
# E=[]
# 
# d_vitd={}
# d_vitd['VITAMIN D']=d['VITAMIN D']
# for v in d['VITAMIN D']:
#     d_vitd[v]=d[v]
#     
# for pair in sorted(d_vitd.items(), key=lambda x: x[0]):
#     print('drug:{}, takenwith:{}'.format(pair[0],pair[1])) 
#     
# for pair in sorted(d_vitd.items(), key=lambda x: x[0]):
#     if pair[0] not in V:
#         V.append(pair[0])
#     for v in pair[1]:
#        if v not in V:
#            V.append(v)
#        e=sorted([pair[0],v])
#        if e not in E:
#            E.append(e)
# 
# print('vertices:',V)
# print('edges:',E)    
# 
# G=nx.Graph()
#      
# for v in V:
#     G.add_node(v)
#     
# for e in E:
#     G.add_edge(e[0],e[1])
#     
# fig, ax = plt.subplots(figsize=(8,5))    
# nx.draw_random(G,with_labels=True, width=0.4,style='dashdot',node_size=1,font_weight='bold',font_size=6,font_color='b')
# #title="Drugs taken with Vitamin D"
# #ax.set_title(title, fontweight="bold")
# #ax.set_xticks([])
# #ax.set_yticks([])
# #plt.savefig('VitaminD_clique.png') 
# =============================================================================
