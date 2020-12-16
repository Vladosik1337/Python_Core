def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left


print('Will you make it?', zero_fuel(50, 25, 2))