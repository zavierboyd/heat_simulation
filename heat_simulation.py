#v1.0 
from __future__ import division
#init room temperatures
room1 = 100.0
room2 = 25.0
room3 = 0.0

#init variables
change1_2 = 0
change2_3 = 0
changeT = 0
t=0

#init things that can't change
uValue1_2 = 1/10.0
uValue2_3 = 6.0
dt=1
area = ((0.3*4)+0.02)*((0.3*12)+0.2) #m^2

b2 = uValue2_3 * area
c2 = b2 * dt

print area
heatCapacity2 = 324266+(2.0/3.0)
heatCapacity3 = 1

#simulation
while room2 > 10:
#	#calculate temprature of room1 to room2
#	difference1_2 = room1-room2
#	a1 = uValue1_2 * difference1_2
#	b1 = a1 * area
#	c1 = b1 * dt
#	change1_2 = c1 / heatCapacity2
	
	#calculate temprature of room2 to room3
	difference2_3 = room3-room2
	a2 = c2 * difference2_3
	change2_3 = a2 / heatCapacity2
	
	#calculate total temprature differince
	#changeT = change1_2 - change2_3
	changeT = change2_3
	
	#apply temprature differince
	room2 += changeT
	
	#add delta time to time
	t += dt
	
	#print tempratures
	#print room1,"room1 Kelvin",
	print room2,"room2 Kelvin",
	print room3,"room3 Kelvin"
	
#print total time of simulation
print t