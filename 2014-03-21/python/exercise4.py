from pyplasm import *

#Homework 1 - exercise3
#Author: Davide Violante

#function for custom colors with 0:255 numbers
def rgb(c):
	return [c[0]/255.0, c[1]/255.0, c[2]/255.0]

#custom colors
OCRA0 = rgb([140, 90, 0.0])
OCRA1 = rgb([160, 110, 0.0])
OCRA2 = rgb([180, 130, 0.0])
OCRA3 = rgb([200, 150, 0.0])
OCRA3A = rgb([220, 170, 0.0])
OCRA4 = rgb([230, 180, 0.0])
OCRA5 = rgb([237, 190, 0.0])
OCRA6 = rgb([244, 200, 0.0])
OCRA7 = rgb([250, 210, 0.0])
OCRA8 = rgb([255, 220, 0.0])
OCRA9 = rgb([80, 40, 0.0])

#def heights of the floors
H1 = 1
H2 = 2
H3 = 3
H3col = 3.001 #prevent glittering
H3int = 3.002 #prevent glittering
H4 = 13

#floor0: sand
pts0 = [[0,0],[0,50],[50,50],[50,0]]
floor0 = JOIN(AA(MK)(pts0))
floor0_3d = COLOR(OCRA0)(PROD([floor0, Q(1)]))

#floor1: 1st big stair
pts1 = [[0,0],[0,20],[40,20],[40,0]]
floor1 = JOIN(AA(MK)(pts1))
floor1_3d = COLOR(OCRA1)(T([1,2,3])([5,15,H1])(PROD([floor1, Q(1)])))

#floor2: 2nd big stair
pts2 = [[0,0],[0,19],[39,19],[39,0]]
floor2 = JOIN(AA(MK)(pts2))
floor2_3d = COLOR(OCRA2)(T([1,2,3])([5.5,15.5,H2])(PROD([floor2, Q(1)])))

#floor3: interior and columns
pts3 = [[0,0],[0,18],[38,18],[38,0]]
floor3base = COLOR(OCRA3)(JOIN(AA(MK)(pts3)))
floor3base = T([1,2,3])([6,16,H3])(floor3base)

#column
column = COLOR(OCRA3A)(JOIN(CYLINDER([0.8,H4-H3])(20)))
column = T([1,2,3])([7,17,H3col])(column)

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

interior1 = CUBOID([23,0.5,H4-H3])
interior1 = T([1,2,3])([12,20,H3int])(interior1)
interior2 = CUBOID([2,3,H4-H3])
interior2 = T([1,2,3])([15,20.5,H3int])(interior2)
interior3 = CUBOID([0.5,9,H4-H3])
interior3 = T([1,2,3])([31,20.5,H3int])(interior3)

interior1b = T([2])([9])(interior1)
interior2b = T([2])([5.5])(interior2)

interiorTOT = COLOR(OCRA3A)(STRUCT([interior1, interior2, interior3, interior1b, interior2b]))

floor3_3d = STRUCT([columnsTOT,interiorTOT])

#floor4: top of the columns (roof)
floor4a = T([1,2])([2,2])((CUBOID([34,14])))
floor4b = CUBOID([38,18])
floor4 = DIFFERENCE([floor4b,floor4a])
floor4 = T([1,2,3])([6,16,H4])(PROD([floor4, Q(1)]))

floor4coltop = CUBOID([2,9.5,1])
floor4coltopfront = T([1,2,3])([12,20,H4])(floor4coltop)
floor4coltoprear = T([1,2,3])([33,20,H4])(floor4coltop)
floor4_3d = COLOR(OCRA4)((STRUCT([floor4,floor4coltopfront,floor4coltoprear])))

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

#triangle supporter
trave = CUBOID([-2,18,2])
trave = T([1,2,3])([8,16,H4+1])(trave)
trave_small1 = S([1,2,3])([0.2,0.97,0.8])(trave)
trave_small1 = T([1,2,3])([4.7,0.74,3])(trave_small1)
trave_small2 = T([1,2,3])([2,0,0])(trave_small1)
travediff = COLOR(OCRA7)(DIFFERENCE([trave,trave_small1,trave_small2]))

north = STRUCT([tridiff,travediff])

#south plan
south = T([1])([36])(north)

#north south - together
vertical = STRUCT([north, south])

#stairs
stairs1 = STRUCT([T([1])([1*i])(CUBOID([1,5,i*0.12]))for i in range(1,10)])
stairs1 = COLOR(OCRA0)(T([1,2,3])([-10,18,0])(stairs1))
stairs2 = T([1,2,3])([0,9,0])(stairs1)
borderstairs = STRUCT([T([1])([1*i])(CUBOID([1,0.5,i*0.2]))for i in range(1,10)])
borderstairs = T([1,2,3])([-10,17.5,0])(borderstairs)
borderstairs2 = T([1,2,3])([0,5.5,0])(borderstairs)
stairs_r = STRUCT([stairs1,COLOR(OCRA9)(borderstairs),COLOR(OCRA9)(borderstairs2)])
stairs_l = T([1,2,3])([0,10,0])(stairs_r)

stairs = STRUCT([stairs_r,stairs_l])
two_and_half_model = STRUCT([floor0_3d,floor1_3d,floor2_3d,floor3_3d,floor4_3d,stairs])
solid_model_3D = STRUCT([two_and_half_model,vertical])

#final view
VIEW(solid_model_3D)
VIEW(SKELETON(1)(solid_model_3D))


exit()