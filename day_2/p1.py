# Calculate the horizontal position and depth you would 
# have after following the planned course. What do you 
# get if you multiply your final horizontal position by 
# your final depth?


total_up = 0
total_down = 0
total_forward = 0

for each in open('horizontal_into_depth.txt', 'r'):
    direction, distance = each.split(" ")
    distance = int(distance)
    if direction == 'up':
        total_up += distance
    elif direction == 'down':
        total_down += distance
    elif direction == 'backwards':
        total_forward -= distance
    elif direction == 'forward':
        total_forward += distance

total_depth = total_down - total_up
print(total_forward * total_depth)