#Homework 3 - exercise3
#Author: Davide Violante

from larcc import *

#mne = merging numbering elimination function
def mne(diagram, master, toRemove, toMerge):
	# unpacking
	V, CV = diagram
	
	# removing the specified cells using toRemove list
	diagram = V, [cell for k,cell in enumerate(CV) if not (k in toRemove)]
	
	# sorting the list to prevent problems with numbering of new cells
	toMerge = list(sort(toMerge))

	# for limit
	numtot = range(len(toMerge))

	# adding the specified new cells using toMerge list
	for k in numtot:
		newCell = toMerge[k] - k
		# using the already existing function
		master = diagram2cell(diagram, master, newCell)
	return master