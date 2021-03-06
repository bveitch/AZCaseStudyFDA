# AZCaseStudyFDA
Respository contains two Python files: DrugCliques2.py and DrugReactionsCountry2.py
***

In DrugCliques2.py the OpenFDA web API is queried for adverse drug effects with a seriousness 2 in Canada limited to 20 patient records.
(Each of these parameters is optional and can be changed).

For each of these queries we search for the names of each drug appearing in each patient record. These can be multiple, and drugs appearing for each patient are grouped in a list.
Following this a python dictionary is built, the key for this dictionary is each *individual drug name* and its values are *the names of all other drugs which appear together with the key in the drug list for each patient*. From this, I find the first degree decendants of 'VITAMIN D', that is the names of all drugs, d, which occur in the drug list along with 'VITAMIN D'. This is contiued one stage further to find the second degree decendants; all drugs used together in a patients treatment with any of the drugs, d.

The python package networkx was used to display this information as a graph ('VitaminD_clique2.png'). The motivation for this was to detect cliques (groups of drugs typically used together) in treatment regimens. The program has been tested for 'CALCIUM' and 'WELLBUTRIN' in addition to 'VITAMIN_D'.

***
In DrugReactionsCountry2.py the OpenFDA web API is queried for drug reactions and their counts occuring in Great Britain, United States and Canada.
At present, the program requires 2 character ISO-3166 ALPHA2 codes rather than the full country name. 
This was used to detect the *twelve most common adverse drug reactions in Great Britain, and this is displayed in a pie chart ('MajorReactionsGB.png')*.
Following this I print, 

    1. a list of drug adverse reactions common to all three counties. 
    2. adverse reactions known only to one country.
    
This could aid processing of further adverse reaction reports as it could form a start for mapping reaction names used by doctors between countries.
However, there are some surprises, for example 'stress' and 'asthma' are apparently only common terms in Canada. Suggest this needs further investigation, to ensure there isnt a bug! Also tested for Great Britain, United States, Canada, Germany and France.
