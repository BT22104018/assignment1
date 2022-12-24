import math
angle = 0

while angle <= 345:
    sin = (math.sin(math.degrees(angle)))
    cos = (math.cos(math.degrees(angle)))
    print("the sine of ", angle," is",round(sin,4)," and the cosine of ", angle," is",round(cos,4))
    angle = angle + 15