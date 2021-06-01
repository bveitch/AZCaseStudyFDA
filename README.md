# AZCaseStudyFDA

Respository contains two Python files: DrugCliques2.py and DrugReactionsCountry2.py

In DrugCliques2.py the OpenFDA web API is queried for adverse drug effects with a seriousness 2 in Canada using a limit of 20.
(Each of these parameters is optional and can be changed)
For each of these queries we search for the drug names appearing in each patient record. 
Drugs appearing for each patient are grouped in a list.
Following this we search for each individual drug name and find all other drugs which appear together with that list for each patient.
That is a dictionary of drugs which appear together with any other drug.
Finally the dictionary is interrogated to find all drugs, d, which occur with 'VITAMIN D'. Furthermore we continue this process one stage further so that for every drug 
occuring with any drug d.
I use the python package networkx to display this information as a graph('VitaminD_clique2.py') The motivation for this was to detect cliques (groups of drugs used together) in treatment regimens.

In DrugReactionsCountry2.py the OpenFDA web API is queried for drug reactions and their counts occuring in Great Britain, United States and Canada.
This was used to detect the twelve most common reactions in Great Britain, and this is displayed in a pie chart ('MajorReactionsGB.py').
Following this I print a list of drug adverse reactions common to all three counties. I lso plot the names of adverse reactions known only to one country.
This could aid processing of further adverse reaction reports as it could form a start for mapping reaction names used by doctors between countries.
There are some surprises, however, for example 'stress' and 'asthma' are apparently only common terms in Canada. Suggest this needs further investigation, to ensure there isnt a bug!
