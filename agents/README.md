Agents
======

The following scripts and CSVs take Agents (ArchivesSpace-speak) or Names (Archivist's Toolkit-speak) in our EADs and import them to ArchivesSpace. This is a three step process:

  1. get agents (that is, corpname, famname and persname subelements of controlaccess and origination elements)from our EADs; 
  2. use OpenRefine (or, in the case of persname elements, a separate script) to parse them out into the different parts that ArchivesSpace expects (for example, in the case of corpname elements, primary name, subordinate name one and subordinate name two); and
  3. build the JSON that the ArchivesSpace API expects and programmatically add the agents to ArchivesSpace, recording the URI that ArchivesSpace generates so that it can be re-incorporated into the EAD later.
  
There are also a number of micellaneous scripts that were used during cleanup and to generate reports.

Get Agents
----------

### getsubjects.py

Goes through our EADs, generates a list of dictionaries of agent elements, and uses this dictionary to generate the **corpname.csv**, **famname.csv*** and **persname.csv*** to be used in OpenRefine.

### corpname.csv

Output of the **getsubjects.py** script for corpname elements.

### famname.csv

Output of the **getsubjects.py** script for famname elements.

### persname.csv

Output of the **getsubjects.py** script for persname elements.

