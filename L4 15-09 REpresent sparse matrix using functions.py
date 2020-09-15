#A.pavan kumar 121910313047
# Program to Represent Sparse Matrix using functions
#Logic to represent Sparse Matrix
def sparse_matrix(arr):
    sp = []
    r = len(arr) 
    c = len(arr[0])
    # Finding the non zero elements
    for i in range(r):
        for j in range(c):
            if arr[i][j]!=0:
                sp.append([i,j,arr[i][j]])
    return sp

#Logic to print martix
def print_martix(arr):
    for i in arr:
        print(*i)

# Declaring the 2-D matrix and printing its sparse matrix
arr = [[0,0,0,3],[0,1,3,0],[9,0,0,0],[0,0,0,4]]
print("The Original Matrix")
print_martix(arr)

print()

#Printing the sparse matrix
sparse = sparse_matrix(arr)
print("The Sparse Matrix")
print_martix(sparse)
