#Homework 3 - exercise4
#Author: Davide Violante

from larcc import *

def diagram2cellEfficient(diagram, master, cell):
	# like the old version
	matrix = diagram2cellMatrix(diagram)(master,cell)
	diagram = larApply(matrix)(diagram)

	# unpacking 
	V1, CV1 = master

	# removing the specified cell
	CV1 = [c for k,c in enumerate(CV1) if k != cell]

	# luckly there is vertexSieve function
	V, CV1, CV2, NN = vertexSieve((V1,CV1),diagram)

	# sum CVs
	CV = (CV1 + CV2)

	# re-packing
	master = V, CV

	return master

	# old version
'''
	V = master[0] + diagram[0]
	offset = len(master[0])
	CV = [c for k,c in enumerate(master[1]) if k != cell] + [
	[v+offset for v in c] for c in diagram[1]]
	master = V, CV
	return master
'''
