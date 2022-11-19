def trapping_rain_water(elevations):
    n = len(elevations)
    left_walls = [0] * n
    right_walls = [0] * n

    max_left_wall = 0
    for i in range(n):
        left_walls[i] = max_left_wall
        max_left_wall = max(elevations[i], max_left_wall)  # 1

    max_right_wall = 0
    for i in reversed(range(n)):
        right_walls[i] = max_right_wall
        max_right_wall = max(elevations[i], max_right_wall)  # 1

    total_water = 0
    for i in range(len(elevations)):
        elevation = elevations[i]
        lowest_wall = min(left_walls[i], right_walls[i])
        if lowest_wall > elevation:  # 2
            total_water += lowest_wall - elevation

    return total_water

#Driver code
inputs = ["3 2 1 2 2 3 2","3 2 1 2 2 3"]
for i in range(len(inputs)):
      elevs = [int(x) for x in inputs[i].split()]
      print("Trapping rain water : ",trapping_rain_water(elevs))
