#Let say we have an unordered list
#We are try to find whatever list elements' are unique or not.
#we will use transform and conquer algorithm design which is type of instance simplification.

A = [1,2,3,16,7,12,9,-1]
A.sort()

flag = True

for i in range(len(A)-1):
    if A[i] == A[i+1]:
        flag = False
        break

if flag:
    print("All elements are unique.")
else:
    print("Fail")
