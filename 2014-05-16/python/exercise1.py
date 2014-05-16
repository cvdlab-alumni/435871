#Homework 3 - exercise1
#Author: Davide Violante

from larcc import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

#home measurements
#wall external width
we = 0.25
#wall internal width
wi = 0.15

#totX = we+5+we+3.5+wi+4+wi+4+we
#totY = we+3.5+wi+2+wi+4.5+we

def cn(master):
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering(master,hpc)(range(len(master[1])),YELLOW,2)
	return hpc

#master form
m_shape = [5,7,2]
m_pattern = [[we,5,we,(3.5+wi+4+wi+4+we),we],
			[we,3.5,wi,2,wi,4.5,we],
			[0.2,3]]
			#0.2,3,0.4 roof

master = assemblyDiagramInit(m_shape)(m_pattern)
V,CV = master
hpc = cn(master)
#VIEW(hpc)

#3 rooms: lounge, myroom, bedroom
r3_shape = [5,1,1]
r3_pattern = [[3.5,wi,4,wi,4],[1],[1]]
r3 = assemblyDiagramInit(r3_shape)(r3_pattern)

master = diagram2cell(r3,master,53)
hpc = cn(master)
#VIEW(hpc)

#bathroom
bath_shape = [3,1,1]
bath_pattern = [[9,wi,3],[1],[1]]
bathroom = assemblyDiagramInit(bath_shape)(bath_pattern)

master = diagram2cell(bathroom,master,49)
hpc = cn(master)
#VIEW(hpc)

#kitchen
kit_shape = [3,1,1]
kit_pattern = [[8,wi,4],[1],[1]]
kitchen = assemblyDiagramInit(kit_shape)(kit_pattern)

master = diagram2cell(kitchen,master,45)
hpc = cn(master)
#VIEW(hpc)

#removing some parts 
toRemove = [0,1,2,3,14,15,16,17,75,77,74,72,71,69,67,25,23,21]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

hpc = cn(master)
#VIEW(hpc)

#loft, dividing the walls
loft_shape = [1,1,2]
loft_pattern = [[1],[1],[0.6,2.4]]
loft = assemblyDiagramInit(loft_shape)(loft_pattern)

toSplit = [11,1,2,3,4,5,10]
for i in range(len(toSplit)):
	master = diagram2cell(loft,master,toSplit[i])

hpc = cn(master)
#VIEW(hpc)

#loft, removing the walls
toRemove = [54,56,58,60,62,64,66]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

#removing some other parts
out1_shape = [3,1,1]
out1_pattern = [[8,wi,4],[1],[1]]
out1 = assemblyDiagramInit(out1_shape)(out1_pattern)

master = diagram2cell(out1,master,25)
master = diagram2cell(out1,master,24)
master = diagram2cell(out1,master,24)

toRemove = [10,11,12,13,63,60,57]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
DRAW(master)

hpc = cn(master)
VIEW(hpc)