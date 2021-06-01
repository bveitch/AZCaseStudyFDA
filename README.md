# AZCaseStudyFDA

Respository contains two Python files: DrugCliques2.py and DrugReactionsCountry2.py

In DrugCliques2.py the OpenFDA web API is queried for adverse drug effects with a seriousness 2 in Canada using a limit of 20.
(Each of these parameters is optional and can be changed).

For each of these queries we search for the names of each drug appearing in each patient record. These can be multiple, and drugs appearing for each patient are grouped in a list.
Following this a python dictionary is built, the key for this dictionary is each individual drug name and its values are the names of all other drugs which appear together with the key in the drug list for each patient. From this, I find the names of all drugs, d, which occur with the drug 'VITAMIN D'. This is contiued one stage further to find all drugs used together in a patients treatment with any of the drug d.

The python package networkx to display this information as a graph('VitaminD_clique2.py') The motivation for this was to detect cliques (groups of drugs typically used together) in treatment regimens.

In DrugReactionsCountry2.py the OpenFDA web API is queried for drug reactions and their counts occuring in Great Britain, United States and Canada.
This was used to detect the twelve most common reactions in Great Britain, and this is displayed in a pie chart ('MajorReactionsGB.py').
Following this I print a list of drug adverse reactions common to all three counties. I lso plot the names of adverse reactions known only to one country.
This could aid processing of further adverse reaction reports as it could form a start for mapping reaction names used by doctors between countries.
There are some surprises, however, for example 'stress' and 'asthma' are apparently only common terms in Canada. Suggest this needs further investigation, to ensure there isnt a bug!
