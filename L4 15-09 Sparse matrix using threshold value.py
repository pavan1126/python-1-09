# Program to Represent a Sparse Matrix with Threshold value
# J. Raghuramjee - 121910313004

# Function to represent the Sparse Matrix
def sparse_matrix(arr):
    sp = []
    r = len(arr) # Number of Rows
    c = len(arr[0]) # Number of columns
    # Finding the non zero elements
    for i in range(r):
        for j in range(c):
            if arr[i][j]!=0:
                sp.append([i,j,arr[i][j]])
    return sp

# Function to print martix
def print_martix(arr):
    if arr==[]: print('EMPTY MATRIX')
    for i in arr:
        print(*i)

arr = [] # Declaring the matrix

# Taking the matrix input
r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of columns : "))
t = int(input("Enter the threshold value : "))
for i in range(r):
    dup = list(map(int,input().split()))
    for j in range(c):
        if dup[j]<=t:
            dup[j]=0
    arr.append(dup)

print("The Original Matrix after applying the threshold value")
print_martix(arr)

print()

# Printing the sparse matrix
sparse = sparse_matrix(arr)
print("The Sparse Matrix")
print_martix(sparse)
