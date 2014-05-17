#Homework 3 - exercise1
#Author: Davide Violante

from larcc import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

#cn = cellNumbering
def cn(master):
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering(master,hpc)(range(len(master[1])),YELLOW,0.6)
	return hpc

#rem = remove: remove walls
def rem(toRemove,master):
	return (master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)])

#home measurements
#wall external width
we = 0.25
#wall internal width
wi = 0.15

#totX = we+5+we+3.5+wi+4+wi+4+we
#totY = we+3.5+wi+2+wi+4.5+we

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

#ROOMS
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
master = rem([0,1,2,3,14,15,16,17,75,77,74,72,71,69,67,25,23,21],master)
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
master = rem([54,56,58,60,62,64,66],master)
#DRAW(master)

#removing some other parts
out1_shape = [3,1,1]
out1_pattern = [[8,wi,4],[1],[1]]
out1 = assemblyDiagramInit(out1_shape)(out1_pattern)

master = diagram2cell(out1,master,25)
master = diagram2cell(out1,master,24)
master = diagram2cell(out1,master,24)

master = rem([10,11,12,13,60,57],master)
#DRAW(master)

hpc = cn(master)
#VIEW(hpc)

#DOORS
d12_shape = [5,1,2]
d12_pattern = [[2,1.5,5.5,0.6,1.4+wi+2],[1],[2,0.8]]
d12 = assemblyDiagramInit(d12_shape)(d12_pattern)
master = diagram2cell(d12,master,21)
hpc = cn(master)
#VIEW(hpc)
#removing the doors to make the doors
master = rem([61,65],master)
#DRAW(master)

d345_shape = [7,1,2]
d345_pattern = [[2,0.7,0.8+wi+2,0.7,1.3+wi+0.15,0.7,3.15],[1],[2,0.8]]
d345 = assemblyDiagramInit(d345_shape)(d345_pattern)
master = diagram2cell(d345,master,23)
hpc = cn(master)
#VIEW(hpc)
master = rem([68,72,76],master)
#DRAW(master)

d6_shape = [1,3,2]
d6_pattern = [[1],[0.5,0.6,0.9],[2,0.8]]
d6 = assemblyDiagramInit(d6_shape)(d6_pattern)
master = diagram2cell(d6,master,13)
hpc = cn(master)
#VIEW(hpc)
master = rem([78],master)
#DRAW(master)

d7_shape = [1,3,2]
d7_pattern = [[1],[0.65,0.7,0.65],[2,0.8]]
d7 = assemblyDiagramInit(d7_shape)(d7_pattern)
master = diagram2cell(d7,master,41)
hpc = cn(master)
#VIEW(hpc)
master = rem([82],master)
#DRAW(master)

#WINDOWS
w1_shape = [1,5,3]
w1_pattern = [[1],[0.9,0.6,0.1,0.6,1.3],[1.2,0.8,1]]
w1 = assemblyDiagramInit(w1_shape)(w1_pattern)
master = diagram2cell(w1,master,41)
hpc = cn(master)
#VIEW(hpc)
master = rem([88,94],master)
#DRAW(master)

w2_shape = [1,3,3]
w2_pattern = [[1],[0.9,0.6,2],[1.2,0.8,1]]
w2 = assemblyDiagramInit(w2_shape)(w2_pattern)
master = diagram2cell(w2,master,28)
hpc = cn(master)
#VIEW(hpc)
master = rem([100],master)
#DRAW(master)

w3_shape = [1,3,3]
w3_pattern = [[1],[0.5,1,0.5],[1.2,0.8,1]]
w3 = assemblyDiagramInit(w3_shape)(w3_pattern)
master = diagram2cell(w3,master,31)
hpc = cn(master)
#VIEW(hpc)
master = rem([107],master)
#DRAW(master)

w4_shape = [1,7,3]
w4_pattern = [[1],[1.2,0.6,0.1,0.6,0.1,0.6,1.3],[1,1,1]]
w4 = assemblyDiagramInit(w4_shape)(w4_pattern)
master = diagram2cell(w4,master,34)
hpc = cn(master)
#VIEW(hpc)
master = rem([114,120,126],master)
#DRAW(master)

w56_shape = [15,1,3]
w56_pattern = [[0.8,0.6,0.1,0.5,0.1,0.6,0.8,wi+1.1,0.6,0.1,0.5,0.1,0.6,1+wi,4+we],[1],[1,1,1]]
w56 = assemblyDiagramInit(w56_shape)(w56_pattern)
master = diagram2cell(w56,master,24)
hpc = cn(master)
#VIEW(hpc)
master = rem([131,137,143,152,158,164],master)
DRAW(master)
