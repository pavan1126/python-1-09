#A.pavan kumar - 121910313047
#program on  Selction sort iterative


# Function for selection sort
def selectionsort(a):
	for i in range(len(a)):
		p = i
		for j in range(i,len(a)):
			if a[j]<a[p]:
				p = j
		a[p],a[i] = a[i],a[p]
	print("selectionsort :   ",a)

# Taking array input
l = list(map(int,input("Enter elements to sort: ").split()))
selectionsort(l)
