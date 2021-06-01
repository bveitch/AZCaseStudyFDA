#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 19:11:59 2021

@author: myconda
"""

import json
import requests
from matplotlib import pyplot as plt
import numpy as np

def reactionsInCountry(countrycode):
    query='https://api.fda.gov/drug/event.json?search=occurcountry:"'+countrycode+'"&count=patient.reaction.reactionmeddrapt.exact'
    response = requests.get(query)
    drugs = json.loads(response.text)
    d={}
    for result in drugs['results']:
        d[result['term']]=result['count']
    return d

def displayMajorReactionsInCountry(countrycode,fname=None, nmajor=12):
    d=reactionsInCountry(countrycode)
    dsort=sorted(d.items(), key=lambda x: x[1], reverse=True)
    reactions=[]
    counts=[]
    for v in dsort[:nmajor]:
        reactions.append(v[0].lower())
        counts.append(v[1])
    count_other=0
    for v in dsort[nmajor:]:
        count_other+=v[1]
    reactions.append('OTHER'.lower())
    counts.append(count_other)
 
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    title="Major Reactions in {}".format(countrycode) 
    ax.axis('equal')
    ax.pie(counts, labels = reactions,autopct='%1.1f%%',textprops={'fontsize': 7})
    plt.title(title, fontweight="bold")
    plt.show()
    if fname is not None:
        plt.savefig(fname) 

def reactionsByCountry(countrylist):
    d={}
    for country in countrylist:
        dic=reactionsInCountry(country)
#        print(list(dic.keys()))
        d[country]=list(dic.keys())
    reactions_country={}
    for country,reactions in d.items():
        for reaction in reactions:
            if reaction in reactions_country.keys():
                reactions_country[reaction].append(country)
            else:
                reactions_country[reaction]=[country]
    return reactions_country

wantPieChartGB=False
if wantPieChartGB:
    displayMajorReactionsInCountry('gb','MajorReactionsGB.png')
    
countrylist=['gb','us','ca']
reactsCountries=reactionsByCountry(countrylist)
print(reactsCountries)
reactionsCommonAll=[]
reactionsOne={}
for reaction, countries in reactsCountries.items():
    if len(countries)==len(countrylist):
        reactionsCommonAll.append(reaction)
    if len(countries)==1:
        reactionsOne[reaction]=countries[0]
        
print("These drug reactions were known to all countries ...")
for reaction in reactionsCommonAll:
    print("   {}".format(reaction.lower()))
print("Drug Reactions specific to only one country...")
for reaction,country in reactionsOne.items():
    print("   {} specific to {}".format(reaction,country.upper()))
