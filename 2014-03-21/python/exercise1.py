from pyplasm import *

#Homework 1 - exercise1
#Author: Davide Violante

#custom colors con numeri da 0 a 255
def rgb(c):
	return [c[0]/255.0, c[1]/255.0, c[2]/255.0]

OCRA0 = rgb([140, 90, 0.0])
OCRA1 = rgb([160, 110, 0.0])
OCRA2 = rgb([180, 130, 0.0])
OCRA3 = rgb([200, 150, 0.0])
OCRA4 = rgb([220, 170, 0.0])

#floor0: sand
pts0 = [[0,0],[0,50],[50,50],[50,0]]
floor0 = COLOR(OCRA0)(JOIN(AA(MK)(pts0)))

#floor1: 1st stair
pts1 = [[0,0],[0,20],[40,20],[40,0]]
floor1 = COLOR(OCRA1)(JOIN(AA(MK)(pts1)))
floor1 = T([1,2,3])([5,15,0.001])(floor1)

#floor2: 2nd stair
pts2 = [[0,0],[0,19],[39,19],[39,0]]
floor2 = COLOR(OCRA2)(JOIN(AA(MK)(pts2)))
floor2 = T([1,2,3])([5.5,15.5,0.002])(floor2)

#floor3: interior and columns
pts3 = [[0,0],[0,18],[38,18],[38,0]]
floor3 = COLOR(OCRA3)(JOIN(AA(MK)(pts3)))
floor3 = T([1,2,3])([6,16,0.003])(floor3)

#column
column = COLOR(OCRA4)(CIRCLE(0.8)([10,10]))
column = T([1,2,3])([7,17,0.004])(column)

#cloning columns
columns_x = STRUCT([column, T(1)(3.28)]*12)
columns_y = STRUCT([column, T(2)(3.2)]*6)
columns_xcopy = STRUCT([columns_x, T(2)(16)]*2)
columns_ycopy = STRUCT([columns_y, T(1)(36.08)]*2)
column2fronta = T([1,2])([5.5,6])(column)
column2frontb = T([1,2])([5.5,9.5])(column)
columns_front = STRUCT([column2fronta, column2frontb])
columns_rear = STRUCT([columns_front, T(1)(22)]*2)

columnsTOT = STRUCT([columns_x, columns_y, columns_xcopy, columns_ycopy, columns_front, columns_rear])

interior1 = COLOR(OCRA4)(CUBOID([23,0.5]))
interior1 = T([1,2,3])([12,20,0.004])(interior1)
interior2 = COLOR(OCRA4)(CUBOID([2,3]))
interior2 = T([1,2,3])([15,20.5,0.004])(interior2)
interior3 = COLOR(OCRA4)(CUBOID([0.5,9]))
interior3 = T([1,2,3])([31,20.5,0.004])(interior3)

interior1b = T([2])([9])(interior1)
interior2b = T([2])([5.5])(interior2)

interiorTOT = STRUCT([interior1, interior2, interior3, interior1b, interior2b])

floor3 = STRUCT([floor3,columnsTOT,interiorTOT])

#ri-aggiungere floor0 alla fine, tolto per evitare di fondere la rotella per zoommare
floorTOT = STRUCT([floor1,floor2,floor3])

building = STRUCT([floorTOT])

VIEW(building)


exit()