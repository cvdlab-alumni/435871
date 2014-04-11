from pyplasm import *
from larcc import *
from myfont import *

#Homework 1 - exercise1
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

#function for a ball
def larBall(radius=1):
	def larBall0(shape=[10,10]):
		V,CV = checkModel(larSphere(radius)(shape))
		return V,[range(len(V))]
	return larBall0


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
floor0_3d = COLOR(OCRA0)(PROD([floor0, Q(1)]))

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
column = COLOR(OCRA3A)(JOIN(CYLINDER([0.8,H4-H3])(20)))
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

interiorTOT = COLOR(OCRA3A)(STRUCT([interior1, interior2, interior3, interior1b, interior2b]))

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

#------> RIAGGIUNGERE floor0_3d
two_and_half_model = STRUCT([floor0_3d,floor1_3d,floor2_3d,floor3_3d,floor4_3d])
solid_model_3D = STRUCT([two_and_half_model,vertical])

#final view
VIEW(solid_model_3D)
#VIEW(SKELETON(1)(solid_model_3D))

