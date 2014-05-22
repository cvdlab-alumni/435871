#Homework 3 - exercise2
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
hpc = cn(master)
#VIEW(hpc)

#ROOMS
#3 rooms: lounge, myroom, bedroom
r3_shape = [5,1,1]
r3_pattern = [[3.5,wi,4,wi,4],[1],[1]]
r3 = assemblyDiagramInit(r3_shape)(r3_pattern)

master = diagram2cell(r3,master,53)
master = diagram2cell(r3,master,52)
hpc = cn(master)
#VIEW(hpc)

#bathroom
bath_shape = [3,1,1]
bath_pattern = [[9.5,wi,2.5],[1],[1]]
bathroom = assemblyDiagramInit(bath_shape)(bath_pattern)

master = diagram2cell(bathroom,master,48)
master = diagram2cell(bathroom,master,48)
hpc = cn(master)
#VIEW(hpc)

#kitchen
kit_shape = [5,1,1]
kit_pattern = [[4.5,we,3.25,we,4],[1],[1]]
kitchen = assemblyDiagramInit(kit_shape)(kit_pattern)

master = diagram2cell(kitchen,master,44)
master = diagram2cell(kitchen,master,44)
master = diagram2cell(kitchen,master,43)
master = diagram2cell(kitchen,master,42)

#removing cells to make the rooms
toRemove = [0,1,2,3,14,15,16,17,21,23,25,62,64,66,75,77,80,83,85,87,90,95]
master = rem(toRemove,master)
hpc = cn(master)
#VIEW(hpc)
#DRAW(master)

#DOORS
#main door and kitchen
d12_shape = [5,1,2]
d12_pattern = [[2,1.5,5.6,0.8,1.1+wi+2],[1],[2,0.8]]
d12 = assemblyDiagramInit(d12_shape)(d12_pattern)
master = diagram2cell(d12,master,32)
hpc = cn(master)
#VIEW(hpc)

#doors: lounge, myroom, bedroom
d345_shape = [7,1,2]
d345_pattern = [[1.9,0.8,0.8+wi+2,0.8,1.2+wi+0.2,0.8,3],[1],[2,0.8]]
d345 = assemblyDiagramInit(d345_shape)(d345_pattern)
master = diagram2cell(d345,master,33)
hpc = cn(master)
#VIEW(hpc)

#doors: bathroom
d6_shape = [1,3,2]
d6_pattern = [[1],[0.6,0.8,0.6],[2,0.8]]
d6 = assemblyDiagramInit(d6_shape)(d6_pattern)
master = diagram2cell(d6,master,59)
hpc = cn(master)
#VIEW(hpc)

#doors: loft
d7_shape = [1,3,3]
d7_pattern = [[1],[0.6,0.8,0.6],[0.2,2,0.6]]
d7 = assemblyDiagramInit(d7_shape)(d7_pattern)
master = diagram2cell(d7,master,24)
hpc = cn(master)
VIEW(hpc)

exit()

#last floor with loft
mastertop = master
hpctop = cn(mastertop)
#VIEW(hpctop)
#DRAW(mastertop)

# #loft of the top apartment
# loft_shape = [1,1,2]
# loft_pattern = [[1],[1],[0.6,2.4]]
# loft = assemblyDiagramInit(loft_shape)(loft_pattern)

# loft2split = [11,1,2,3,4,5,10]
# for i in range(len(loft2split)):
# 	mastertop = diagram2cell(loft,mastertop,loft2split[i])

# mastertop = rem([70,72,74,76,78,80,82],mastertop)

# hpctop = cn(mastertop)
# VIEW(hpctop)
# DRAW(mastertop)
# #end loft


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

#specular apartment
masterS = larApply(s(1,-1,1))(master)
total = diagram2cell(masterS,total,1)
total = diagram2cell(masterS,total,1)
total = diagram2cell(masterS,total,1)
total = diagram2cell(masterS,total,1)
total = diagram2cell(masterS,total,1)
total = diagram2cell(masterS,total,1)

hpc = cn(total)
#VIEW(hpc)
#DRAW(total)



#removing some parts 
master = rem([0,1,2,3,14,15,16,17,75,77,74,72,71,69,67,25,23,21],master)
#DRAW(master)

hpc = cn(master)
#VIEW(hpc)

# #loft, dividing the walls
# loft_shape = [1,1,2]
# loft_pattern = [[1],[1],[0.6,2.4]]
# loft = assemblyDiagramInit(loft_shape)(loft_pattern)

# toSplit = [11,1,2,3,4,5,10]
# for i in range(len(toSplit)):
# 	master = diagram2cell(loft,master,toSplit[i])

# hpc = cn(master)
# #VIEW(hpc)

# #loft, removing the walls
# master = rem([54,56,58,60,62,64,66],master)
# #DRAW(master)

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
#DRAW(master)

hole_shape = [2,1,1]
hole_pattern = [[4,4],[1],[1]]
hole = assemblyDiagramInit(hole_shape)(hole_pattern)
master = diagram2cell(hole,master,48)
hpc = cn(master)
#VIEW(hpc)
master = rem([166],master)
#DRAW(master)

########## Exercise 2 begins here ##########

#creating the main building
building = assemblyDiagramInit([1,2,7])([[we+5+wi+3.5+wi+4+wi+4+we],2*[we+7+we+3.5+we],7*[3.2]])
hpcB = cn(building)
building = diagram2cell(master,building,13)
hpcB = cn(building)
#VIEW(hpcB)

#creating the several apartments
masterR = larApply(s(1,-1,1))(master)
#masterR = larApply(t(0,0.25,0))(masterR)
building = diagram2cell(masterR,building,6)
building = diagram2cell(master,building,11)
building = diagram2cell(master,building,10)
building = diagram2cell(master,building,9)
building = diagram2cell(master,building,8)
building = diagram2cell(master,building,7)
building = diagram2cell(master,building,6)
building = diagram2cell(masterR,building,5)
building = diagram2cell(masterR,building,4)
building = diagram2cell(masterR,building,3)
building = diagram2cell(masterR,building,2)
building = diagram2cell(masterR,building,1)
building = diagram2cell(masterR,building,0)
hpcB = cn(building)

#testing colors
# building = MKPOLS(building)
# building[8] = COLOR(Color4f([(1),(0),(0)]))(building[8])
# structBuilding = STRUCT(building)

structBuilding = STRUCT(MKPOLS(building))

fill = CUBOID([4-0.12,0.35,0.2])
fill = T([1,2,3])([5+we+wi,7+we+4-wi-0.02,3.2*6])(fill)
fills = STRUCT(NN(7)([fill,T(3)(-3.2)]))

#additional walls
muroint = CUBOID([we,7.7,3.2*7])
muroint = T([1,2])([we+5+4,we+7+wi])(muroint)
muroint2 = T(1)(-4.1)(muroint)
muriint = STRUCT([muroint,muroint2])

muroext = CUBOID([we,7+we+wi,6*3.2])
muroext = T(1)(-0.01)(muroext)
muroext2 = T(2)(we+wi+7+7.7)(muroext)
muroext3 = CUBOID([we+5,0.25,3.2*6])
muroext3 = T(2)(-0.01)(muroext3)
muroext4 = T(2)(7+wi+0.025)(muroext3)
muroext5 = T(2)(7.7+we-0.035)(muroext4)
muroext6 = T(2)(7+we-0.075)(muroext5)
muriext = STRUCT([muroext,muroext2,muroext3,muroext4,muroext5,muroext6])

#additional windows
ww = CUBOID([0.5,0.5,1])
ww = T([1,2,3])([5,we+wi+7+3.5,1])(ww)
wwn = STRUCT(NN(7)([ww,T(3)(3.2)]))
wris = DIFFERENCE([muriint,wwn])

ww2 = CUBOID([0.5,0.5,1])
wwn2 = STRUCT(NN(3)([ww2,T(2)(0.6)]))
wwn2 = T([1,2,3])([-0.2,3,1])(wwn2)
wwnn = STRUCT(NN(6)([wwn2,T(3)(3.2)]))
wwnn2 = T([2])([15])(wwnn)
wwnntot = STRUCT([wwnn,wwnn2])
wwris = DIFFERENCE([muriext,wwnntot])

#entrances
ent = CUBOID([1.5,0.5,2.2])
ent = T([1,2])([2,-0.2])(ent)
ent2 = T([2])([22.4])(ent)
enttot = STRUCT([ent,ent2])
entris2 = DIFFERENCE([structBuilding,enttot])
entris3 = DIFFERENCE([wwris,enttot])

#elevator
elev = CUBOID([1.5,1.5,2.2])
elev = T([1,2,3])([9.7,7.6,0.2])(elev)
wire1 = CUBOID([0.05,0.05,20])
wire1 = T([1,2,3])([10.3,8.2,2.4])(wire1)
wire2 = T([2])([0.2])(wire1)
wires = STRUCT([wire1,wire2])
elev1 = STRUCT([wires,elev])
elev2 = T([2])([5.8])(elev1)
elevs = STRUCT([elev1,elev2])

#roof
roof = CUBOID([13.6,23.5,0.5])
roof = T([1,2,3])([4.2+we-0.05,-0.5,3.2*7])(roof)

#transparent roof just to make the interiors visibles!
#remove this line to add the roof
#roof = MATERIAL([1,1,1,0, 0,0,0,0.2, 0,0,0,0, 0,0,0,0, 100])(roof)

#ground floor
groundbig = CUBOID([37,38.5,0.2])
groundbig = T([1,2,3])([-10,-8,-0.2])(groundbig)

dom = INTERVALS(1)(32)
gr1 = BEZIER(S1)([[0,0],[0,10],[10,10],[10,8]])
gr2 = BEZIER(S1)([[0,0],[2,0],[2,8],[10,8]])
gr1 = MAP(gr1)(dom)
gr2 = MAP(gr2)(dom)
ground = SOLIDIFY(STRUCT([gr1,gr2]))
ground = PROD([ground,Q(0.7)])
ground = T([1,2,3])([-10,-8,0])(ground)

ground2 = R([3,1])(PI)(ground)
ground2 = T([1,2,3])([17,0,0.7])(ground2)
groundf = STRUCT([ground,ground2])

groundr = R([1,2])(PI)(groundf)
groundr = T([1,2])([17,22.5])(groundr)

OCRA = rgb([255, 243, 190])
grounds = COLOR(OCRA)(STRUCT([groundf,groundr,groundbig]))

OCRA2 = rgb([255, 220, 150])
colorato = COLOR(OCRA2)(STRUCT([fills,wris,entris2,entris3,elevs,SKEL_1(roof)]))

VIEW(STRUCT([colorato,grounds]))
