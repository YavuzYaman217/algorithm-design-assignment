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
    
# Test Case 1: Example from code
points = [[-1, -2], [0, 0], [1, 2], [2, 3]]
print(f"Test 1: {minDistance(points):.4f} (Expected: 1.4142)")

# Test Case 2: Points on a line
points = [[0, 0], [1, 0], [2, 0], [3, 0]]
print(f"Test 2: {minDistance(points):.4f} (Expected: 1.0)")

# Test Case 3: Points at corners of square
points = [[0, 0], [1, 0], [0, 1], [1, 1]]
print(f"Test 3: {minDistance(points):.4f} (Expected: 1.0)")

# Test Case 4: Two points only
points = [[0, 0], [3, 4]]
print(f"Test 4: {minDistance(points):.4f} (Expected: 5.0)")

# Test Case 5: Overlapping points
points = [[1, 1], [1, 1], [5, 5]]
print(f"Test 5: {minDistance(points):.4f} (Expected: 0.0)")

# Test Case 6: Points in diagonal line
points = [[0, 0], [1, 1], [2, 2], [3, 3]]
print(f"Test 6: {minDistance(points):.4f} (Expected: 1.4142)")

# Test Case 7: Close and far points
points = [[0, 0], [0.5, 0.5], [100, 100]]
print(f"Test 7: {minDistance(points):.4f} (Expected: 0.7071)")

# Test Case 8: Negative coordinates
points = [[-5, -5], [-3, -3], [0, 0]]
print(f"Test 8: {minDistance(points):.4f} (Expected: 2.8284)")
