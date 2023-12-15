def point_in_rect(rect, p):
    n = len(rect)
    inside = False
    j = n - 1
    for i in range(n):
        if ((rect[i][1] > p[1]) != (rect[j][1] > p[1])) and (p[0] < (rect[j][0] - rect[i][0]) * (p[1] - rect[i][1]) / (rect[j][1] - rect[i][1]) + rect[i][0]):
            inside = not inside
        j = i
    return inside
 
# Example usage
R = [(10, 10), (10, -10), (-10, -10), (-10, 10)]
P = (0, 0)
print(point_in_rect(R, P)) 
 
R = [(10, 10), (10, -10), (-10, -10), (-10, 10)]
P = (20, 20)
print(point_in_rect(R, P))