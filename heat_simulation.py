# v2.0
from __future__ import division
from matrix_class import *
d = MatrixImpN([[1, 1], [1, 1]])
print d


# init material temperatures K
wall_Temp = 18.0
inside_Temp = 20.0
window_Temp = 10.0
outside_Temp = 7.0

# init thermal masses J/K
wall_mass = 278666.0 + (2 / 3)
inside_mass = 45600.0
window_mass = 47040.0
outside_mass = 10.0**9

# init interfaces W/K
wall_inside_conduction = 269.2656
inside_window_conduction = 40.65
window_outside_conduction = 90.90909091

# init joules
wall_Joules = wall_Temp * wall_mass
inside_Joules = inside_Temp * inside_mass
window_Joules = window_Temp * window_mass
outside_Joules = outside_Temp * outside_mass
# init time
time = 0.0
dt = 60

# simulation
a = MatrixImpN([[1 - wall_inside_conduction * dt * (1 / wall_mass), wall_inside_conduction * dt * (1 / wall_mass), 0],
                [wall_inside_conduction * dt * (1 / inside_mass), 1 - wall_inside_conduction * dt * (1 / inside_mass) - inside_window_conduction * dt * (1 / inside_mass), inside_window_conduction * dt * (1 / inside_mass)],
                [0, inside_window_conduction * dt * (1 / window_mass), 1 - inside_window_conduction * dt * (1 / window_mass)]])

b = MatrixImpN([[wall_Temp], [inside_Temp], [window_Temp]])

for i in range(60):
    b = a * b
    print
    print
    print b
    # calculate energy flow part 1 Watts
    wall_to_inside_Watts = wall_inside_conduction * wall_Temp
    inside_to_wall_Watts = wall_inside_conduction * inside_Temp
    inside_to_window_Watts = inside_window_conduction * inside_Temp
    window_to_inside_Watts = inside_window_conduction * window_Temp
    # window_to_outside_Watts = window_outside_conduction * window_Temp
    # outside_to_window_Watts = window_outside_conduction * outside_Temp
    ##################################################################
    # calculate energy flow part 2 Joules
    wall_to_inside_Joules = wall_to_inside_Watts * dt
    inside_to_wall_Joules = inside_to_wall_Watts * dt
    inside_to_window_Joules = inside_to_window_Watts * dt
    window_to_inside_Joules = window_to_inside_Watts * dt
    # window_to_outside_Joules = window_to_outside_Watts * dt
    # outside_to_window_Joules = outside_to_window_Watts * dt
    #######################################################
    # calculate joules in each mass
    wall_Joules += inside_to_wall_Joules - wall_to_inside_Joules
    # inside_Joules += wall_to_inside_Joules - inside_to_wall_Joules
    inside_Joules += wall_to_inside_Joules + window_to_inside_Joules - inside_to_wall_Joules - inside_to_window_Joules
    window_Joules += inside_to_window_Joules - window_to_inside_Joules
    # window_Joules += inside_to_window_Joules + outside_to_window_Joules\
    # - window_to_inside_Joules - window_to_outside_Joules
    # outside_Joules += window_to_outside_Joules - outside_to_window_Joules
    ####################################################################################################################
    # calculate new temperatures
    wall_temp_test = wall_Temp * (1 - wall_inside_conduction * dt * (1 / wall_mass)) + \
        inside_Temp * (wall_inside_conduction * dt * (1 / wall_mass))

    # wall_Temp * (wall_inside_conduction * dt) + inside_Temp * (-wall_inside_conduction * dt)
    wall_Temp = wall_Joules * (1 / wall_mass)
    print wall_temp_test, wall_Temp
    inside_Temp = inside_Joules * (1 / inside_mass)
    window_Temp = window_Joules * (1 / window_mass)
    outside_Temp = outside_Joules * (1 / outside_mass)
    ##################################################
    print "{wall_Temp:4.2f} K Wall".format(wall_Temp=wall_Temp),
    print "{inside_Temp:4.2f} K Inside".format(inside_Temp=inside_Temp),
    print "{window_Temp:4.2f} K Window".format(window_Temp=window_Temp),
    # print "{outside_Temp:4.2f} K Outside".format(outside_Temp=outside_Temp)
    time += dt


print time, "Time t"

# [a b c] [x]   [ax+by+cz]
# [d e f] [y] = [dx+ey+fz]
# [g h i] [z]   [gx+hy+iz]
#
# [a b] [x]   [ax+by]   [x']
# [d e] [y] = [dx+ey] = [y']
#
# [wall_inside_conduction,0] [wall_Temp]    = [wall_to_inside_Watts] ... [new_wall_Temp]
# [0,wall_inside_conduction] [inside_Temp]  = [inside_to_wall_Watts] ... [new_inside_Temp]