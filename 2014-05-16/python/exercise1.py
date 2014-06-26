#Homework 3 - exercise1
#Author: Davide Violante

from larcc import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

#cn = cellNumbering
def cn(master):
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering(master,hpc)(range(len(master[1])),YELLOW,2)
	return hpc

#rem = remove: remove walls
def rem(toRemove,master):
	return (master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)])

#function for custom colors with 0:255 numbers
def rgb(c):
	return [c[0]/255.0, c[1]/255.0, c[2]/255.0]

#APARTMENT MEASUREMENTS
#wall external width
we = 0.25
#wall internal width
wi = 0.15

#total width, length and height of the apartment in meters
totX = we+5+we+3.5+wi+4+wi+4+we+we
totY = we+3.5+we+2+wi+4.5+we
totZ = we+3

#master form
m_shape = [5,7,2]
m_pattern = [[we,5,we,(3.5+wi+4+wi+4+we),we],
			[we,3.5,we,2,wi,4.5,we],
			[we,3]]

master = assemblyDiagramInit(m_shape)(m_pattern)
V,CV = master

# ----- ROOMS ----- #
#3 rooms: lounge, myroom, bedroom
r3_shape = [5,1,1]
r3_pattern = [[3.5,wi,4,wi,4],[1],[1]]
r3 = assemblyDiagramInit(r3_shape)(r3_pattern)

master = diagram2cell(r3,master,53)
master = diagram2cell(r3,master,52)

#bathroom
bath_shape = [3,1,1]
bath_pattern = [[9.5,wi,2.5],[1],[1]]
bathroom = assemblyDiagramInit(bath_shape)(bath_pattern)

master = diagram2cell(bathroom,master,48)
master = diagram2cell(bathroom,master,48)

#kitchen
kit_shape = [5,1,1]
kit_pattern = [[4.5,we,3.25,we,4],[1],[1]]
kitchen = assemblyDiagramInit(kit_shape)(kit_pattern)

master = diagram2cell(kitchen,master,44)
master = diagram2cell(kitchen,master,44)
master = diagram2cell(kitchen,master,43)
master = diagram2cell(kitchen,master,42)

hpc = cn(master)
#VIEW(hpc)
#removing cells to make the rooms
# toRemove = [0,1,2,3,14,15,16,17,21,23,25,62,64,66,75,77,80,83,85,87,88,90,95]
# master = rem(toRemove,master)
# hpc = cn(master)
# VIEW(hpc)
#DRAW(master)


# ----- DOORS ----- #
#main door and kitchen
d12_shape = [5,1,2]
d12_pattern = [[2.2,1.25,5.7,0.85,1.0+wi+2],[1],[2.1,0.9]]
d12 = assemblyDiagramInit(d12_shape)(d12_pattern)
master = diagram2cell(d12,master,43)

#doors: lounge, myroom, bedroom
d345_shape = [7,1,2]
d345_pattern = [[1.9,0.85,0.75+wi+2,0.85,1.15+wi+0.2,0.85,2.95],[1],[2.1,0.9]]
d345 = assemblyDiagramInit(d345_shape)(d345_pattern)
master = diagram2cell(d345,master,44)

#doors: bathroom
d6_shape = [1,3,2]
d6_pattern = [[1],[0.6,0.85,0.55],[2.1,0.9]]
d6 = assemblyDiagramInit(d6_shape)(d6_pattern)
master = diagram2cell(d6,master,74)

#doors: loft
d7_shape = [1,3,3]
d7_pattern = [[1],[0.6,0.8,0.6],[0.2,1.9,0.9]]
d7 = assemblyDiagramInit(d7_shape)(d7_pattern)
master = diagram2cell(d7,master,35)

#doors: elevator
d8_shape = [1,3,2]
d8_pattern = [[1],[2,1,0.5],[1.9,1.1]]
d8 = assemblyDiagramInit(d8_shape)(d8_pattern)
master = diagram2cell(d8,master,80)

#stairs hole
# sh_shape = [2,1,1]
# sh_pattern = [[2,2.5],[1],[1]]
# sh = assemblyDiagramInit(sh_shape)(sh_pattern)
# master = diagram2cell(sh,master,74)
# master = diagram2cell(sh,master,65)


#removing doors to make entrable rooms
#master = rem([70,74,80,84,88,94,102,109,113,115],master)
#hpc = cn(master)
#VIEW(hpc)
#DRAW(master)

# ----- WINDOWS ----- #
#heights
wh = [0.9,1.2,0.9]
#kitchen window
w1_shape = [1,3,3]
w1_pattern = [[1],[0.9,1.2,1.4],wh]
w1 = assemblyDiagramInit(w1_shape)(w1_pattern)
master = diagram2cell(w1,master,81)

#kitchen window 2
w2_shape = [1,3,3]
w2_pattern = [[1],[0.4,0.7,2.4],wh]
w2 = assemblyDiagramInit(w2_shape)(w2_pattern)
master = diagram2cell(w2,master,48)

#bathroom window
w3_shape = [1,3,3]
w3_pattern = [[1],[0.5,1,0.5],wh]
w3 = assemblyDiagramInit(w3_shape)(w3_pattern)
master = diagram2cell(w3,master,51)

#bedroom window
#pattern 3 windows
wdiv3 = [1.4,1.8,1.3]
w4_shape = [1,3,3]
w4_pattern = [[1],wdiv3,wh]
w4 = assemblyDiagramInit(w4_shape)(w4_pattern)
master = diagram2cell(w4,master,54)

#lounge and myroom windows
w56_shape = [7,1,3]
w56_pattern = [[0.8,1.8,0.9,wi+1.2,1.8,1+wi,4+we],[1],wh]
w56 = assemblyDiagramInit(w56_shape)(w56_pattern)
master = diagram2cell(w56,master,44)

# ----- TOP FLOOR -----
#saving the master of current state to make a different one for top floor
#mastertop = master
#mastertop = rem([106,112, 121, 130, 139,145,151, 160,166,172, 181,187,193],mastertop)


loft_shape1 = [1,1,2]
loft_pattern1 = [[1],[1],[2,1]]
loft1 = assemblyDiagramInit(loft_shape1)(loft_pattern1)
master = diagram2cell(loft1,master,19)

#building the loft for 7th floor
loft_shape = [1,1,2]
loft_pattern = [[1],[1],[0.8,2.2]]
loft = assemblyDiagramInit(loft_shape)(loft_pattern)
master = diagram2cell(loft,master,5)
master = diagram2cell(loft,master,6)
master = diagram2cell(loft,master,7)
master = diagram2cell(loft,master,8)
master = diagram2cell(loft,master,9)
master = diagram2cell(loft,master,21)

hpc = cn(master)
#VIEW(hpc)
#master = rem([0,1,2,3,9,10,11,12, 15,17,19, 48,50,52,61,62,65,68,69,70, 83,87,93,97,101,107,115,122, 130,139,148,157,166,175, 184,186,188,190,192,194,196],master)
#DRAW(master)

emptyChain = [0,1,2,3,9,10,11,12, 15,17,19, 48,50,52,61,62,65,68,69,70, 83,87,93,97,101,107,115,122, 130,139,148,157,166,175, 184,186,188,190,192,194,196]

#CREDITS TO Leonardo Tilomelli for these functions
def extractFacets(master, emptyChain=[]):
    solidCV = [cell for k,cell in enumerate(master[1]) if not (k in emptyChain)]
    exteriorCV =  [cell for k,cell in enumerate(master[1]) if k in emptyChain]
    exteriorCV += exteriorCells(master)
    CV = solidCV + exteriorCV
    V = master[0]
    FV = [f for f in larFacets((V,CV),3,len(exteriorCV))[1] if len(f) >= 4]
    BF = boundaryCells(solidCV,FV)
    boundaryFaces = [FV[face] for face in BF]
    B_Rep = V,boundaryFaces
    return B_Rep

def extractTriaFacets(master, emptyChain=[]):
    master = extractFacets(master,emptyChain)
    master = quads2tria(master)
    return master

def objExporter((V,FV), filePath):
    out_file = open(filePath,"w")
    out_file.write("# List of Vertices:\n")
    for v in V:
        out_file.write("v")
        for c in v:
            out_file.write(" " + str(c))
        out_file.write("\n")
    out_file.write("# Face Definitions:\n")
    for f in FV:
        out_file.write("f")
        for v in f:
            out_file.write(" " + str(v+1))
        out_file.write("\n")
    out_file.close()

master_factes_tria = extractTriaFacets(master, emptyChain)
objExporter(master_factes_tria, "F:\master435871.obj")

exit()


# loft2split = [1,2,3,4,5,11]
# for i in range(len(loft2split)):
# 	mastertop = diagram2cell(loft,mastertop,loft2split[i])


#mastertop = rem([183,185,187,189,191,193,195],mastertop)
DRAW(mastertop)
# ----- END TOP FLOOR ----- #

#additional room window
w7_shape = [7,1,3]
w7_pattern = [wdiv3,[1],wh]
w7 = assemblyDiagramInit(w7_shape)(w7_pattern)
master = diagram2cell(w7,master,16)
master = diagram2cell(w3,master,3)

#removing windows to leave the holes (kitchen, kitchen2, bathroom, bedroom, myroom, lounge, addroom)
master = rem([104,110, 119, 128, 137,143,149, 158,164,170, 179,185,191, 203,209,215,224],master)

hpc = cn(mastertop)
#VIEW(hpc)
#DRAW(mastertop)

# ----- COLORS ----- #
mastertop = MKPOLS(mastertop)

#loft
C_LOFT = rgb([255,200,153])
listLoft = [5,6,0,1,2,3,4,10,182,183,184,185,186,187]
for i in range(len(listLoft)):
	mastertop[listLoft[i]] = COLOR(C_LOFT)(mastertop[listLoft[i]])

#lounge
c_LON = rgb([255,230,153])
mastertop[40] = COLOR(c_LON)(mastertop[40])
#myroom
c_MY = rgb([217,255,204])
mastertop[42] = COLOR(c_MY)(mastertop[42])
#bedroom
c_BED = rgb([255,218,204])
mastertop[44] = COLOR(c_BED)(mastertop[44])
#bath
c_BATH = rgb([194,255,241])
mastertop[47] = COLOR(c_BATH)(mastertop[47])
#kitchen
c_BATH = rgb([255,255,179])
mastertop[50] = COLOR(c_BATH)(mastertop[50])
#bath
c_BATH = rgb([222,222,222])
mastertop[45] = COLOR(c_BATH)(mastertop[45])

#end colors

VIEW(STRUCT(mastertop))
