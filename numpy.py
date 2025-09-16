import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)
# print("First element : ", arr[0])

# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)
# print(arr[0][0])
# print(arr[0][1])
# print(arr[0][2])
# print(arr[1][0])
# print(arr[1][1])
# print(arr[1][2])

'Code to find the dimension of the array'
# b = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(b)
# print(b.ndim)

'negative indexing in 2d array'
# a = np.array([[1,2,3,4,5],[6,7,8,9,0]])
# print(a[1,-1])

'Slicing in 1d array'
# arr = np.array([1,2,3,4,5,6,7,8,9,0])
# print(arr[:-1])
# print(arr[0::2])
# print(arr.dtype)

# a = np.array([1,2,3,4,5])
# # x = a.copy()
# a[0]=100
# x = a.copy()
# print(a)
# print(x)

'Iterating a 1d array'
# arr = np.array([1,2,3,4,5])
# for i in arr:
#     print(i)

# arr = np.array([[1,2,3],[4,5,6]])
# for i in arr:
#     print(i)

'Shape of the array'
# arr = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr.shape) # 2rows 4columns 

'Reshaping 1d to 2d array'
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# brr = arr.reshape(3,4)
# print(brr)

'Joining 2 arrays'
# arr1 = np.array([1,2,3,4])
# arr2 = np.array([5,6,7,8])
# arr3 = np.concatenate((arr1,arr2))
# print(arr3)

'Splitting an array'
# arr1 = np.array([1,2,3,4,5,6,7,8])
# arr2 = np.array_split(arr1,6)
# print(arr2)

'Sorting an array'
# arr1 = np.array([5,7,8,4,9,1,2,3,6,2])
# arr2 = np.sort(arr1)
# print(arr2)

# arr3 = np.array(["car", "plane", "bus", "truck", "loader", "bike"])
# arr4 = np.sort(arr3)
# print(arr4)

'Element search in an array. Returns the index position of the searched item'
# arr = np.array([1,2,3,4,4,5,6,7,8,9,9])
# x = np.where(arr == 9)
# print(x)

# x = np.where(arr%2 == 0)
# print(x)

'Filtering an array. Can be done using boolean index list'
# arr1 = np.array([1,2,3,4])
# x = [True,False,True,False]
# arr2 = arr1[x]
# print(arr2)

'Generating random integer and array'

# from numpy import random
# x = random.randint(100)
# print(x)

# x = random.randint(100,size=(5))
# print(x)

# arr = np.array([1,2,3,4])
# print(arr[2]+arr[3])

# arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr[1,4])

# arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(arr[0,1,2])

# arr=np.array([1,2,3,4,5,6,7])
# print(arr[::2])

# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(2,3,2)
# print(newarr)

# arr=np.array(["banana","cherry","apple"])
# print(np.sort(arr))