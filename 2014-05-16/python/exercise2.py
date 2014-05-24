#Homework 3 - exercise2
#Author: Davide Violante

from larcc import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

#cn = cellNumbering
def cn(master):
	hpc = SKEL_1(STRUCT(MKPOLS(master)))
	hpc = cellNumbering(master,hpc)(range(len(master[1])),YELLOW,1)
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
#L=loft, K=kitchen, LO=lounge, M=myroom, P=parentsroom, WC=bathroom
Lx = 5; Ly = 4.5+2
LOx = 3.5; LOy = 4.5
Mx = Px = 4; My = Py = 4.5
Ky = 3.5
WCy = 2

#		  L     LO    M    P
totX = we+5+we+3.5+wi+4+wi+4+we+we
#		  K      WC   P
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

#removing cells to make the rooms
toRemove = [0,1,2,3,14,15,16,17,21,23,25,62,64,66,75,77,80,83,85,87,88,90,95]
master = rem(toRemove,master)
#hpc = cn(master)
#VIEW(hpc)
#DRAW(master)

# ----- DOORS ----- #
#main door and kitchen
d12_shape = [5,1,2]
d12_pattern = [[2.3,1.5,5.3,0.8,1.1+wi+2],[1],[2,0.8]]
d12 = assemblyDiagramInit(d12_shape)(d12_pattern)
master = diagram2cell(d12,master,32)

#doors: lounge, myroom, bedroom
d345_shape = [7,1,2]
d345_pattern = [[1.9,0.8,0.8+wi+2,0.8,1.2+wi+0.2,0.8,3],[1],[2,0.8]]
d345 = assemblyDiagramInit(d345_shape)(d345_pattern)
master = diagram2cell(d345,master,33)

#doors: bathroom
d6_shape = [1,3,2]
d6_pattern = [[1],[0.6,0.8,0.6],[2,0.8]]
d6 = assemblyDiagramInit(d6_shape)(d6_pattern)
master = diagram2cell(d6,master,59)

#doors: loft
d7_shape = [1,3,3]
d7_pattern = [[1],[0.6,0.8,0.6],[0.2,1.8,0.8]]
d7 = assemblyDiagramInit(d7_shape)(d7_pattern)
master = diagram2cell(d7,master,24)

#doors: elevator
d8_shape = [1,3,2]
d8_pattern = [[1],[2,1,0.5],[1.8,1]]
d8 = assemblyDiagramInit(d8_shape)(d8_pattern)
master = diagram2cell(d8,master,62)

#stairs hole
sh_shape = [2,1,1]
sh_pattern = [[2,2.5],[1],[1]]
sh = assemblyDiagramInit(sh_shape)(sh_pattern)
master = diagram2cell(sh,master,58)
master = diagram2cell(sh,master,65)

#removing doors to make entrable rooms
master = rem([70,74,80,84,88,94,102,109,113,115],master)
#hpc = cn(master)
#VIEW(hpc)
#DRAW(master)

# ----- WINDOWS ----- #
#heights
wh = [0.8,1.2,1]
#kitchen window
w1_shape = [1,5,3]
w1_pattern = [[1],[0.9,0.6,0.1,0.6,1.3],[1.2,0.8,1]]
w1 = assemblyDiagramInit(w1_shape)(w1_pattern)
master = diagram2cell(w1,master,61)

#kitchen window 2
w2_shape = [1,3,3]
w2_pattern = [[1],[0.4,0.8,2.3],wh]
w2 = assemblyDiagramInit(w2_shape)(w2_pattern)
master = diagram2cell(w2,master,37)

#bathroom window
w3_shape = [1,3,3]
w3_pattern = [[1],[0.6,0.8,0.6],wh]
w3 = assemblyDiagramInit(w3_shape)(w3_pattern)
master = diagram2cell(w3,master,40)

#bedroom window
#pattern 3 windows
wdiv3 = [1.2,0.6,0.1,0.6,0.1,0.6,1.3]
w4_shape = [1,7,3]
w4_pattern = [[1],wdiv3,wh]
w4 = assemblyDiagramInit(w4_shape)(w4_pattern)
master = diagram2cell(w4,master,43)

#lounge and myroom windows
w56_shape = [15,1,3]
w56_pattern = [[0.8,0.6,0.1,0.5,0.1,0.6,0.8,wi+1.1,0.6,0.1,0.5,0.1,0.6,1+wi,4+we],[1],wh]
w56 = assemblyDiagramInit(w56_shape)(w56_pattern)
master = diagram2cell(w56,master,33)

# ----- TOP FLOOR -----
#saving the master of current state to make a different one for top floor
mastertop = master
mastertop = rem([106,112, 121, 130, 139,145,151, 160,166,172, 181,187,193],mastertop)

#building the loft for 7th floor
loft_shape = [1,1,2]
loft_pattern = [[1],[1],[0.7,2.3]]
loft = assemblyDiagramInit(loft_shape)(loft_pattern)

loft2split = [1,2,3,4,5,11]
for i in range(len(loft2split)):
	mastertop = diagram2cell(loft,mastertop,loft2split[i])

mastertop = rem([183,185,187,189,191,193,195],mastertop)
#DRAW(mastertop)
# ----- END TOP FLOOR ----- #

#additional room window
w7_shape = [7,1,3]
w7_pattern = [wdiv3,[1],wh]
w7 = assemblyDiagramInit(w7_shape)(w7_pattern)
master = diagram2cell(w7,master,16)
master = diagram2cell(w3,master,3)

#removing windows to leave the holes (kitchen, kitchen2, bathroom, bedroom, myroom, lounge, addroom)
master = rem([104,110, 119, 128, 137,143,149, 158,164,170, 179,185,191, 203,209,215,224],master)
#hpc = cn(master)
#VIEW(hpc)
#DRAW(master)

# ---------- EXERCISE 2 BEGINS HERE ---------- #

# ----- GARAGES ----- #
garage_shape = [2,1,2]
garage_pattern = [[9,8.8],[totY],[we+0.05,3]]
garage = assemblyDiagramInit(garage_shape)(garage_pattern)

gar1_shape = [4,5,2]
gar1_pattern = [[1,3.5,we,4.25],[1.4,3.5,1,3.5,1.5],[2.5,0.7]]
gar1 = assemblyDiagramInit(gar1_shape)(gar1_pattern)

garage = diagram2cell(gar1,garage,3)
garage = rem([19,21,35,39],garage)

# hpc = cn(garage)
# VIEW(hpc)
# DRAW(garage)

#whole building structure
total_shape = [1,2,8]
total_pattern = [[totX],2*[totY],8*[we+3]]
total = assemblyDiagramInit(total_shape)(total_pattern)

total = diagram2cell(master,total,9)
total = diagram2cell(master,total,9)
total = diagram2cell(master,total,9)
total = diagram2cell(master,total,9)
total = diagram2cell(master,total,9)
total = diagram2cell(master,total,9)
total = diagram2cell(mastertop,total,9)

#specular apartment
masterS = larApply(s(1,-1,1))(master)
masterStop = larApply(s(1,-1,1))(mastertop)
total = diagram2cell(masterS,total,1)
total = diagram2cell(masterS,total,1)
total = diagram2cell(masterS,total,1)
total = diagram2cell(masterS,total,1)
total = diagram2cell(masterS,total,1)
total = diagram2cell(masterS,total,1)
total = diagram2cell(masterStop,total,1)
total = diagram2cell(garage,total,1)

hpc = cn(total)
#VIEW(hpc)
#DRAW(total)

# ----- PYPLASM PART BEGINS HERE ----- #
# ----- STAIRS ----- #
s1 = 0.5
s2 = 0.232
step2D = MKPOL([[[0,0],[0,s1],[s1,s2],[s1,s1]],[[1,2,3,4]],None])
step3D = MAP([S1,S3,S2])(PROD([step2D,Q(2)]))
stair = STRUCT(NN(15)([step3D,T([1,3])([s1,s2])]))
stair = R([1,2])(PI/2)(stair)
stair = T([1,2,3])([we+5+we+2,we+4.5+wi+2+we,3.2*6+0.05])(stair)
stairs = STRUCT(NN(6)([stair,T(3)(-3.2-0.05)]))

# ----- ROOF ----- #
roof1 = CUBOID([we+3.5+wi+4+wi+4+we+we,(we+4.5+wi+2+we+3.5+we)*2,0.8])
roof1 = T([1,2,3])([we+5,0,3.25*8])(roof1)
roof2 = CUBOID([we+3.5+wi+4+wi+4,(4.5+wi+2+we+3.5+we)*2,0.6])
roof2 = T([1,2,3])([we+5+we,we,3.25*8+0.2])(roof2)
roof = DIFFERENCE([roof1,roof2])

# ----- CORNICE ------ #
cornice1 = CUBOID([we+3.5+wi+4+wi+4+we+we+1.2,(we+4.5+wi+2+we+3.5+we+0.6)*2,0.2])
cornice1 = T([1,2,3])([we+5-0.6,-0.6,3.25*8])(cornice1)
cornice = DIFFERENCE([cornice1,(roof1)])
#maindoor fill
mdfill = CUBOID([2,Ky+we,we])
mdfill = T([1,2,3])([we+Lx+we,we+Ly+we+Ky+we+we,3.25])(mdfill)
roof = STRUCT([cornice, roof, mdfill])

# ----- BUILDING DOOR ----- #
maindoor1 = CUBOID([0.5,1.5,2])
maindoor1 = T([1,2,3])([we+Lx+we-0.25,we+Ly+we+Ky+Ky/2,3.25])(maindoor1)

#hole in a single cell
totalview = MKPOLS(total)

# hpc = cn(total)
# VIEW(hpc)
# DRAW(total)

totalview[19] = DIFFERENCE([totalview[19],maindoor1])

#function to make Bezier curve giving control points
def makeBez(cp):
	return MAP(BEZIER(S1)(cp))(INTERVALS(1)(32))

def disk2D(p):
	u,v = p
	return [v*COS(u),v*SIN(u)]

#custom function to make a 3D disk with given PI, height, radius and quality
def semiDisk(pi,h,r,q):
	return PROD([MAP(disk2D)(PROD([INTERVALS(pi)(q), INTERVALS(r)(3)])), Q(h)])

# q = totY*3
# street1 = makeBez([[0,0],[0,q+10],[-10,q],[q,q]])
# street2 = makeBez([[1.5,0],[1.5,q-1.5]])
# street3 = makeBez([[1.5,q-1.5],[q,q-1.5]])
# street4 = makeBez([[0,0],[1.5,0]])
# street5 = makeBez([[q,q],[q,q-1.5]])

# street = STRUCT([street1,street2,street3,street4,street5])
# street = PROD([SOLIDIFY(street), Q(0.1)])

# ----- SIDEWALK ----- #
sidewalk1 = CUBOID([2,totY*3,0.25])
sidewalk1 = T([1,2,3])([-2,0,3.25])(sidewalk1)
sidewalk2 = CUBOID([totX*3/2,2,0.25])
sidewalk2 = T([1,2,3])([0,-2,3.25])(sidewalk2)
cornerwalk = R([1,2])(PI)(semiDisk(PI/2,0.25,2,16))
cornerwalk = T([3])([3.25])(cornerwalk)

sidewalk3 = T([1])([-8])(sidewalk1)
sidewalk4 = T([2])([-8])(sidewalk2)
cornerwalk2 = R([1,2])(PI)(semiDisk(PI/2,0.25,10,16))
cornerwalk2 = T([3])([3.25])(cornerwalk2)
cornerwalk3 = R([1,2])(PI)(semiDisk(PI/2,0.25,8,16))
cornerwalk3 = T([3])([3.25])(cornerwalk3)
cornerA = DIFFERENCE([cornerwalk2,cornerwalk3])

sidewalk = STRUCT([sidewalk1,sidewalk2,cornerwalk,sidewalk3,sidewalk4,cornerA])

# ----- STREET ----- #
street1 = CUBOID([10,totY*3,0.25])
street1 = T([1,2,3])([-10,0,3])(street1)
street2 = CUBOID([totX*3/2,10,0.25])
street2 = T([1,2,3])([0,-10,3])(street2)
cornerstreet = R([1,2])(PI)(semiDisk(PI/2,0.25,10,16))
cornerstreet = T([3])([3])(cornerstreet)

street = STRUCT([street1,street2,cornerstreet,sidewalk])

# ----- RAMP ----- #
ramp1 = CUBOID([2,4,3.5])
ramp1 = T([1,2,3])([0,totY*2,0])(ramp1)

ptsramp = [[0,0,0],[0,4,0],[0,4,-3.5],[7,4,-3.5],[7,4,-3.25],[7,0,-3.5],[7,0,-3.25],[0,0,-3.5]]
ramp2 = JOIN(AA(MK)(ptsramp))
ramp2 = T([1,2,3])([2,totY*2,3.5])(ramp2)
ramp = STRUCT([ramp1,ramp2])
ramp2 = R([1,2])(PI/2)(ramp)
ramp2 = T(1)(totY*4)(ramp2)

ramps = STRUCT([ramp,ramp2])

# ----- GARAGE STREET ----- #
gs1 = CUBOID([totX-9,4,0.25])
gs1 = T([1,2,3])([9,totY*2,0])(gs1)

gs2 = CUBOID([4,totY*2-9,0.25])
gs2 = T([1,2,3])([totX,9,0])(gs2)

gscorner = semiDisk(PI/2,0.25,4,1)
gscorner = T([1,2])([totX,totY*2])(gscorner)

gs = STRUCT([gs1,gs2,gscorner])

# ----- GARAGE WALLS ----- #
gw1 = CUBOID([totX,we,3.5])
gw1 = T([1,2,3])([0,totY*2+4,0])(gw1)

gw2 = CUBOID([we,totY*2,3.5])
gw2 = T([1,2,3])([totX+4,0,0])(gw2)

gwcornerR = semiDisk(PI/2,3.5,4,1)
gwcornerR = T([1,2])([totX,totY*2])(gwcornerR)
gwcorner2 = semiDisk(PI/2,3.5,4.25,1)
gwcorner2 = T([1,2])([totX,totY*2])(gwcorner2)

gwcorner = DIFFERENCE([gwcorner2,gwcornerR])

gw = STRUCT([gw1,gw2,gwcorner])


#totalview = STRUCT(MKPOLS(total))
totalview = STRUCT(totalview)
VIEW(STRUCT([totalview, stairs, roof, street, ramps, gs, gw]))
