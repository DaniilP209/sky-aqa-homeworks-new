def square (side): 
    area  = side * side
    return int(area) if area == int(area) else int(area) + 1
side_length = 3.14
result = square(side_length)
print("Площадь квадрата:", result)