from pyplasm import *
from larcc import *
from myfont import *
from random import random

#Homework 1 - exercise4
#Author: Davide Violante

#function for custom colors with 0:255 numbers
def rgb(c):
	return [c[0]/255.0, c[1]/255.0, c[2]/255.0]

#function for HALF sphere
def larSphere(radius=1):
	def larSphere0(shape=[10,20]):
		V,CV = larIntervals(shape)([PI,PI])
		V = translatePoints(V,[0,PI])
		domain = V,CV
		x = lambda V : [radius*COS(p[0])*SIN(p[1]) for p in V]
		y = lambda V : [radius*COS(p[0])*COS(p[1]) for p in V]
		z = lambda V : [radius*SIN(p[0]) for p in V]
		return larMap([x,y,z])(domain)
	return larSphere0

#function for a ball that recall function for HALF sphere
def larBall(radius=1):
	def larBall0(shape=[10,10]):
		V,CV = checkModel(larSphere(radius)(shape))
		return V,[range(len(V))]
	return larBall0

#function for HALF cylinder
def larCylinder(params):
	radius,height= params
	def larCylinder0(shape=[36,1]):
		domain = larIntervals(shape)([PI,1])
		V,CV = domain
		x = lambda V : [radius*COS(p[0]) for p in V]
		y = lambda V : [radius*SIN(p[0]) for p in V]
		z = lambda V : [height*p[1] for p in V]
		mapping = [x,z,y]
		model = larMap(mapping)(domain)
		# model = makeOriented(model)
		return model
	return larCylinder0

#function for a Rod that recall function for HALF cylinder
def larRod(params):
	radius,height = params
	def larRod0(shape=[36,1]):
		V,CV = checkModel(larCylinder(params)(shape))
		return V,[range(len(V))]
	return larRod0

#custom colors
OCRA0 = rgb([140, 90, 0.0])
OCRA1 = rgb([160, 110, 0.0])
OCRA2 = rgb([180, 130, 0.0])
OCRA3 = rgb([200, 150, 0.0])
OCRA3A = rgb([220, 170, 0.0])
OCRA4 = rgb([230, 190, 0.0])
OCRA5 = rgb([240, 210, 50])
OCRA6 = rgb([240, 210, 80])
OCRA7 = rgb([240, 220, 110])
OCRA8 = rgb([255, 220, 140])

#def heights of the floors
H1 = 1
H2 = 2
H3 = 3
H3col = 3.001 #prevent glittering
H3int = 3.002 #prevent glittering
H4 = 13

#------------- BASE -------------#
#floor0: sand - base
pts0 = [[0,0],[0,50],[50,50],[50,0]]
floor0 = JOIN(AA(MK)(pts0))
floor0_3d = COLOR(OCRA1)(PROD([floor0, Q(1)]))

#HW2: DETAILS -> miniblocks
halfball = larBall(0.5)()
halfball = T(3)(0.5)(STRUCT(MKPOLS(halfball)))
blkcil = CYLINDER([0.5,0.5])(20)
blk = STRUCT([halfball,blkcil])
blk = T([1,2,3])([7,13,1])(blk)
blks_l = STRUCT(NN(10)([blk,T(1)(4)]))
blks_r = T(2)(24)(blks_l)
blk2 = T([1,2,3])([-4,4,0])(blk)
blks_f = STRUCT(NN(5)([blk2,T(2)(4)]))
blks_b = T(1)(44)(blks_f)

blks = COLOR(OCRA4)(STRUCT([blks_l,blks_r,blks_f,blks_b]))

#floor1: 1st stair - base
pts1 = [[0,0],[0,20],[40,20],[40,0]]
floor1 = JOIN(AA(MK)(pts1))
floor1_3d = COLOR(OCRA1)(T([1,2,3])([5,15,H1])(PROD([floor1, Q(1)])))

#floor2: 2nd stair - base
pts2 = [[0,0],[0,19],[39,19],[39,0]]
floor2 = JOIN(AA(MK)(pts2))
floor2_3d = COLOR(OCRA2)(T([1,2,3])([5.5,15.5,H2])(PROD([floor2, Q(1)])))

#------------- INTERMEDIATE -------------#
#floor3: interior and columns - intermediate
pts3 = [[0,0],[0,18],[38,18],[38,0]]
floor3base = COLOR(OCRA3)(JOIN(AA(MK)(pts3)))
floor3base = T([1,2,3])([6,16,H3])(floor3base)

#column
column = COLOR(OCRA3A)(JOIN(CYLINDER([0.8,H4-H3])(30)))
column = T([1,2,3])([7,17,H3col])(column)

#HW2: DETAILS -> column bases
#column base and column top
cbase = COLOR(OCRA3A)(JOIN(CUBOID([2,2,0.45])))
cbase = T([1,2,3])([6,16,H3col])(cbase)
ctopbase = COLOR(OCRA3A)(JOIN(CUBOID([2,2,0.45])))
ctopbase = T([1,2,3])([6,16,H4-0.45])(ctopbase)

column = STRUCT([column,cbase,ctopbase])

#cloning and positioning columns
columns_x = STRUCT([column, T(1)(3.28)]*12)
columns_y = STRUCT([column, T(2)(3.2)]*6)
columns_xcopy = STRUCT([columns_x, T(2)(16)]*2)
columns_ycopy = STRUCT([columns_y, T(1)(36.08)]*2)
column2fronta = T([1,2])([6,6])(column)
column2frontb = T([1,2])([6,9.5])(column)
columns_front = STRUCT([column2fronta, column2frontb])
columns_rear = STRUCT([columns_front, T(1)(21)]*2)

columnsTOT = STRUCT([columns_x, columns_y, columns_xcopy, columns_ycopy, columns_front, columns_rear])
ctopbaseTOT = STRUCT([ctopbase])

interior1 = CUBOID([23,0.5,H4-H3])
interior1 = T([1,2,3])([12,20,H3int])(interior1)
interior2 = CUBOID([2,3,H4-H3])
interior2 = T([1,2,3])([15,20.5,H3int])(interior2)
interior3 = CUBOID([0.5,9,H4-H3])
interior3 = T([1,2,3])([31,20.5,H3int])(interior3)

interior1b = T([2])([9])(interior1)
interior2b = T([2])([5.5])(interior2)

#HW2: EXERCISE2 -> windows!
squarehole = CUBOID([2,1,6])
squarehole = T([1,2,3])([27,19.7,3])(squarehole)
halfcirclehole = STRUCT(MKPOLS(larRod([1,1])()))
halfcirclehole = T([1,2,3])([28,19.7,9])(halfcirclehole)
holeint = STRUCT([squarehole,halfcirclehole])
holeints = STRUCT(NN(4)([holeint,T(1)(-2.7)]))
holeints2 = T(2)(9)(holeints)

holeint1 = DIFFERENCE([interior1,holeints])
holeint2 = DIFFERENCE([interior1b,holeints2])

interiorTOT = COLOR(OCRA3A)(STRUCT([interior2, interior3, interior2b, holeint1, holeint2]))

floor3_3d = STRUCT([columnsTOT,ctopbaseTOT,interiorTOT,blks])

#------------- ROOF -------------#
#floor4: top of the columns - roof
floor4a = T([1,2])([2,2])((CUBOID([34,14])))
floor4b = CUBOID([38,18])
floor4 = DIFFERENCE([floor4b,floor4a])
floor4 = T([1,2,3])([6,16,H4])(PROD([floor4, Q(1)]))

floor4coltop = CUBOID([2,9.5,1])
floor4coltopfront = T([1,2,3])([12,20,H4])(floor4coltop)
floor4coltoprear = T([1,2,3])([33,20,H4])(floor4coltop)

#HW2: DETAILS -> top interior girder
floor4coltop1 = CUBOID([2,8.5,0.7])
floor4coltopfront1 = T([1,2,3])([12,20.5,H4+1])(floor4coltop1)
floor4coltop2 = CUBOID([2,7.5,0.7])
floor4coltopfront2 = T([1,2,3])([12,21,H4+1.7])(floor4coltop2)
floor4coltop3 = CUBOID([2,6,0.7])
floor4coltopfront3 = T([1,2,3])([12,21.75,H4+2.4])(floor4coltop3)
floor4coltopfrontTOT = STRUCT([floor4coltopfront1,floor4coltopfront2,floor4coltopfront3])

#top triangle
npts = [[0,0,0],[0,18,0],[0,9,4],
		[-2,0,0],[-2,18,0],[-2,9,4]]
tri = JOIN(AA(MK)(npts))
tri = T([1,2,3])([8,16,H4+3])(tri)

tri_small1 = S([1,2,3])([0.2,0.8,0.8])(tri)
tri_small1 = T([1,2,3])([4.7,5,3.5])(tri_small1)
tri_small2 = T([1,2,3])([2,0,0])(tri_small1)
#relief
tridiff = COLOR(OCRA8)(DIFFERENCE([tri,tri_small1,tri_small2]))

#HW2: DETAILS -> triangle hole
triangle_hole = S([1,2,3])([1.3,0.1,0.4])(tri)
triangle_hole = T([1,2,3])([4,22.5,7.5])(triangle_hole)
triangle_hole1 = DIFFERENCE([floor4coltopfrontTOT,triangle_hole])

floor4_3d = COLOR(OCRA4)((STRUCT([floor4,floor4coltopfront,floor4coltoprear,triangle_hole1])))

#triangle supporter
trave = CUBOID([-2,18,2])
trave = T([1,2,3])([8,16,H4+1])(trave)
trave_small1 = S([1,2,3])([0.2,0.97,0.8])(trave)
trave_small1 = T([1,2,3])([4.7,0.74,3])(trave_small1)
trave_small2 = T([1,2,3])([2,0,0])(trave_small1)
travediff = COLOR(OCRA7)(DIFFERENCE([trave,trave_small1,trave_small2]))

#HW2: DETAILS -> relief on front
dash = CUBOID([1.8,0.2,1])
dash1 = T([1,2,3])([6.2,17,H4+1.5])(dash)
dash2 = T([1,2,3])([6.2,17.3,H4+1.5])(dash)
dash3 = T([1,2,3])([6.2,17.6,H4+1.5])(dash)
dash123 = STRUCT([dash1,dash2,dash3])
dashes = COLOR(OCRA7)(STRUCT(NN(6)([dash123,T(2)(3)])))

topsides1 = T([1,2,3])([8,16,H4+1])(CUBOID([4,1,2]))
topsides2 = T([2])([17])(topsides1)
topsides = COLOR(OCRA7)(STRUCT([topsides1,topsides2]))

north = STRUCT([tridiff,travediff,dashes])

#south plan
south = T([1])([36])(north)

#north and south together
vertical = STRUCT([north,south,topsides])

two_and_half_model = STRUCT([floor0_3d,floor1_3d,floor2_3d,floor3_3d,floor4_3d])
solid_model_3D = STRUCT([two_and_half_model,vertical])

#final view
#VIEW(solid_model_3D)
#VIEW(SKELETON(1)(solid_model_3D))

#HW2: NEIGHBOURHOOD

BLACK1 = rgb([40, 40, 40])
BLACK2 = rgb([60, 60, 60])
GREY1 = rgb([155, 155, 155])
GREY2 = rgb([120, 120, 120])
BLUE1 = rgb([0, 40, 160])
LIGHTBLUE = rgb([180, 255, 255])
BEIGE = rgb([255, 255, 200])
GREY3 = rgb([222, 222, 222])

#sidewalk
sidewalk1 = CUBOID([110,-3,1])
sidewalk1 = T([1,2])([-30,0])(sidewalk1)
sidewalk2 = T([2])([-12-3])(sidewalk1)
sidewalks = COLOR(BLACK2)(STRUCT([sidewalk1,sidewalk2]))

#road
road = CUBOID([110,-12,0.6])
road = COLOR(BLACK1)(T([1,2])([-30,-3])(road))

#road details: lamps with lights
lampcil = T([1,2,3])([-29,-2,1])(CYLINDER([0.2,14])(10))
lampcilbase = T([1,2,3])([-29,-2,1])(CYLINDER([0.3,2])(10))
lampsquare = T([1,2,3])([-29.2,-1.8,15])(CUBOID([0.4,-2,0.5]))

lightcone = CONE([3.5,14.5])(16)
lightcone = MATERIAL([1,1,1,0, 0,0,0,0.1, 0,0,0,0, 0,0,0,0, 100])(lightcone)
lightcone = T([1,2,3])([-29.2,-3.5,0.6])(lightcone)

lamp = STRUCT([lampcil,lampcilbase,lampsquare,lightcone])
lamps = COLOR(GREY1)(STRUCT(NN(10)([lamp,T(1)(12)])))

#road details: bus stop
bussit = T([1,2,3])([-27,-2,1])(CUBOID([4,1.5,0.5]))
busback = T([1,2,3])([-27,-0.7,1])(CUBOID([4,0.3,4]))
busroof = T([1,2,3])([-27,-2.4,5])(CUBOID([4,2,0.1]))
busstop = COLOR(GREY1)(STRUCT([bussit,busback,busroof]))

#depth of buildings
BD = -13
#building
b1 = T([1,2])([-30,-18])(CUBOID([10,BD,10]))
b2 = T([1,2])([-17,-18])(CUBOID([8,BD,20]))
b3 = T([1,2])([-6,-18])(CUBOID([11,BD,13]))
b4 = T([1,2])([8,-18])(CUBOID([6,BD,4]))
b5 = T([1,2])([17,-18])(CUBOID([20,BD,30]))
b5a = T([1,2,3])([19.5,-19,30])((CUBOID([15,BD+2,20])))
b6 = T([1,2])([40,-18])(CUBOID([5,BD,25]))
b7 = T([1,2])([48,-18])(CUBOID([13,BD,15]))
b8 = T([1,2])([64,-18])(CUBOID([16,BD,22]))

buildings = COLOR(BLUE1)(STRUCT([b1,b2,b3,b4,b5,b6,b7,b8,b5a]))

#road borders
roadbord1 = T([1,2,3])([24,0,1])(CUBOID([56,0.3,1.5]))
roadbord2 = T([1,2,3])([-30,0,1])(CUBOID([50,0.3,1.5]))
roadbords = COLOR(GREY2)(STRUCT([roadbord1,roadbord2]))

details = STRUCT([sidewalks,road,buildings,lamps,busstop,roadbords])

solid_model_3D = T([2,3])([65,15])(solid_model_3D)

#hill
ptshill = [[0,0,0],[0,100,0],[100,100,0],[100,0,0],
		   [25,25,15],[25,75,15],[75,75,15],[75,25,15]]

hill0 = JOIN(AA(MK)(ptshill))
hill0 = COLOR(OCRA0)(T([1,2])([-25,40])(hill0))

#background
bkg = [[0,0],[0,150],[110,150],[110,0]]
bkg1 = JOIN(AA(MK)(bkg))
bkg3d = COLOR(OCRA0)(PROD([bkg1, Q(1)]))
bkg3d = T(1)(-30)(bkg3d)

#path to the awesome temple
smallpath = COLOR(GREY2)(T([1,2,3])([20,0,1])(CUBOID([4,42,0.01])))

#border for path
pathbord1 = T([1,2,3])([24,0.3,1])(CUBOID([0.3,42,0.3]))
pathbord2 = T(1)(-4.3)(pathbord1)
pathbords = COLOR(GREY3)(STRUCT([pathbord1,pathbord2]))

#stairs to the awesome temple
stairs1 = STRUCT([T([2])([1*i])(CUBOID([4,1,i*0.6]))for i in range(1,25)])
stairs1 = COLOR(GREY2)(T([1,2,3])([20,40,1])(stairs1))

ptsstairs = [[0,0,0],[0,25,0],[0,25,15],
			 [-0.3,0,0],[-0.3,25,0],[-0.3,25,15]]
stairborders1 = JOIN(AA(MK)(ptsstairs))
stairborders1 = T([1,2,3])([20,40,1])(stairborders1)
stairborders2 = T(1)(4.3)(stairborders1)

stairborders = COLOR(GREY3)(STRUCT([stairborders1,stairborders2]))

pathbkg = STRUCT([hill0,bkg3d,smallpath,stairs1,pathbords,stairborders])

#hill details: trees
BROWN1 = rgb([110, 65, 0])
GREEN1 = rgb([0, 150, 0])
trunk = COLOR(BROWN1)(T(3)(1)(CYLINDER([1,5])(10)))
foliage0 = T(3)(5)(CONE([6,10])(20))
foliage1 = T(3)(11)(CONE([4,10])(20))
foliage2 = T(3)(17)(CONE([2.7,10])(20))
foliage = COLOR(GREEN1)(STRUCT([foliage0,foliage1,foliage2]))

#tree
tree = STRUCT([trunk,foliage])
tree1 = T([1,2])([0,10])(tree)
tree2 = T([1,2])([4,32])(tree)
tree3 = T([1,2])([-15,25])(tree)
trees = STRUCT([tree1,tree2,tree3])

#what about a kiosk?
kroof = COLOR(BEIGE)(T(3)(10)(CONE([10,5])(20)))
ksupport = T([1,2,3])([0,9,1])(CYLINDER([0.2,9])(10))
ksupports = COLOR(GREY3)(STRUCT(NN(8)([ksupport,R([1,2])(PI/4)])))
kchair = T([1,2,3])([0,5,1])(CUBOID([2,2,1]))
kchairs = COLOR(GREY3)(STRUCT(NN(5)([kchair,R([1,2])(PI/2.5)])))

kiosk = STRUCT([kroof,ksupports,kchairs])

kiosk = T([1,2])([50,20])(kiosk)

total = STRUCT([solid_model_3D,details,pathbkg,trees,kiosk])
VIEW(total)
#VIEW(SKELETON(1)(total))

