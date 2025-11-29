import math

def distance(p1,p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1]-p2[1])**2)
def minDistance(points):
    n = len(points)
    
    min_dist = float('inf')
    
    for i in range(n):
        for j in range(i+1,n):
            dist = distance(points[i],points[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist
    
print(minDistance([[-1, -2], [0, 0], [1, 2], [2, 3]]))
