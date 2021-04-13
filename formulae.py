import math

#v = angle_velocity1 t = theta m = mass l = length g = gravity


def firstaccn(t1, t2, m1, m2, l1, l2, g, v1, v2):
    numerator1 = -g * (2 * m1 + m2) * math.sin(t1)
    numerator2 = -m2 * g * math.sin(t1 - 2 * t2)
    numerator3 = -2 * math.sin(t1 - t2)
    numerator4 = m2 * ((v2 * v2) * l2 + (v1 * v1) * l1 * math.cos(t1 - t2))
    numerator = numerator1 + numerator2 + (numerator3 * numerator4)
    denominator = l1 * (2 * m1 + m2 - m2 * math.cos(2 * t1 - 2 * t2))

    return float(numerator / denominator)


def secondaccn(t1, t2, m1, m2, l1, l2, g, v1, v2):
    numerator1 = 2 * math.sin(t1 - t2)
    numerator2 = (v1 * v1) * l1 * (m1 + m2) + g * (m1 + m2) * math.cos(t1)
    numerator3 = (v2 * v2) * l2 * m2 * math.cos(t1 - t2)
    numerator = numerator1 * (numerator2 + numerator3) 
    denominator = l2 * (2 * m1 + m2 - m2 * math.cos(2 * t1 - 2 * t2))

    return float(numerator / denominator)
    

    
